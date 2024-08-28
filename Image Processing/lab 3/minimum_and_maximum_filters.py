import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def max_min_filter(image_path):
    gray_image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    
    # Define a kernel
    kernel = np.ones((5, 5), np.uint8)
    
    # Apply Maximum Filter
    max_image = cv.dilate(gray_image, kernel)
    
    # Apply Minimum Filter
    min_image = cv.erode(gray_image, kernel)
    
    return gray_image, max_image, min_image

image_path = 'photos/bird.jpg'

gray_image, max_image, min_image = max_min_filter(image_path)

fig, axes = plt.subplots(1, 3, figsize=(18, 6))
axes[0].imshow(gray_image, cmap='gray')
axes[0].set_title("Original Image")
axes[0].axis("off")
axes[1].imshow(max_image, cmap='gray')
axes[1].set_title("Maximum Filtered Image")
axes[1].axis("off")
axes[2].imshow(min_image, cmap='gray')
axes[2].set_title("Minimum Filtered Image")
axes[2].axis("off")
plt.show()
