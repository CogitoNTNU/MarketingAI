from PIL import Image, ImageFont, ImageDraw
import os

base_path = os.path.dirname(os.path.abspath("__main__"))

def chose_font_size(image_file_name: str, text, font_path, max_width, max_height):
    font_size = 1
    font = ImageFont.truetype(base_path + "/arial.ttf", font_size)
    image_file_path = base_path + "/data/raw_images/" + image_file_name + ".png"
    print(image_file_path)

    image = Image.open(image_file_path)
    draw = ImageDraw.Draw(image)

    while font.getsize(text)[0] < max_width and font.getsize(text)[1] < max_height:
        font_size += 1
        font = ImageFont.truetype(font_path, font_size)
        draw = ImageDraw.Draw(image)

    return font_size - 1