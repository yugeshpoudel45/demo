# This is the Midpoint Filters implementation
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def midpoint_filter(image_path, kernel_size):
    gray_image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    
    # Pad the image to handle borders
    padded_image = cv.copyMakeBorder(gray_image, kernel_size//2, kernel_size//2, kernel_size//2, kernel_size//2, cv.BORDER_REFLECT)
    
    # Initialize output image
    filtered_image = np.zeros_like(gray_image, dtype=np.float64)
    
    # Apply Midpoint Filter
    for i in range(gray_image.shape[0]):
        for j in range(gray_image.shape[1]):
            neighborhood = padded_image[i:i+kernel_size, j:j+kernel_size].astype(np.float64)
            filtered_image[i, j] = 0.5 * (np.max(neighborhood) + np.min(neighborhood))
    
    filtered_image = np.uint8(filtered_image)
    
    return gray_image, filtered_image

image_path = 'photos/bird.jpg'

gray_image, filtered_image = midpoint_filter(image_path, 3)  # 3x3 kernel

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(gray_image, cmap='gray')
axes[0].set_title("Original Image")
axes[0].axis("off")
axes[1].imshow(filtered_image, cmap='gray')
axes[1].set_title("Midpoint Filter")
axes[1].axis("off")
plt.show()
