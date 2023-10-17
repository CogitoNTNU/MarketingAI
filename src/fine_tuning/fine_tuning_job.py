import openai
from src.config import Config


def upload_training_file(filepath: str) -> str:
    openai.api_key = Config().API_KEY
    response = openai.File.create(file=open(filepath, "rb"), purpose="fine_tune")
    return response["id"]

def create_fine_tuning_job(file_id:str, model:str):
    openai.api_key = Config().API_KEY
    openai.FineTuningJob.create(training_file=file_id, model=model)

    

