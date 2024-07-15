# DONE || 2024-07-05 || Bit Plane Slicing of an Image
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

image = rgbToGray(meroImage)

# ------------------------------------------------------------

# # Function to perform bit plane slicing
# # It takes the image and the bit plane to slice as input
# # It returns the sliced image
# # It isolates the bit plane by performing a bitwise AND operation with the image and 2^bit_plane
def bit_plane_slicing(image, bit_plane):
    return ((image & (1 << bit_plane)) >> bit_plane) * 255

# Slice all bit planes
sliced_images = [bit_plane_slicing(image, i) for i in range(8)]

# ------------------------------------------------------------

# Display the images
fig, axes = plt.subplots(2, 4, figsize=(12, 6))
axes[0, 0].imshow(image, cmap='gray')
axes[0, 0].set_title("Original Grayscale Image")
axes[0, 0].axis("off")

# Display the bit plane sliced images
for i in range(7):
    row, col = divmod(i + 1, 4)
    axes[row, col].imshow(sliced_images[i + 1], cmap='gray')
    axes[row, col].set_title(f"Bit Plane {i + 1} Image")
    axes[row, col].axis("off")

# Show the plot
plt.show()
