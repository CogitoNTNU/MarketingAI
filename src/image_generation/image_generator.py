'''
The class is a wrapper class for generating images from a prompt
The class uses the OpenAI API to generate images
'''

import openai

from src.config import Config

class ImageGenerator:
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

    def generate_image(self, image_prompt: str, width: int, height: int) -> dict:
        '''
        Generates an image from a prompt of a certain size
        Args:
            image_prompt (str): The prompt to generate the image from. Must be less than 1000 characters.
            width (int): The width of the image. Must be 256, 512, or 1024
            height (int): The height of the image. Must be 256, 512, or 1024
        Returns:
            A dictionary containing the image url
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
        return response

if __name__ == "__main__":
    image_generator = ImageGenerator()
    image_prompt = image_generator.get_user_prompt()
    response = image_generator.generate_image(image_prompt, 512, 512)
    print(response['data'][0]['url'])