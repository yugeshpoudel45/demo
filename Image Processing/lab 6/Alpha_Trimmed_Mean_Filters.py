# This is the Alpha Trimmed Mean Filters implementation
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def alpha_trimmed_mean_filter(image_path, kernel_size, alpha):
    gray_image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    
    # Pad the image to handle borders
    padded_image = cv.copyMakeBorder(gray_image, kernel_size//2, kernel_size//2, kernel_size//2, kernel_size//2, cv.BORDER_REFLECT)
    
    # Initialize output image
    filtered_image = np.zeros_like(gray_image, dtype=np.float64)
    
    # Apply Alpha Trimmed Mean Filter
    for i in range(gray_image.shape[0]):
        for j in range(gray_image.shape[1]):
            neighborhood = padded_image[i:i+kernel_size, j:j+kernel_size].astype(np.float64).flatten()
            sorted_neighborhood = np.sort(neighborhood)
            trimmed_neighborhood = sorted_neighborhood[alpha:-alpha]
            filtered_image[i, j] = np.mean(trimmed_neighborhood)
    
    filtered_image = np.uint8(filtered_image)
    
    return gray_image, filtered_image

image_path = 'photos/bird.jpg'

gray_image, filtered_image = alpha_trimmed_mean_filter(image_path, 3, 1)  # 3x3 kernel, alpha=1

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(gray_image, cmap='gray')
axes[0].set_title("Original Image")
axes[0].axis("off")
axes[1].imshow(filtered_image, cmap='gray')
axes[1].set_title("Alpha Trimmed Mean Filter")
axes[1].axis("off")
plt.show()
