# DONE || 2024-07-06 || Histogram of an Image
import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

meroImage = cv.imread('photos/bird.jpg', cv.IMREAD_GRAYSCALE)

row, col = meroImage.shape
print(meroImage.shape)
# shape of the image is (2448, 3264) meaning 2448 rows and 3264 columns.

# !--------------------Histogram implementation here-----------------
arr = np.zeros(256)
# It means we are creating an array of size 256, with all elements initialized to 0.

for i in range(row):
    for j in range(col):
        pixelValue = meroImage[i,j]
        arr[pixelValue] = arr[pixelValue] + 1
        
# pixelValue is the intensity value of the pixel at (i, j) position.
# arr[0] vaneko 0 intensity gareko kati ota xa image ma, 1 intensity gareko kati ota xa image ma vaneko
# arr[pixelValue] + 1 is done kinaki suruma 256 size ko array ma sabai element 0 gareko xa, so harek choti tyo intensity value vayeko pixel aaune bitikai we increment the value by 1. So, last ma thaha hos ki kati kati intensity value ko kati kati ota pixels xa vanera.
# -------------------------------
# Eg:
# arr[0] = 0
# arr[0] = arr[0] + 1
# arr[0] = 0 + 1
# arr[0] = 1   
        
print(arr)
# Yo bird wala image ma total 59 lakhs ota pixels xa, each pixel ko intensity value 0-255 ko range ma xa.
# arr[0] is 870, meaning there are 870 pixels with intensity value 0.
# arr[1] is 305, meaning there are 305 pixels with intensity value 1.


# -----------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Plot the grayscale image
axes[0].imshow(meroImage, cmap='gray')
axes[0].set_title("Grayscale Image")
axes[0].axis("off")

# Plot the grayscale histogram
axes[1].bar(range(256), arr , color='black')
axes[1].set_title("Grayscale Histogram")
axes[1].set_xlabel('Pixel Intensity')
axes[1].set_ylabel('Frequency')

plt.show()