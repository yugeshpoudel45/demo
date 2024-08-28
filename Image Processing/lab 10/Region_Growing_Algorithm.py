import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def region_growing(image_path, seed_point, threshold):
    image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    seed_value = image[seed_point]
    segmented_image = np.zeros_like(image)
    
    # Initialize stack with seed point
    stack = [seed_point]
    while stack:
        x, y = stack.pop()
        if segmented_image[x, y] == 0:
            segmented_image[x, y] = 255
            # Check neighbors
            for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= nx < image.shape[0] and 0 <= ny < image.shape[1]:
                    if segmented_image[nx, ny] == 0 and abs(int(image[nx, ny]) - seed_value) <= threshold:
                        stack.append((nx, ny))
    
    return image, segmented_image

image_path = 'photos/bird.jpg'
seed_point = (100, 100)  # Adjust this point to be within the image
threshold = 10

original_image, segmented_image = region_growing(image_path, seed_point, threshold)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(original_image, cmap='gray')
axes[0].set_title("Original Image")
axes[0].axis("off")
axes[1].imshow(segmented_image, cmap='gray')
axes[1].set_title("Region Grown Image")
axes[1].axis("off")
plt.show()
