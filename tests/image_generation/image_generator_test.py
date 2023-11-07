import pytest

from src.image_generation.image_generator import ImageGenerator, StableDiffusionImageGenerator, create_image_generator, DallEImageGenerator

@pytest.fixture
def image_generator() -> ImageGenerator:
    return create_image_generator('dall-e')

def test_create_image_generator_invalid_input():
    # If it throws an error, it works if does not throw an error, it does not work
    # Given
    model_name = 'invalid-model'
    
    # When & Then
    with pytest.raises(ValueError) as e:
        create_image_generator(model_name)
    
    assert str(e.value) == f'Invalid model name: {model_name}'

def test_create_image_generator_valid_input():
    # Given
    model_dall_e = 'dall-e'
    model_dall_e_3 = 'dall-e-3'
    model_stable_diffusion = 'stable-diffusion'

    
    # When
    dall_e_2 = create_image_generator(model_dall_e)
    dall_e_3 = create_image_generator(model_dall_e_3)
    stable_diffusion = create_image_generator(model_stable_diffusion)
    # Then
    assert isinstance(dall_e_2, DallEImageGenerator)
    assert isinstance(dall_e_3, DallEImageGenerator)
    assert isinstance(stable_diffusion, StableDiffusionImageGenerator)


def test_image_generation_with_empty_string_prompt(image_generator):
    # Arrange
    no_prompt = ""
    with pytest.raises(ValueError):
        # Act
        result = image_generator.generate_image(no_prompt, 1, 1)

def test_image_generation_with_non_string_prompt(image_generator):
    # Arrange
    non_string_prompt = 1
    with pytest.raises(TypeError):
        # Act
        result = image_generator.generate_image(non_string_prompt, 1, 1)

def test_image_generation_with_none_prompt(image_generator):
    # Arrange
    none_prompt = None
    with pytest.raises(TypeError):
        # Act
        result = image_generator.generate_image(none_prompt, 1, 1)


def test_image_generation_with_too_long_prompt(image_generator):
    # Arrange
    too_long_prompt = "A" * 3001
    with pytest.raises(ValueError):
        # Act
        result = image_generator.generate_image(too_long_prompt, 1, 1)

def test_image_generation_with_non_integer_width(image_generator):
    # Arrange
    non_integer_width = "1"
    valid_height = 1
    valid_prompt = "A picture of a cat"
    with pytest.raises(TypeError):
        # Act
        result = image_generator.generate_image(valid_prompt, non_integer_width, valid_height)

def test_image_generation_with_non_integer_height(image_generator):
    # Arrange
    valid_width = 1
    non_integer_height = "1"
    valid_prompt = "A picture of a cat"
    with pytest.raises(TypeError):
        # Act
        result = image_generator.generate_image(valid_prompt, valid_width, non_integer_height)
        # Assert

def test_image_generation_with_too_small_width(image_generator):
    # Arrange
    too_small_width = 0
    valid_height = 1
    valid_prompt = "A picture of a cat"
    with pytest.raises(ValueError):
        # Act
        result = image_generator.generate_image(valid_prompt, too_small_width, valid_height)
        # Assert

def test_image_generation_with_too_small_height(image_generator):
    # Arrange
    valid_width = 1
    too_small_height = 0
    valid_prompt = "A picture of a cat"
    with pytest.raises(ValueError):
        # Act
        result = image_generator.generate_image(valid_prompt, valid_width, too_small_height)
        # Assert

def test_image_generation_with_too_large_width(image_generator):
    # Arrange
    too_large_width = 1025
    valid_height = 1
    valid_prompt = "A picture of a cat"
    with pytest.raises(ValueError):
        # Act
        result = image_generator.generate_image(valid_prompt, too_large_width, valid_height)
        # Assert

def test_image_generation_with_too_large_height(image_generator):
    # Arrange
    valid_width = 1
    too_large_height = 1025
    valid_prompt = "A picture of a cat"
    with pytest.raises(ValueError):
        # Act
        result = image_generator.generate_image(valid_prompt, valid_width, too_large_height)
        # Assert

def test_image_generation_with_width_not_equal_to_height(image_generator):
    # Arrange
    width_not_equal_to_height = 512
    valid_prompt = "A picture of a cat"
    with pytest.raises(ValueError):
        # Act
        result = image_generator.generate_image(valid_prompt, width_not_equal_to_height, width_not_equal_to_height + 1)
        # Assert

def test_image_generation_with_invalid_width(image_generator):
    # Arrange
    invalid_width = 300
    valid_prompt = "A picture of a cat"
    with pytest.raises(ValueError):
        # Act
        result = image_generator.generate_image(valid_prompt, invalid_width, invalid_width)
        # Assert

def test_image_generation_with_invalid_height(image_generator):
    # Arrange
    invalid_height = 300
    valid_prompt = "A picture of a cat"
    with pytest.raises(ValueError):
        # Act
        result = image_generator.generate_image(valid_prompt, invalid_height, invalid_height)
        # Assert

@pytest.mark.apitest
def test_image_generation_with_valid_prompt(image_generator):
    # Arrange
    valid_size = 256
    valid_prompt = "A picture of a cat"
    # Act
    result = image_generator.generate_image(valid_prompt, valid_size, valid_size)
    # Assert
    assert result is not None


def test_create_image_generator_valid_input():
    # Given
    model_name = 'dall-e'
    
    # When
    image_generator = create_image_generator(model_name)
    
    # Then
    assert isinstance(image_generator, DallEImageGenerator)

def test_create_image_generator_invalid_input():
    # Given
    model_name = 'invalid-model'
    
    # When & Then
    with pytest.raises(ValueError) as e:
        create_image_generator(model_name)
    
    assert str(e.value) == f'Invalid model name: {model_name}'
