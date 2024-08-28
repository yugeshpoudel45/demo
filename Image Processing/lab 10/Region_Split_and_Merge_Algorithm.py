# This is the Region Split and Merge Algorithm implementation
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def split_and_merge(image, threshold):
    height, width = image.shape
    segmented_image = np.zeros_like(image)

    def split(x, y, w, h):
        region = image[y:y+h, x:x+w]
        if np.std(region) < threshold:
            segmented_image[y:y+h, x:x+w] = np.mean(region)
        else:
            hw, hh = w//2, h//2
            if w > 1 and h > 1:
                split(x, y, hw, hh)
                split(x + hw, y, hw, hh)
                split(x, y + hh, hw, hh)
                split(x + hw, y + hh, hw, hh)

    split(0, 0, width, height)
    return segmented_image

def region_split_and_merge(image_path, threshold):
    image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    segmented_image = split_and_merge(image, threshold)
    return image, segmented_image

image_path = 'photos/bird.jpg'
threshold = 15

original_image, segmented_image = region_split_and_merge(image_path, threshold)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(original_image, cmap='gray')
axes[0].set_title("Original Image")
axes[0].axis("off")
axes[1].imshow(segmented_image, cmap='gray')
axes[1].set_title("Region Split and Merged Image")
axes[1].axis("off")
plt.show()
