# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 13:19:41 2023

@author: arab
"""
'''Calculate the Euclidean distance between two RGB colors'''

import cv2

# Load the image
image = cv2.imread('F:/Arshan_Abbas/Fabian/Task2/Img/Welle_1_spur_1_0.png')  # Replace with the path to your image

if image is None:
    print("Image not found.")
    exit()

# Get the height (number of rows) and width (number of columns) of the image
height, width, _ = image.shape

# Loop through each column (x-coordinate)
for x in range(width):
    # Loop through each row (y-coordinate)
    for y in range(height):
        # Get the pixel value at the current (x, y) position
        pixel_value = image[y, x]
        
        # You can perform operations on the pixel_value here
        # For example, you can access pixel_value[0] for the blue channel, pixel_value[1] for green, and pixel_value[2] for red.
        
        # Print the pixel coordinates and the pixel value
        print(f"Pixel at (x={x}, y={y}): {pixel_value}")

# Don't forget to release the image when done
cv2.destroyAllWindows()
