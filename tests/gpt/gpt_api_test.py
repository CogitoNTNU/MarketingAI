from src.gpt.gpt_api import *

def test_request_chat_completion():
    assert request_chat_completion(None, "system", "Hello, how are you?") is not None
    assert request_chat_completion(None, "user", "I am fine, how are you?") is not None
    assert request_chat_completion(None, "assistant", "I am fine, how are you?") is not None

def test_with_previous_message():
    previous_message = {"role": "system", "content": "Hello, how are you?"}
    assert request_chat_completion(previous_message, "user", "I am fine, how are you?") is not None
    assert request_chat_completion(previous_message, "assistant", "I am fine, how are you?") is not None


