import os
import openai
from openai.error import OpenAIError
from src.config import Config


try:
    # Set OpenAI API key
    api_key = Config().API_KEY
    openai.api_key = api_key
except:
    print("OpenAI API key not found. Please set the environment variable OPENAI_API_KEY to your API key.")
    exit(1)


def request_chat_completion(previous_message:dict, role:str = "system",message :str = ""):

    try:
        if(not (role == "system" or "user" or "assistant")):
            print("Invalid role")
            return None
        
        if(previous_message):
            response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                previous_message,
                {"role": role, "content": message}
            ]
            )
        else: 
            response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": role, "content": message}, 
            ]
            )
        print(response)
        return response
    except OpenAIError as error:
        print(f"An error has occured while requesting chat completion.")
        print(f"The error: {str(error)}")
        return None
    except Exception as e: 
        print(f"An unexpected error occured: {str(e)}")
        return None