# Done || 2024-07-04 || Adaptive Thresholding of an Image
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image_path = "photos/bird.jpg"
meroImage = cv.imread(image_path)

def rgbToGray(image):
    R = np.array(image[:, :, 0])
    G = np.array(image[:, :, 1])
    B = np.array(image[:, :, 2])
    avg = (R * 0.299 + G * 0.587 + B * 0.114)
    return avg.astype(np.uint8)

gray = rgbToGray(meroImage)

def logarithmic_transform(image):
    c = 255 / np.log(1 + np.max(image))  
    log_image = c * (np.log(1 + image))
    log_image = np.array(log_image, dtype=np.uint8)  
    return log_image

# np.max(image) finds the maximum pixel value in the image.
# np.log(1 + np.max(image)) computes the logarithm of one plus this maximum value.
# 255 / np.log(1 + np.max(image)) scales the logarithmic values to the range 0 to 255.
# This ensures the transformed pixel values fit within the valid range for an 8-bit image.

# np.log(1 + image) applies the logarithmic transformation to each pixel in the image.
# c * scales these values to ensure they are within the 0-255 range.

log_transformed_image = logarithmic_transform(gray)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].imshow(gray, cmap='gray')
axes[0].set_title("Original Image")
axes[0].axis("off")

axes[1].imshow(log_transformed_image, cmap='gray')
axes[1].set_title("Logarithmic Image")
axes[1].axis("off")

plt.show()
