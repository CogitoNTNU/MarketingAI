# The class is a wrapper class for generating images from a prompt
# The class uses the OpenAI API to generate images

import openai

class ImageGenerator:
    MAX_PROMPT_LENGTH = 1000
    MAX_IMAGE_SIZE = 1024

    def get_user_prompt(self) -> str:
        image_prompt = input('What do you want to generate an image of? ')
        self.validate_prompt(image_prompt)
        return image_prompt

    def validate_prompt(self, image_prompt: str) -> None:
        if not isinstance(image_prompt, str):
            raise TypeError('Prompt must be a string')
        
        if len(image_prompt) == 0:
            raise ValueError('Prompt must not be empty')
        
        if (len(image_prompt) > self.MAX_PROMPT_LENGTH):
            raise ValueError('Prompt must be less than 1000 characters')

    def validate_size(self, width: int, height: int) -> None:
        if not isinstance(width, int):
            raise TypeError('Width must be an integer')
        
        if not isinstance(height, int):
            raise TypeError('Height must be an integer')
        
        if width < 1:
            raise ValueError('Width must be greater than 0')
        
        if height < 1:
            raise ValueError('Height must be greater than 0')
        
        if width > self.MAX_IMAGE_SIZE:
            raise ValueError('Width must be less than 1024')
        
        if height > self.MAX_IMAGE_SIZE:
            raise ValueError('Height must be less than 1024')
        
        if (width != height):
            raise ValueError('Width and height must be equal')
        
        valid_sizes = [256, 512, 1024]
        if (width not in valid_sizes):
            raise ValueError('Width must be 256, 512, or 1024')

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
        self.validate_prompt(image_prompt)
        self.validate_size(width, height)
        size = str(width) + 'x' + str(height)
        openai.api_key = '' # TODO: Make sure this is the way we get environment variables
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