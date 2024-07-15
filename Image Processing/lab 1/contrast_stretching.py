# DONE || 2024-07-05 || Contrast Stretching of an Image
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

# Contrast stretching function
# Yesma image vaneko each pixel ko intensity value ho
def contrast_stretch(image):
    min_val = np.min(image)
    max_val = np.max(image)
    stretched_image = (image - min_val) * (255 / (max_val - min_val))
    # Yo 100% mileko xa,Eg: yesma 50 to 100 ko intensity vaneko image line, yesle tesko intensity value lai 0-255 ko range ma lagxa
    return stretched_image.astype(np.uint8)
# streched_image.astype(np.uint8) le image ko pixel intensity value lai 0-255 ko range ma lauxa

# np.min(image): Finds the minimum pixel intensity value in the image.
# np.max(image): Finds the maximum pixel intensity value in the image.
# (image - min_val): Subtracts the minimum pixel intensity value from each pixel in the image.
# Scaling factor = (255 / (max_val - min_val))
# Scaling is done by multiplying by the scaling factor.
# (255 / (max_val - min_val)): Scales the pixel intensity values to the range [0, 255].




# Apply contrast stretching
stretched_image = contrast_stretch(image)

# Display the images
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].imshow(image, cmap='gray')
axes[0].set_title("Grayscale Image")
axes[0].axis("off")

axes[1].imshow(stretched_image, cmap='gray')
axes[1].set_title("Contrast-Stretched Image")
axes[1].axis("off")

plt.show()
