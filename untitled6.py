# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 10:27:01 2023

@author: arab
Identify pixel colour and position
"""

from PIL import Image

def get_pixel_color_and_position(image_path, x, y):
    # Open the image
    img = Image.open(image_path)
    
    # Get the pixel color at the specified position (x, y)
    pixel_color = img.getpixel((x, y))
    
    # Return the pixel color and position
    return pixel_color, (x, y)

# Example usage
image_path = "path_to_your_image.png"
x_position = 100
y_position = 200

pixel_color, pixel_position = get_pixel_color_and_position(image_path, x_position, y_position)
print(f"Pixel color at position {pixel_position}: {pixel_color}")