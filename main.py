from src.image_generation.image_generator import ImageGenerator, download_and_save_image
from src.gpt.gpt_api import request_chat_completion
import logging



# Set up logging
logging.basicConfig(filename='PropagandaAI.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

logger.info('Starting PropagandaAI')
prompt: str = input('What shall PropogandaAI generate: ')
result = prompt
# result: str = request_chat_completion(None, 'system', prompt)["choices"][0]["message"]["content"]

logger.info('Generating Text on prompt')
logger.info(f'Starting image generation based on prompt: {result}')

image_generator = ImageGenerator()
image_url = image_generator.generate_image(result, 512, 512)
print(image_url)

# Save image to file
logger.info('Saving image to file')
download_and_save_image(image_url, prompt)