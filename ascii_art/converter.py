from PIL import Image
import numpy as np

class ImageToAscii:
    def __init__(self, asci_chars=None):
        self.asci_chars = asci_chars or '@%#*+=-:. '

    def resize_image(self, image, new_width=100):
        width, height = image.size
        aspect_ratio = height/width * 0.5
        new_height = int(aspect_ratio * new_width)
        new_image = image.resize((new_width, new_height))
        return new_image
    
    def grayify(self, image):
        return image.convert('L')
    
    def pixels_to_ascii(self, image):
        pixels = np.array(image)
        ascii_chars = np.array(list(self.ascii_chars))
        scaled_pixels = (pixels / 255) * (len(ascii_chars) - 1)
        ascii_image = ascii_chars[scaled_pixels.astype(int)]
        return "\n".join("".join(row) for row in ascii_image)
    
    def convert(self, image_path, output_width=100):
        image = Image.open(image_path)
        resized_image = self.resize_image(image, new_width=output_width)
        grayscale_image = self.image_to_grayscale(resized_image)
        return self.map_pixels_to_ascii(grayscale_image)
    

    
