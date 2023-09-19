from src.gpt.gpt_api import *
import pytest

@pytest.mark.apitest
def test_request_chat_completion_as_system():
    # Act
    result = request_chat_completion(None, "system", "I am fine, how are you?")
    # Assert
    assert isinstance(result,str), "Result is not a string"

@pytest.mark.apitest
def test_request_chat_completion_as_user():
    # Act
    result = request_chat_completion(None, "user", "I am fine, how are you?")
    # Assert
    assert isinstance(result,str), "Result is not a string"

@pytest.mark.apitest
def test_request_chat_completion_as_assistant():
    # Act
    result = request_chat_completion(None, "assistant", "I am fine, how are you?")
    # Assert
    assert isinstance(result,str), "Result is not a string"

@pytest.mark.apitest
def test_with_previous_message_as_system():
    # Arrange
    previous_message = {"role": "system", "content": "Hello, how are you?"}
    # Act
    result = request_chat_completion(previous_message, "system", "I am fine, how are you?")
    # Assert
    assert isinstance(result,str), "Result is not a string"

@pytest.mark.apitest
def test_with_previous_message_as_user():
    # Arrange
    previous_message = {"role": "system", "content": "Hello, how are you?"}
    # Act
    result = request_chat_completion(previous_message, "user", "I am fine, how are you?")
    # Assert
    assert isinstance(result,str), "Result is not a string"

@pytest.mark.apitest
def test_with_previous_message_as_assistant():
    # Arrange
    previous_message = {"role": "system", "content": "Hello, how are you?"}
    # Act
    result = request_chat_completion(previous_message, "assistant", "I am fine, how are you?")
    # Assert
    assert isinstance(result,str), "Result is not a string"
