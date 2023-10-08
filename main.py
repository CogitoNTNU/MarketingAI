from src.assembler.image_text_assambler import assemble_image
from src.image_generation.image_generator import ImageGenerator, download_and_save_image
from src.gpt.gpt_api import request_chat_completion
import logging



# Set up logging
logging.basicConfig(filename='PropagandaAI.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

logger.info('Starting PropagandaAI')
user_prompt: str = input('What shall PropogandaAI generate: ')
image_prompt = "Classic propaganda poster: Bold, primary colors with a powerful " + user_prompt
# result: str = request_chat_completion(None, 'system', prompt)["choices"][0]["message"]["content"]

logger.info('Generating Text on prompt')
logger.info(f'Starting image generation based on prompt: {image_prompt}')

image_generator = ImageGenerator()
image_url = image_generator.generate_image(image_prompt, 512, 512)
print(image_url)

# Save image to file
logger.info('Saving image to file')
download_and_save_image(image_url, user_prompt)

# generate image text
logger.info('Generating image text')
template = f"This is a picture of {image_prompt}. Generate a short captivating and relevant caption for a poster. The response should not contain any other information than the caption."
result = request_chat_completion(None, 'system', template)
# result = "Midterm presentation!"
# Assemble image
logger.info('Assembling image')
assemble_image(user_prompt, result, "arial.ttf", 50, (255, 155, 155), (30, 50))