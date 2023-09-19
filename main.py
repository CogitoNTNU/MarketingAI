from src.image_generation import image_generator

import logging

# Set up logging
logging.basicConfig(filename='PropagandaAI.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

logger.info('Starting PropagandaAI')

image_generator = image_generator.ImageGenerator()
image_prompt = image_generator.get_user_prompt()
image = image_generator.generate_image(image_prompt, 512, 512)
print(image)