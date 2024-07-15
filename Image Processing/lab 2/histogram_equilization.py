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

gray_img = rgbToGray(meroImage)

# ------------------------------------------------------------

def histogram_equalization(img):
    # Calculate histogram
    arr = np.zeros(256)
    for pixelNum in img.flatten():
        arr[pixelNum] = arr[pixelNum] + 1
    # img.flatten() le 2D image lai 1D ma convert garxa. 
    # Eg: [[1,2,3],[4,5,6]] lai [1,2,3,4,5,6] ma convert garxa
    # yesma 1,2,3,4,5,6 vaneko pixel intensity value ho
    
    # Then, Histogram ma calculate gare jastai,
    # We calculate the frequency of each pixel intensity value in the image and keep track of it in the array arr.
    # Tara yesma 1D array vayeko le, we can directly calculate the frequency of each pixel intensity value by iterating over the array.
    
    # ----------------------Histogram calculated upto here here------------------------------
    
    # ---------------------------------------------------------------------------------------
    
    # ---------------------Histogram Equalization starts from here---------------------------
    # Calculate cumulative distribution function (CDF)
    cdf = np.zeros(256)
    cdf[0] = arr[0]
    for i in range(1, 256):
        cdf[i] = cdf[i - 1] + arr[i]

    # Normalize CDF
    cdf_min = cdf.min()
    cdf_max = cdf.max()
    cdf = (cdf - cdf_min) / (cdf_max - cdf_min) * 255
    cdf = cdf.astype(np.uint8)

    # Map the original gray levels to equalized gray levels
    equalized_img = np.zeros_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            equalized_img[i, j] = cdf[img[i, j]]

    return equalized_img

# --------------------------------------------------------------------

equalized_img = histogram_equalization(gray_img)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].imshow(gray_img, cmap='gray')
axes[0].set_title("Original Grayscale img")
axes[0].axis("off")

axes[1].imshow(equalized_img, cmap='gray')
axes[1].set_title("Histogram Equalized img")
axes[1].axis("off")

plt.show()
