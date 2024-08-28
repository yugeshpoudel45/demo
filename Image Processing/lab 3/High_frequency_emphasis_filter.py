# This is the High frequency emphasis filter implementation
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def high_frequency_emphasis(image_path):
    gray_image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    
    # Define High-Pass Kernel
    kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    
    # Apply High-Pass Filter
    high_pass_image = cv.filter2D(gray_image, -1, kernel)
    
    # Emphasize High Frequencies
    emphasized_image = cv.addWeighted(high_pass_image, 1.5, gray_image, 0.5, 0)
    
    return gray_image, emphasized_image

image_path = 'photos/bird.jpg'

gray_image, emphasized_image = high_frequency_emphasis(image_path)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(gray_image, cmap='gray')
axes[0].set_title("Original Image")
axes[0].axis("off")
axes[1].imshow(emphasized_image, cmap='gray')
axes[1].set_title("High Frequency Emphasized Image")
axes[1].axis("off")
plt.show()
