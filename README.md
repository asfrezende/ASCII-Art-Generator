# **ASCII Art Generator: a script that converts image files in a directory into ASCII art in TXT and PNG formats.**

## **Features:**
- Converts image formats (PNG, JPEG and JPG) to ASCII art with colored output;
- Costumizable scaling and characters density for detailed or simplified outputs, that can be modified here:
  ```python
  scale = 0.4        # Controls the level of detail
  char_width = 8     # Character spacing in output image
  char_height = 18   # Character spacing in output image
  chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1] # Character set for brightness levels
  ```

## **Requirements and Installation:**
- Requirements:
  - Python 3.x;
  - Pillow Library (PIL fork).
- Installation:
  - Clone or download this reposity;
  - Install the dependency required:
    ```
    pip install Pillow
    ```

## **Usage:**
- Place the images you want to convert in the same directory as the script;
- Run the script;
- The script will generate two files:
  - A text file with the ASCII representation, `([original_file_name]_ascii.txt)`;
  - An image file with colored ASCII characters, `(ascii_ver_[original_file_name].png)`

## **How it works:**
- The script scans the directory for image files;
- For each image it, then:
  - Resizes the image based on the `scale` factor;
  - Converts the image to greyscale pixel-by-pixel;
  - Maps the brightness of each pixel to values from the `char` set;
  - Generates the output files.

## **Example:**
Input and output below:

![Album cover of Elliot Smith's album Either/Or: a man sitting wearing black clothes and a cap facing the camera with a orange/brown tint](https://github.com/asfrezende/ASCII-Art-Generator/blob/main/eitheror.png?raw=true) ![Album cover of Elliott Smith's album Either/Or coverted to colored ASCII characters](https://github.com/asfrezende/ASCII-Art-Generator/blob/main/ascii_ver_eitheror.png?raw=true)

### **Notes**
- I'm using the "lucon.ttf" font from Windows. If needed, you shall change the font path.
- This script was made based on the tutorial of the YouTuber Raphson, which you can find [here](https://www.youtube.com/@Raphson/videos).

Any feedback and suggestions are welcome!
