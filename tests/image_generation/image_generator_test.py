import pytest

from src.image_generation.image_generator import ImageGenerator





def test_image_generation_with_empty_prompt():
    # Arrange

    image_generator = ImageGenerator()
    no_prompt = ""
    pytest.raises(ValueError):
        # Act
        result = image_generator.generate_image(no_prompt)
        # Assert
    


    
