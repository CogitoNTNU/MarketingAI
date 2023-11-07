from src.assembler.image_text_assambler import assemble_image
from src.image_generation.image_generator import ImageGenerator, create_image_generator, download_and_save_image
from src.gpt.text_generator import request_chat_completion
from src.assembler.text_color import chose_color
from src.assembler.text_size_pos import chose_font_size
from src.function_calling.image_classifier import classify_text
import logging

logging.basicConfig(filename='PropagandaAI.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

logger.info('Starting PropagandaAI')
user_prompt: str = input('What shall PropogandaAI generate: ')
image_prompt = "Classic propaganda poster: Bold, primary colors with a powerful " + user_prompt
# result: str = request_chat_completion(None, 'system', prompt)["choices"][0]["message"]["content"]

# Classify image prompt using function calling
classification = classify_text(image_prompt)
print(classification)
logger.info(f'Classification: {classification}')

# # Generate descriptive prompt
# logger.info('Generating descriptive prompt')
image_prompt = "Generate a " + classification + " poster of: " + user_prompt

logger.info('Generating Text on prompt')
logger.info(f'Starting image generation based on prompt: {image_prompt}')

image_generator: ImageGenerator = create_image_generator('dall-e')
image_url = image_generator.generate_image(image_prompt, 512, 512)
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
assemble_image(user_prompt, result, "arial.ttf", 20, chose_color(user_prompt), (0, 0))