from typing import Tuple
from PIL import Image, ImageDraw, ImageFont


SAVE_PATH  = "data/assembled_images/"
IMAGE_PATH = "data/raw_images/"
FONT_PATH  = "data/fonts/"

IMAGE_SUFFIX = ".png"

def assemble_image(image_name: str, text: str, font_name: str, font_size: int, text_color: Tuple[int, int, int], text_position: Tuple[int, int], show: bool = False) -> Image:
    """
    Assemble an image with custom text.

    Args:
        image_name (str): The name of the image to be loaded.
        text (str): The text to be added to the image.
        font_name (str): The name of the font to be used.
        font_size (int): The size of the font.
        text_color (tuple): The three integers representing the hex color of the text, e.g. (255, 255, 255) for white.
        text_position (tuple): The relative position of the text on the image, e.g. (50, 50) for 50 pixels from the top and 50 pixels from the left.'
        show (bool): Whether to show the image or not on screen of caller.
    Returns:
        Image: The assembled image with corresponding text.
    """
    # Load an image
    image = Image.open(IMAGE_PATH + image_name + IMAGE_SUFFIX)

    # Prepare a drawing context
    draw = ImageDraw.Draw(image)

    # Load your custom font
    try:
        font = ImageFont.truetype(FONT_PATH + font_name, size=font_size)
    except Exception as e:
        print("The font file is not accessible.")
        font = ImageFont.load_default()

    # Add text to the image
    draw.text(text_position, text, font=font, fill=text_color)

    # Save and display the image
    image.save(SAVE_PATH + image_name + IMAGE_SUFFIX)
    if show:
        image.show()
    return Image

if __name__ == "__main__":
    # assemble_image("img.png", "Hello World!", "arial.ttf", 50, (255, 255, 255), (50, 50))
    assemble_image("img", "Hello PropagandaAI!", "arial.ttf", 50, (255, 0, 0), (30, 50))