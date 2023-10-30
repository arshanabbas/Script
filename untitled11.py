# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 10:43:46 2023

@author: arab
"""

import cv2

# Load the image
image = cv2.imread('F:/Arshan_Abbas/Fabian/Task2/Img/Welle_1_spur_1_0.png')  # Replace with the path to your image

if image is None:
    print("Image not found.")
    exit()

# Define the initial color
initial_color = image[0, 0]  # Get the color of the first pixel
initial_position = (0, 0)

# Get the height (number of rows) and width (number of columns) of the image
height, width, _ = image.shape

# Loop through each column (x-coordinate)
for x in range(width):
    # Loop through each row (y-coordinate)
    for y in range(height):
        # Get the current pixel's color
        current_color = image[y, x]
        
        # Check if the color has changed
        if not all(initial_color == current_color):
            print(f"Color change from {initial_color} to {current_color} at position (x={x}, y={y})")
            initial_color = current_color  # Update the initial color
            initial_position = (x, y)  # Update the initial position

# Don't forget to release the image when done
cv2.destroyAllWindows()
