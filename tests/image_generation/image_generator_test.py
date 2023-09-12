import pytest

from src.image_generation.image_generator import ImageGenerator

def test_image_generation_with_empty_string_prompt():
    # Arrange

    image_generator = ImageGenerator()
    no_prompt = ""
    with pytest.raises(ValueError):
        # Act
        result = image_generator.generate_image(no_prompt)
        # Assert

def test_image_generation_with_non_string_prompt():
    # Arrange

    image_generator = ImageGenerator()
    non_string_prompt = 1
    with pytest.raises(TypeError):
        # Act
        result = image_generator.generate_image(non_string_prompt)
        # Assert

def test_image_generation_with_none_prompt():
    # Arrange

    image_generator = ImageGenerator()
    none_prompt = None
    with pytest.raises(TypeError):
        # Act
        result = image_generator.generate_image(none_prompt)
        # Assert

def test_image_generation_with_too_long_prompt():
    # Arrange

    image_generator = ImageGenerator()
    too_long_prompt = "A" * 3001
    with pytest.raises(ValueError):
        # Act
        result = image_generator.generate_image(too_long_prompt)
        # Assert

@pytest.mark.apitest
def test_image_generation_with_valid_prompt():
    # Arrange

    image_generator = ImageGenerator()
    valid_prompt = "A picture of a cat"
    # Act
    result = image_generator.generate_image(valid_prompt)
    # Assert
    assert result is not None