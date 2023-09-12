import pytest

from src.image_generation.image_generator import ImageGenerator

def test_image_generation_with_empty_string_prompt():
    # Arrange

    image_generator = ImageGenerator()
    no_prompt = ""
    with pytest.raises(ValueError):
        # Act
        result = image_generator.generate_image(no_prompt, 1, 1)
        # Assert

def test_image_generation_with_non_string_prompt():
    # Arrange

    image_generator = ImageGenerator()
    non_string_prompt = 1
    with pytest.raises(TypeError):
        # Act
        result = image_generator.generate_image(non_string_prompt, 1, 1)
        # Assert

def test_image_generation_with_none_prompt():
    # Arrange

    image_generator = ImageGenerator()
    none_prompt = None
    with pytest.raises(TypeError):
        # Act
        result = image_generator.generate_image(none_prompt, 1, 1)
        # Assert

def test_image_generation_with_too_long_prompt():
    # Arrange

    image_generator = ImageGenerator()
    too_long_prompt = "A" * 3001
    with pytest.raises(ValueError):
        # Act
        result = image_generator.generate_image(too_long_prompt, 1, 1)
        # Assert

def test_image_generation_with_non_integer_width():
    # Arrange

    image_generator = ImageGenerator()
    non_integer_width = "1"
    valid_height = 1
    valid_prompt = "A picture of a cat"
    with pytest.raises(TypeError):
        # Act
        result = image_generator.generate_image(valid_prompt, non_integer_width, valid_height)
        # Assert

def test_image_generation_with_non_integer_height():
    # Arrange

    image_generator = ImageGenerator()
    valid_width = 1
    non_integer_height = "1"
    valid_prompt = "A picture of a cat"
    with pytest.raises(TypeError):
        # Act
        result = image_generator.generate_image(valid_prompt, valid_width, non_integer_height)
        # Assert

def test_image_generation_with_too_small_width():
    # Arrange

    image_generator = ImageGenerator()
    too_small_width = 0
    valid_height = 1
    valid_prompt = "A picture of a cat"
    with pytest.raises(ValueError):
        # Act
        result = image_generator.generate_image(valid_prompt, too_small_width, valid_height)
        # Assert

def test_image_generation_with_too_small_height():
    # Arrange

    image_generator = ImageGenerator()
    valid_width = 1
    too_small_height = 0
    valid_prompt = "A picture of a cat"
    with pytest.raises(ValueError):
        # Act
        result = image_generator.generate_image(valid_prompt, valid_width, too_small_height)
        # Assert

def test_image_generation_with_too_large_width():
    # Arrange

    image_generator = ImageGenerator()
    too_large_width = 1025
    valid_height = 1
    valid_prompt = "A picture of a cat"
    with pytest.raises(ValueError):
        # Act
        result = image_generator.generate_image(valid_prompt, too_large_width, valid_height)
        # Assert

def test_image_generation_with_too_large_height():
    # Arrange

    image_generator = ImageGenerator()
    valid_width = 1
    too_large_height = 1025
    valid_prompt = "A picture of a cat"
    with pytest.raises(ValueError):
        # Act
        result = image_generator.generate_image(valid_prompt, valid_width, too_large_height)
        # Assert

@pytest.mark.apitest
def test_image_generation_with_valid_prompt():
    # Arrange

    image_generator = ImageGenerator()
    valid_prompt = "A picture of a cat"
    # Act
    result = image_generator.generate_image(valid_prompt, 1, 1)
    # Assert
    assert result is not None