from src.assembler.image_text_assambler import assemble_image
from src.function_calling.langchain_function_calling import run_agent
from src.image_generation.image_generator import ImageGenerator, create_image_generator, download_and_save_image
from src.gpt.text_generator import request_chat_completion
import logging
from PIL import Image

# Set up logging
logging.basicConfig(filename='PropagandaAI.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

def generate_image_from_prompt(prompt: str, show_on_screen: bool = False) -> Image:
    """ Generates an image from a prompt and saves it to file and returns the image"""
    logger.info('Starting MarketingAI')
    # Create the image prompt
    user_prompt: str = prompt
    image_prompt = f"(Classic propaganda poster: Bold, primary colors) {user_prompt}"

    # Create caption
    image_text_template = f"This is a picture of {image_prompt}. Generate a short captivating and relevant caption for a poster. The response should not contain any other information than the caption."
    image_text = request_chat_completion(None, message=image_text_template)

    # Combine image and text
    logger.info('Generating Text on prompt')
    image_prompt = f"{image_prompt} With the caption '{image_text}'"
    logger.info(f'Starting image generation based on prompt: {image_prompt}')
    image_generator: ImageGenerator = create_image_generator("dall-e-3")
    image_url = image_generator.generate_image(image_prompt, 1024, 1024)
    logger.info(f"Image url: {image_url}")

    # Save image to file
    logger.info('Saving image to file')
    download_and_save_image(image_url, user_prompt)

    # generate image text
    logger.info('Generating image text')
    template = f"This is a picture of {image_prompt}. Generate a short captivating and relevant caption for a poster. The response should not contain any other information than the caption."
    result = request_chat_completion(None, 'system', template)
    logger.info(f'Generated image text: {result}')

    # Assemble image
    logger.info('Assembling image')
    return assemble_image(user_prompt, result, "arial.ttf", 50, (255, 155, 155), (30, 50), show_on_screen)

def valid_prompt(prompt: str) -> bool:
    if len(prompt) > 1000:
        return False
    # Prompt can not have signs that will not be able to have in file name
    if any(char in prompt for char in ['/', '\\', ':', '*', '?', '"', '<', '>', '|']):
        return False
    return True

if __name__ == "__main__":
    user_prompt: str = input('What shall PropogandaAI generate: ')
    while not valid_prompt(user_prompt):
        user_prompt: str = input('Invalid prompt. What shall PropogandaAI generate: ')
    generate_image_from_prompt(user_prompt)