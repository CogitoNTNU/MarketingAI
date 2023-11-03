import os
from dotenv import load_dotenv

"""
This module provides the Config class to manage configuration variables
from environment files. It also supports fetching test cases 
ifthe configuration is loaded from a test environment file.
"""

#a class for defining the config variables
class Config():
    def __init__(self, path='.env', gpt_model="gpt-3.5-turbo"):
        self.path = path
        self.GPT_MODEL = gpt_model
        load_dotenv(dotenv_path=path)
        self.API_KEY = os.getenv('API_KEY')
        self.STABLE_DIFFUSION_API_KEY = os.getenv("STABLE_DIFFUSION_API_KEY")
        self.DALL_E_API_KEY = os.getenv("DALL_E_API_KEY")

    
    def get_testcase(self, testcase):
        """
        Retrieves the value of a test case from the environment file if it's a test configuration.
        """
        if (self.path == "test.env"):
            return os.getenv(testcase)
        else:
            return "Wrong config file for testing"
