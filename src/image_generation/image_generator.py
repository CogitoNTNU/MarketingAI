'''
The class is a wrapper class for generating images from a prompt
The class uses the OpenAI API to generate images
'''

from abc import ABC, ABCMeta, abstractmethod
from time import sleep
from typing import Any
import openai
import logging
import json

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
    def __instancecheck__(cls, instance: Any) -> bool:
        return cls.__subclasscheck__(type(instance))
    
    @classmethod
    def __subclasscheck__(cls, subclass: Any) -> bool:
        return (
            hasattr(subclass, 'generate_image') and
            callable(subclass.generate_image)
        )   

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
    Args:
        model_name (str): The name of the model to use. 
            Either 'dall-e' or 'stable-diffusion'
    Returns:
        An image generator
    '''
    model_name = model_name.lower()
    logger.info(f'Creating image generator for model: {model_name}')
    if model_name == 'dall-e':
        image_generator = DallEImageGenerator("dall-e-2")
    elif model_name == 'dall-e-3':
        image_generator = DallEImageGenerator("dall-e-3")
    elif model_name == 'stable-diffusion':
        image_generator = StableDiffusionImageGenerator()
    else:
        raise ValueError(f'Invalid model name: {model_name}')
    return image_generator


class StableDiffusionImageGenerator(ImageGenerator):

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
        url = "https://stablediffusionapi.com/api/v4/dreambooth"

        payload = json.dumps({
            "key": Config().STABLE_DIFFUSION_API_KEY,
            "model_id": "midjourney",
            "prompt": image_prompt,
            "negative_prompt": "text",
            "width": "1024",
            "height": "1024",
            "samples": "1",
            "num_inference_steps": "30",
            "safety_checker": "no",
            "enhance_prompt": "yes",
            "seed": None,
            "guidance_scale": 7.5,
            "multi_lingual": "no",
            "panorama": "no",
            "self_attention": "no",
            "upscale": "no",
            "embeddings_model": None,
            "lora_model": None,
            "tomesd": "yes",
            "use_karras_sigmas": "yes",
            "vae": None,
            "lora_strength": None,
            "scheduler": "UniPCMultistepScheduler",
            "webhook": None,
            "track_id": None
        })

        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        sleep(8)
        logger.info(response.json())

        return response.json()["output"][0]

class DallEImageGenerator(ImageGenerator):
    """
     A class to generate images from a given prompt using the OpenAI API
    """
    MAX_PROMPT_LENGTH = 1000
    SUPPORTED_SIZES = [256, 512, 1024]
    def __init__(self, model_version: str = 'dall-e-3') -> None:
        '''
        Args:
            model_version (str): The version of the model to use. 
                Either 'dall-e-2' or 'dall-e-3'
        '''
        if model_version not in ['dall-e-2', 'dall-e-3']:
            raise ValueError(f'Invalid model version: {model_version}')
        self.model_version = model_version

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
            model=self.model_version,
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