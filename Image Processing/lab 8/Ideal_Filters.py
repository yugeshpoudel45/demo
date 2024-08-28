# This is the Ideal Filters implementation
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def ideal_filter(image_path, cutoff, filter_type):
    gray_image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    
    # Fourier Transform
    f_transform = np.fft.fftshift(np.fft.fft2(gray_image))
    
    # Construct the Ideal Filter
    rows, cols = gray_image.shape
    crow, ccol = rows // 2 , cols // 2
    mask = np.zeros((rows, cols), np.float32)
    for i in range(rows):
        for j in range(cols):
            dist = np.sqrt((i-crow)**2 + (j-ccol)**2)
            if filter_type == 'lowpass' and dist <= cutoff:
                mask[i, j] = 1
            elif filter_type == 'highpass' and dist > cutoff:
                mask[i, j] = 1
    
    # Apply the Ideal Filter
    f_transform_filtered = f_transform * mask
    filtered_image = np.abs(np.fft.ifft2(np.fft.ifftshift(f_transform_filtered)))
    
    return gray_image, np.uint8(filtered_image)

image_path = 'photos/bird.jpg'

# Lowpass Filter with cutoff at 30
gray_image_low, lowpass_filtered_image = ideal_filter(image_path, 30, 'lowpass')

# Highpass Filter with cutoff at 30
gray_image_high, highpass_filtered_image = ideal_filter(image_path, 30, 'highpass')

fig, axes = plt.subplots(1, 3, figsize=(18, 6))
axes[0].imshow(gray_image_low, cmap='gray')
axes[0].set_title("Original Image")
axes[0].axis("off")
axes[1].imshow(lowpass_filtered_image, cmap='gray')
axes[1].set_title("Ideal Lowpass Filter")
axes[1].axis("off")
axes[2].imshow(highpass_filtered_image, cmap='gray')
axes[2].set_title("Ideal Highpass Filter")
axes[2].axis("off")
plt.show()
