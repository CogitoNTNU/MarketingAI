import pytest
from src.config import *

test_1 = "test_1"

def test_pass():

    assert test_1 == Config("test.env").get_testcase("TEST_1")
