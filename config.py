import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

#a class for defining the config variables
class Config():
    def __init__(self):
        self.API_KEY = os.getenv('API_KEY')
   