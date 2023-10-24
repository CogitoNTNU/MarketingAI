from src.assembler.image_text_assambler import assemble_image
from src.function_calling.langchain_function_calling import run_agent
from src.function_calling.no_framework_function_calling import prompt_and_parse
from src.image_generation.image_generator import ImageGenerator, create_image_generator, download_and_save_image
from src.gpt.text_generator import request_chat_completion
import logging



# Set up logging
logging.basicConfig(filename='MarketingAI.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

logger.info('Starting MarketingAI')
user_prompt: str = input('What shall MarketingAI generate: ')

# Don't use framework:
prompt_and_parse()


# # Use framework:
# answers = run_agent(user_prompt)
# logger.info(f"Finished running langchain_function_calling.py, result: {answers}")