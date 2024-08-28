import cv2 as cv
import matplotlib.pyplot as plt


def gaussian_blur(image_path):
    gray_image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    
    # Apply Gaussian Blur
    blurred_image = cv.GaussianBlur(gray_image, (5, 5), 0)
    # This line means that the kernel size is 5x5 and the standard deviation is 0
    
    return gray_image, blurred_image

image_path = 'photos/bird.jpg'

gray_image, blurred_image = gaussian_blur(image_path)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(gray_image, cmap='gray')
axes[0].set_title("Original Image")
axes[0].axis("off")
axes[1].imshow(blurred_image, cmap='gray')
axes[1].set_title("Gaussian Blurred Image")
axes[1].axis("off")
plt.show()
