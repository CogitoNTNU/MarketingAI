from src.image_generation.image_generator import ImageGenerator
from src.gpt.gpt_api import request_chat_completion
import logging

# Set up logging
logging.basicConfig(filename='PropagandaAI.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

logger.info('Starting PropagandaAI')
prompt: str = input('What shall propogandaAI generate: ')
result: str = request_chat_completion(None, 'system', prompt)["choices"][0]["message"]["content"]

logger.info('Generating Text on prompt')
logger.info(f'Starting image generation based on prompt: {result}')

image_generator = ImageGenerator()
image = image_generator.generate_image(result, 512, 512)
print(image)