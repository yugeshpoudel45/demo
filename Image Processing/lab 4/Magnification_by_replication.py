import cv2 as cv
import matplotlib.pyplot as plt


def magnification_by_replication(image_path, scale_factor):
    gray_image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    
    # Magnify the image by replication
    height, width = gray_image.shape
    new_height, new_width = int(height * scale_factor), int(width * scale_factor)
    magnified_image = cv.resize(gray_image, (new_width, new_height), interpolation=cv.INTER_NEAREST)
    
    return gray_image, magnified_image

image_path = 'photos/bird.jpg'
scale_factor = 2

gray_image, magnified_image = magnification_by_replication(image_path, scale_factor)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(gray_image, cmap='gray')
axes[0].set_title("Original Image")
axes[0].axis("off")
axes[1].imshow(magnified_image, cmap='gray')
axes[1].set_title("Magnified Image by Replication")
axes[1].axis("off")
plt.show()
