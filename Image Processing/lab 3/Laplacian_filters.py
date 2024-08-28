import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def laplacian_filter(image_path):
    gray_image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    
    # Apply Laplacian Filter
    laplacian_image = cv.Laplacian(gray_image, cv.CV_64F)
    
    # Normalize the Laplacian image to the range 0-255
    abs_laplacian = np.absolute(laplacian_image)
    laplacian_normalized = cv.normalize(abs_laplacian, None, 0, 255, cv.NORM_MINMAX)
    laplacian_normalized = np.uint8(laplacian_normalized)
    
    return gray_image, laplacian_normalized

image_path = 'photos/bird.jpg'

gray_image, laplacian_image = laplacian_filter(image_path)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(gray_image, cmap='gray')
axes[0].set_title("Original Image")
axes[0].axis("off")
axes[1].imshow(laplacian_image, cmap='gray')
axes[1].set_title("Laplacian Filtered Image")
axes[1].axis("off")
plt.show()
