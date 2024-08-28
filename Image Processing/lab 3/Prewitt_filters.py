# This is the Prewitt filters implementation
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def prewitt_filter(image_path):
    gray_image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    
    # Define Prewitt Kernels
    prewitt_x = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]], dtype=int)
    prewitt_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]], dtype=int)
    
    # Apply Prewitt Filter
    grad_x = cv.filter2D(gray_image, -1, prewitt_x)
    grad_y = cv.filter2D(gray_image, -1, prewitt_y)
    
    # Combine Gradients
    gradient = cv.addWeighted(grad_x, 0.5, grad_y, 0.5, 0)
    
    return gray_image, gradient

image_path = 'photos/bird.jpg'

gray_image, gradient = prewitt_filter(image_path)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(gray_image, cmap='gray')
axes[0].set_title("Original Image")
axes[0].axis("off")
axes[1].imshow(gradient, cmap='gray')
axes[1].set_title("Prewitt Filtered Image")
axes[1].axis("off")
plt.show()
