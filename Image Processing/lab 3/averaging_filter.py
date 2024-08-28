import cv2 as cv
import matplotlib.pyplot as plt


def averaging_filter(image_path):
    gray_image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    
    # Apply Averaging Filter
    averaged_image = cv.blur(gray_image, (5, 5))
    
    return gray_image, averaged_image

image_path = 'photos/bird.jpg'

gray_image, averaged_image = averaging_filter(image_path)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(gray_image, cmap='gray')
axes[0].set_title("Original Image")
axes[0].axis("off")
axes[1].imshow(averaged_image, cmap='gray')
axes[1].set_title("Averaging Filtered Image")
axes[1].axis("off")
plt.show()
