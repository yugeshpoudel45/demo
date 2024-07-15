# Done || 2024-07-04 || Thresholding of an Image
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image_path = "photos/bird.jpg"
meroImage = cv.imread(image_path)

def rgbToGray(image):
    R = np.array(image[:, :, 0])
    # image[:, :, 0] vaneko image ko row haru, column haru, 0th index ko value i.e. Red color
    G = np.array(image[:, :, 1])
    B = np.array(image[:, :, 2])
    avg = (R * 0.299 + G * 0.587 + B * 0.114)
    return avg.astype(np.uint8)

gray = rgbToGray(meroImage)

# This function applies thresholding to an image
# Yesle image lai black and white banauxa, no anything in between
def apply_threshold(image, threshold=128):
    threshold_image = np.where(image > threshold, 255, 0)
    return threshold_image.astype(np.uint8)
# In thresholding, we convert the image into a binary image. The input image is a grayscale image, and the output image is a binary image. The output image has pixel values of only 0 and 255. The pixel value 0 indicates black, and the pixel value 255 indicates white.

thresholded_image = apply_threshold(gray)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].imshow(gray, cmap='gray')
axes[0].set_title("Original Image")
axes[0].axis("off")

axes[1].imshow(thresholded_image, cmap='gray')
axes[1].set_title("Threshold Image")
axes[1].axis("off")

plt.show()
# This function applies adaptive thresholding to an image