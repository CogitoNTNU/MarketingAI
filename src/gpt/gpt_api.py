import os
import openai
import config

try:
    # Set OpenAI API key
    api_key = config.api_key
    openai.api_key = api_key
except:
    print("OpenAI API key not found. Please set the environment variable OPENAI_API_KEY to your API key.")
    exit(1)


def request_chat_completion(previous_message:dict, role:str = "system",message :str = ""):

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

request_chat_completion(None,"system", "Cogito is better then Brain")