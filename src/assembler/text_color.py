from PIL import Image, ImageStat

def chose_color(path:str)->tuple:
    image = Image.open(path)

    # Convert the image to grayscale
    grayscale_image = image.convert('L')

    # Calculate the average grayscale value
    stat = ImageStat.Stat(grayscale_image)
    average_brightness = stat.mean[0]

    # Determine the text color based on background brightness
    threshold = 128  # Adjust this threshold as needed
    text_color = (0, 0, 0)  # Black text
    if average_brightness < threshold:
        text_color = (255, 255, 255)  # White text
        
    return text_color


