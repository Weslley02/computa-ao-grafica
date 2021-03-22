from PIL import Image
import os

INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"

def in_path(filename):
    return os.path.join(INPUT_FOLDER, filename)

def bandeirafranca(height):
    width = 3height//2
    BLUE = (0, 85, 164)
    WHITE = (255, 255, 255)
    RED = (239, 65, 53)
    image = Image.new("RGB", (width,height), WHITE)

    offset = width//3
    for x in range(offset):
        for y in range(height):
            image.putpixel((x, y), BLUE)
            image.putpixel((x + 2offset, y), RED)
    return image

if name == "main":
    bandeira = bandeirafranca(700)
    bandeira.show()