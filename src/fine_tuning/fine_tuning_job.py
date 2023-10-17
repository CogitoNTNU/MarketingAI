import openai
from src.config import Config

def upload_training_file(file: str) -> str:
    PATH_TO_DATA = "src/fine_tuning/"
    openai.api_key = Config().API_KEY
    response = openai.File.create(file=open(PATH_TO_DATA + file, "rb"), purpose="fine-tune")
    return response

def create_fine_tuning_job(file_id:str, model:str):
    openai.api_key = Config().API_KEY
    openai.FineTuningJob.create(training_file=file_id, model=model)

if __name__ == "__main__":
    response = upload_training_file("propaganda.jsonl")
    print(response)