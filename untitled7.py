# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 10:30:25 2023

@author: arab
Read the image and identify particular pixel colour and position
"""

from PIL import Image

def identify_pixel_color_and_position(image_path, target_color):
    # Open the image
    img = Image.open(image_path)
    
    # Get image dimensions
    width, height = img.size
    
    # Iterate through each pixel
    for x in range(width):
        for y in range(height):
            # Get the pixel color at the current position (x, y)
            pixel_color = img.getpixel((x, y))
            
            # Compare the pixel color with the target color
            if pixel_color == target_color:
                return (x, y)  # Return the position if the color matches
    
    return None  # Return None if the color is not found

# Example usage
image_path = "path_to_your_image.png"
target_color = (255, 0, 0)  # Red color, replace with the desired color in RGB format

pixel_position = identify_pixel_color_and_position(image_path, target_color)

if pixel_position:
    print(f"Pixel color {target_color} found at position {pixel_position}")
else:
    print(f"Pixel color {target_color} not found in the image")
