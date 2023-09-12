# The class is a wrapper class for generating images from a prompt
# The class uses the OpenAI API to generate images

import openai
import os

class ImageGenerator:
    def get_user_prompt():
        image_prompt = input('What do you want to generate an image of? ')
        
        if not isinstance(image_prompt, str):
            raise TypeError('Prompt must be a string')
        
        if len(image_prompt) == 0:
            raise ValueError('Prompt must not be empty')

        return image_prompt

    def generate_image(image_prompt: str):
        openai.api_key = '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' # TODO: Make sure this is the way we get environment variables
        response = openai.Image.create(
            prompt=image_prompt,
            n=1,
            size="1024x1024"
        )
        print(response)
        return response

if __name__ == "__main__":
    image_prompt = ImageGenerator.get_user_prompt()
    response = ImageGenerator.generate_image(image_prompt)
    print(response['data'][0]['url'])