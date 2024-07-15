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

grayImage = rgbToGray(meroImage)

# ---------------Dilation of binary image----------------
def dilate(image, kernel):
    """
    Perform dilation on a binary image using a given kernel.
    :param image: Binary image (numpy array).
    :param kernel: Structuring element (numpy array).
    :return: Dilated binary image.
    """
    kernel_center = (kernel.shape[0] // 2, kernel.shape[1] // 2)
    padded_image = np.pad(image, pad_width=kernel_center, mode='constant', constant_values=0)
    dilated_image = np.zeros_like(image)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if np.any(padded_image[i:i + kernel.shape[0], j:j + kernel.shape[1]] & kernel):
                dilated_image[i, j] = 1

    return dilated_image

# ---------------Dilation of grayscale image----------------
# def dilate(image, kernel):
#     """
#     Perform dilation on a grayscale image using a given kernel.
#     :param image: Grayscale image (numpy array).
#     :param kernel: Structuring element (numpy array).
#     :return: Dilated grayscale image.
#     """
#     kernel_center = (kernel.shape[0] // 2, kernel.shape[1] // 2)
#     padded_image = np.pad(image, pad_width=kernel_center, mode='constant', constant_values=0)
#     dilated_image = np.zeros_like(image)

#     for i in range(image.shape[0]):
#         for j in range(image.shape[1]):
#             dilated_image[i, j] = np.max(padded_image[i:i + kernel.shape[0], j:j + kernel.shape[1]] * kernel)

#     return dilated_image

# ---------------Erosion of binary image----------------
def erode(image, kernel):
    """
    Perform erosion on a binary image using a given kernel.
    :param image: Binary image (numpy array).
    :param kernel: Structuring element (numpy array).
    :return: Eroded binary image.
    """
    kernel_center = (kernel.shape[0] // 2, kernel.shape[1] // 2)
    padded_image = np.pad(image, pad_width=kernel_center, mode='constant', constant_values=1)
    eroded_image = np.zeros_like(image)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if np.all(padded_image[i:i + kernel.shape[0], j:j + kernel.shape[1]] & kernel):
                eroded_image[i, j] = 1

    return eroded_image

# ---------------Erosion of grayscale image----------------
# def erode(image, kernel):  # New function for grayscale erosion
#     """
#     Perform erosion on a grayscale image using a given kernel.
#     :param image: Grayscale image (numpy array).
#     :param kernel: Structuring element (numpy array).
#     :return: Eroded grayscale image.
#     """
#     kernel_center = (kernel.shape[0] // 2, kernel.shape[1] // 2)
#     padded_image = np.pad(image, pad_width=kernel_center, mode='constant', constant_values=255)
#     eroded_image = np.zeros_like(image)

#     for i in range(image.shape[0]):
#         for j in range(image.shape[1]):
#             eroded_image[i, j] = np.min(padded_image[i:i + kernel.shape[0], j:j + kernel.shape[1]] * kernel)

#     return eroded_image


# Threshold the image to get a binary image
_, binary_image = cv.threshold(grayImage, 127, 255, cv.THRESH_BINARY)
binary_image = binary_image // 255  # Convert to binary (0 or 1)

# Define the structuring element
kernel = np.ones((3, 3), np.uint8)

# Perform dilation
dilated_image = dilate(binary_image, kernel)

# Perform erosion
eroded_image = erode(binary_image, kernel)

# --------------------Plot the results----------------------------------
fig, axes = plt.subplots(2, 2, figsize=(12, 6))
axes[0,0].imshow(grayImage, cmap='gray')
axes[0,0].set_title('GrayScale Image')
axes[0,0].axis('off')

axes[0,1].imshow(binary_image, cmap='gray')
axes[0,1].set_title('Binary Image')
axes[0,1].axis('off')

axes[1,0].imshow(dilated_image, cmap='gray')
axes[1,0].set_title('Dilated Image')
axes[1,0].axis('off')

axes[1,1].imshow(eroded_image, cmap='gray')
axes[1,1].set_title('Eroded Image')
axes[1,1].axis('off')

plt.show()
