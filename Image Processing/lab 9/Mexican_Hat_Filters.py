# This is the Mexican Hat Filters implementation
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def mexican_hat_filter(image_path, sigma):
    image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    
    # Create Mexican Hat filter (Laplacian of Gaussian)
    ksize = int(6*sigma + 1)
    mexican_hat = cv.getDerivKernels(2, 0, ksize)
    filtered_image = cv.filter2D(image, -1, mexican_hat[0])
    
    return image, filtered_image

image_path = 'photos/bird.jpg'
sigma = 1

original_image, filtered_image = mexican_hat_filter(image_path, sigma)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(original_image, cmap='gray')
axes[0].set_title("Original Image")
axes[0].axis("off")
axes[1].imshow(filtered_image, cmap='gray')
axes[1].set_title("Mexican Hat Filtered Image")
axes[1].axis("off")
plt.show()
