from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import os
import math

fnt = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)
chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1] # Character set for brightness levels
charArray = list(chars)
charLength = len(charArray)
interval = charLength/256

scale = 0.4        # Controls the level of detail
char_width = 8     # Character spacing in output image
char_height = 18   # Character spacing in output image


# This function gets all the image files on the current directory
def gets_image():
    image_files = []
    extensions = [".png", ".jpeg", ".jpg"]
    directory = os.getcwd()
    
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[1].lower()
            if file_ext in extensions:
                image_files.append(file_path)

    return image_files


# Given an input value (greyscale color), returns the correspondent character with the same value
def get_char(input_value):
    return charArray[math.floor(input_value*interval)]


# Converts all files in the current directory into ASCII, returning an image and a TXT file
def ascii_conversor():
    image_files = gets_image()

    for image_path in image_files:
        # Sets the names for the output files
        file_name = os.path.basename(image_path)
        base_name = os.path.splitext(file_name)[0]
        output_file_txt = base_name + "_ascii.txt"
        output_file_txt = open(output_file_txt, "w")
        output_image_name = "ascii_ver_" + base_name + ".png"

        # Opens image and resizes it
        image = Image.open(image_path)
        im_width, im_height = image.size
        image = image.resize((int(scale*im_width), int(scale*im_height*(char_width/char_height))), Image.NEAREST)
        im_width, im_height = image.size
        pix = image.load()

        output_file_img = Image.new('RGB', (char_width*im_width, char_height*im_height), color = (0, 0, 0)) # [color] here is the background color, I'm using pure black
        output_img = ImageDraw.Draw(output_file_img)

        # Converts image into a TXT file and a new image with the colored characters
        for i in range(im_height):
            for j in range(im_width):
                r, g, b = pix[j, i]
                h = int(r/3+g/3+b/3)
                pix[j, i] = (h, h, h)
                output_file_txt.write(get_char(h))
                output_img.text((j*char_width, i*char_height), get_char(h), font = fnt, fill = (r, g, b))
            output_file_txt.write('\n')

        output_file_img.save(output_image_name)


def main():
    ascii_conversor()

if __name__ == "__main__":
    main()