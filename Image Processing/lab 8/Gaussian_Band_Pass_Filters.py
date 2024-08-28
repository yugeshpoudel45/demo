import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def gaussian_band_pass_filter(image_path, low_cutoff, high_cutoff):
    gray_image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    
    # Fourier Transform
    f_transform = np.fft.fftshift(np.fft.fft2(gray_image))
    
    # Construct the Gaussian Band Pass Filter
    rows, cols = gray_image.shape
    crow, ccol = rows // 2, cols // 2
    mask = np.zeros((rows, cols), np.float32)
    
    for i in range(rows):
        for j in range(cols):
            dist = np.sqrt((i - crow)**2 + (j - ccol)**2)
            if low_cutoff < dist < high_cutoff:
                mask[i, j] = 1
            else:
                mask[i, j] = 0
    
    # Apply the Gaussian Band Pass Filter
    f_transform_filtered = f_transform * mask
    filtered_image = np.abs(np.fft.ifft2(np.fft.ifftshift(f_transform_filtered)))
    
    return gray_image, np.uint8(filtered_image)

image_path = 'photos/bird.jpg'
low_cutoff = 10
high_cutoff = 50

gray_image, filtered_image = gaussian_band_pass_filter(image_path, low_cutoff, high_cutoff)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(gray_image, cmap='gray')
axes[0].set_title("Original Image")
axes[0].axis("off")
axes[1].imshow(filtered_image, cmap='gray')
axes[1].set_title("Gaussian Band Pass Filtered Image")
axes[1].axis("off")
plt.show()
