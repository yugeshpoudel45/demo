import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def weighted_averaging(image_path):
    gray_image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    
    # Define Custom Kernel for Weighted Averaging
    kernel = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16
    
    # Apply Filter
    weighted_image = cv.filter2D(gray_image, -1, kernel)
    
    return gray_image, weighted_image

image_path = 'photos/bird.jpg'

gray_image, weighted_image = weighted_averaging(image_path)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(gray_image, cmap='gray')
axes[0].set_title("Original Image")
axes[0].axis("off")
axes[1].imshow(weighted_image, cmap='gray')
axes[1].set_title("Weighted Averaging Image")
axes[1].axis("off")
plt.show()
