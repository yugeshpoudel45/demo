# Done || 2024-07-04 || Negative Image
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

def negate_image(image_path):
    gray_image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    
    # Negate the image
    if gray_image.dtype == np.uint8:
        neg_image = 255 - gray_image
    # This checks if the image's pixel values are of type uint8 (unsigned 8 bit integer), which means they are integers ranging from 0 to 255.
    # For images with pixel values from 0 to 255, subtracting each pixel value from 255 creates the negative image. For example, a pixel value of 0 (black) becomes 255 (white), and a pixel value of 255 (white) becomes 0 (black).
    # Negate gareko image feri back lyaunu xa vane, run this function once again by keeping new image intensity as input.
    
    else:
        gray_image = gray_image / gray_image.max()
        neg_image = 1 - gray_image
    # gray image.max gives the maximum pixel value in the image (i.e., 255 for uint8 images). This line normalizes the pixel values to be between 0 and 1.
    # If the image's pixel values are not in the range 0-255, this part normalizes the pixel values to be between 0 and 1 by dividing by the maximum pixel value. Then, it creates the negative by subtracting these normalized values from 1.
    
    return gray_image, neg_image

image_path = 'photos/bird.jpg'

gray_image, neg_image = negate_image(image_path)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(gray_image, cmap='gray')
axes[0].set_title("Original Image")
axes[0].axis("off")
axes[1].imshow(neg_image, cmap='gray')
axes[1].set_title("Negative Image")
axes[1].axis("off")
plt.show()
