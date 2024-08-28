# This is the High boost filter implementation
import cv2 as cv
import matplotlib.pyplot as plt


def high_boost_filter(image_path):
    gray_image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    
    # Apply Gaussian Blur
    blurred_image = cv.GaussianBlur(gray_image, (5, 5), 0)
    
    # Create High Boost Image
    high_boost_image = cv.addWeighted(gray_image, 1.5, blurred_image, -0.5, 0)
    
    return gray_image, high_boost_image

image_path = 'photos/bird.jpg'

gray_image, high_boost_image = high_boost_filter(image_path)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(gray_image, cmap='gray')
axes[0].set_title("Original Image")
axes[0].axis("off")
axes[1].imshow(high_boost_image, cmap='gray')
axes[1].set_title("High Boost Filtered Image")
axes[1].axis("off")
plt.show()
