'''
The class is a wrapper class for generating images from a prompt
The class uses the OpenAI API to generate images
'''

from abc import ABC, ABCMeta, abstractmethod
from typing import Any
import openai
import logging

import requests
from PIL import Image
from io import BytesIO

from src.config import Config

# Setup logger
logger = logging.getLogger(__name__)

class ImageGenerator(ABC):
    '''
    Abstract class for generating images from a given prompt
    '''

    @classmethod
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))
    
    @classmethod
    def __subclasscheck__(cls: ABCMeta, subclass: type) -> bool:
        return (hasattr(subclass, 'generate_image') and 
                callable(subclass.generate_image))

    @abstractmethod
    def generate_image(self, image_prompt: str, width: int, height: int) -> str:
        '''
        Generates an image from a prompt of a certain size
        Args:
            image_prompt (str): The prompt to generate the image from. Must be less than 1000 characters.
            width (int): The width of the image. Must be 256, 512, or 1024
            height (int): The height of the image. Must be 256, 512, or 1024
        Returns:
            The URL of the generated image
        '''
        pass



def create_image_generator(model_name: str) -> ImageGenerator:
    '''
    Creates an image generator based on the config
    Returns:
        An image generator
    '''
    model_name = model_name.lower()
    if model_name == 'dall-e':
        image_generator = DallEImageGenerator()
    else:
        raise ValueError(f'Invalid model name: {model_name}')
    return image_generator


class DallEImageGenerator(ImageGenerator):
    """
     A class to generate images from a given prompt using the OpenAI API
    """
    MAX_PROMPT_LENGTH = 1000
    SUPPORTED_SIZES = [256, 512, 1024]

    def get_user_prompt(self) -> str:
        image_prompt = input('What do you want to generate an image of? ')
        self._validate_prompt(image_prompt)
        return image_prompt

    def _validate_prompt(self, image_prompt: str) -> None:
        if not isinstance(image_prompt, str):
            raise TypeError('Prompt must be a string')
        
        if len(image_prompt) == 0:
            raise ValueError('Prompt must not be empty')
        
        if (len(image_prompt) > self.MAX_PROMPT_LENGTH):
            raise ValueError(f'Prompt must be less than {self.MAX_PROMPT_LENGTH} characters')

    def _validate_size(self, width: int, height: int) -> None:
        if not isinstance(width, int):
            raise TypeError('Width must be an integer')
        
        if not isinstance(height, int):
            raise TypeError('Height must be an integer')
        
        if (width != height):
            raise ValueError('Width and height must be equal')
        
        if (width not in self.SUPPORTED_SIZES):
            raise ValueError(f'Width must be {self.SUPPORTED_SIZES}')

    def generate_image(self, image_prompt: str, width: int, height: int) -> str:
        '''
        Generates an image from a prompt of a certain size
        Args:
            image_prompt (str): The prompt to generate the image from. Must be less than 1000 characters.
            width (int): The width of the image. Must be 256, 512, or 1024
            height (int): The height of the image. Must be 256, 512, or 1024
        Returns:
            The URL of the generated image
        '''
        self._validate_prompt(image_prompt)
        self._validate_size(width, height)
        size = str(width) + 'x' + str(height)
        openai.api_key = Config().API_KEY
        response = openai.Image.create(
            prompt=image_prompt,
            n=1,
            size=size
        )
        parse_url = response["data"][0]["url"]

        logging.info(f'Generated image from prompt: {image_prompt}, size: {size}, url: {parse_url}')

        return parse_url
    

SAVE_PATH = "data/raw_images/"

def download_and_save_image(image_url: str, image_name: str) -> None:
    """ Download and save an image from a given URL. """
    try:
        response = requests.get(image_url)
        response.raise_for_status()  # Check if the request was successful
        
        image = Image.open(BytesIO(response.content))
        image.save(SAVE_PATH + image_name + ".png")
        print(f"Image saved to {SAVE_PATH + image_name + '.png'}")
    except requests.RequestException as e:
        print(f"Failed to fetch image from URL: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")