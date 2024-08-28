import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def roberts_cross_filter(image_path):
    gray_image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    
    # Define Roberts Cross Kernels
    roberts_x = np.array([[1, 0], [0, -1]], dtype=int)
    roberts_y = np.array([[0, 1], [-1, 0]], dtype=int)
    
    # Apply Roberts Cross Filter
    grad_x = cv.filter2D(gray_image, cv.CV_32F, roberts_x)  # Convert to floating-point type
    grad_y = cv.filter2D(gray_image, cv.CV_32F, roberts_y)  # Convert to floating-point type
    
    # Combine Gradients
    gradient_magnitude = cv.magnitude(grad_x, grad_y)
    
    return gray_image, gradient_magnitude

image_path = 'photos/bird.jpg'

gray_image, gradient_magnitude = roberts_cross_filter(image_path)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(gray_image, cmap='gray')
axes[0].set_title("Original Image")
axes[0].axis("off")
axes[1].imshow(gradient_magnitude, cmap='gray')
axes[1].set_title("Roberts Cross Filtered Image")
axes[1].axis("off")
plt.show()
