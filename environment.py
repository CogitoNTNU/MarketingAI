import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="secrets.env")

print(os.getenv('API_KEY'))