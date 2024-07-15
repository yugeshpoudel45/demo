# DONE || 2024-07-06 || Intensity Level Slicing of an Image
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

# ------------------------------------------------------------

lower = 120  # Lower threshold
upper = 140  # Upper threshold

# In intensity level slicing, pixels with intensity values between the lower and upper thresholds are assigned a new intensity value i.e. (slice value).
# And, other remaining pixels are left unchanged. This is useful for highlighting specific intensity values in an image.
# Remaining pixels lai 0 assign garyo vane black color ma aaucha. yeslai binary intensity level slicing pani vancha.


def intensity_level_slicing(image, lower, upper, slice_value=255):
    sliced_image = np.where((image >= lower) & (image <= upper), slice_value, image)
    # -----------Remaining pixels lai 0 rakheko yesma----------------
    # sliced_image = np.where((image >= lower) & (image <= upper), slice_value, 0)
    return sliced_image.astype(np.uint8)
# Yesma np.where() function le image ko pixels lai check garxa ani condition satisfy bhaye chai slice_value assign garxa varible ma, otherwise image ko pixel value lai as it is rakhxa.

sliced_image = intensity_level_slicing(gray, lower, upper)

# ------------------------------------------------------------

fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].imshow(gray, cmap='gray')
axes[0].set_title("Original Image")
axes[0].axis("off")

axes[1].imshow(sliced_image, cmap='gray')
axes[1].set_title(f"Intensity Level Sliced\n({lower}-{upper})")
axes[1].axis("off")

plt.show()
