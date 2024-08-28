import cv2 as cv
import matplotlib.pyplot as plt


def median_filter(image_path):
    gray_image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    
    # Apply Median Filter
    median_image = cv.medianBlur(gray_image, 5)
    
    return gray_image, median_image

image_path = 'photos/bird.jpg'

gray_image, median_image = median_filter(image_path)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(gray_image, cmap='gray')
axes[0].set_title("Original Image")
axes[0].axis("off")
axes[1].imshow(median_image, cmap='gray')
axes[1].set_title("Median Filtered Image")
axes[1].axis("off")
plt.show()
