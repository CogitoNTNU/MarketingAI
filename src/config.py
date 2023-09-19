import os
from dotenv import load_dotenv

"""
This module provides the Config class to manage configuration variables
from environment files. It also supports fetching test cases 
ifthe configuration is loaded from a test environment file.
"""

#a class for defining the config variables
class Config():
    def __init__(self, path='.env'):
        self.path = path
        load_dotenv(dotenv_path=path)
        self.API_KEY = os.getenv('API_KEY')
    
    def get_testcase(self, testcase):
        """
        Retrieves the value of a test case from the environment file if it's a test configuration.
        """
        if (self.path == "test.env"):
            return os.getenv(testcase)
        else:
            return "Wrong config file for testing"

