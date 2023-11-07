from PIL import Image, ImageFont, ImageDraw

def chose_font_size(image, text, font_path, max_width, max_height):
    font_size = 1
    font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(image)

    while font.getsize(text)[0] < max_width and font.getsize(text)[1] < max_height:
        font_size += 1
        font = ImageFont.truetype(font_path, font_size)
        draw = ImageDraw.Draw(image)

    return font_size - 1