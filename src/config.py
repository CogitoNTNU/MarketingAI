import os
from dotenv import load_dotenv

#a class for defining the config variables
class Config():
    def __init__(self, path='.env', gpt_model="gpt-3.5-turbo"):
        self.path = path
        self.GPT_MODEL = gpt_model
        load_dotenv(dotenv_path=path)
        self.API_KEY = os.getenv('API_KEY')
    
    def get_testcase(self, testcase):
        if (self.path == "test.env"):
            return os.getenv(testcase)
        else:
            return "Wrong config file for testing"

