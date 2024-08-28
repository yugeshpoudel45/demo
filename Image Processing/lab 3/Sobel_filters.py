# This is the Sobel filters implementation
import cv2 as cv
import matplotlib.pyplot as plt


def sobel_filter(image_path):
    gray_image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    
    # Compute X and Y Gradients using Sobel Filter
    sobelx = cv.Sobel(gray_image, cv.CV_64F, 1, 0, ksize=3)
    sobely = cv.Sobel(gray_image, cv.CV_64F, 0, 1, ksize=3)
    
    # Combine Gradients
    gradient_magnitude = cv.magnitude(sobelx, sobely)
    
    return gray_image, gradient_magnitude

image_path = 'photos/bird.jpg'

gray_image, gradient_magnitude = sobel_filter(image_path)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(gray_image, cmap='gray')
axes[0].set_title("Original Image")
axes[0].axis("off")
axes[1].imshow(gradient_magnitude, cmap='gray')
axes[1].set_title("Sobel Filtered Image")
axes[1].axis("off")
plt.show()
