# This is the Arithmetic Mean Filters implementation
import cv2 as cv
import matplotlib.pyplot as plt


def arithmetic_mean_filter(image_path, kernel_size):
    gray_image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    
    # Apply Arithmetic Mean Filter (Smoothing)
    smoothed_image = cv.blur(gray_image, (kernel_size, kernel_size))
    
    return gray_image, smoothed_image

image_path = 'photos/bird.jpg'

gray_image, smoothed_image = arithmetic_mean_filter(image_path, 5)  # 5x5 kernel

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(gray_image, cmap='gray')
axes[0].set_title("Original Image")
axes[0].axis("off")
axes[1].imshow(smoothed_image, cmap='gray')
axes[1].set_title("Arithmetic Mean Filter")
axes[1].axis("off")
plt.show()
