# This is the Hough Transform implementation
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def hough_transform_lines(image_path):
    image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    
    # Detect edges using Canny
    edges = cv.Canny(image, 50, 150)
    
    # Apply Hough Line Transform
    lines = cv.HoughLines(edges, 1, np.pi / 180, 200)
    line_image = np.copy(image)
    
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 2)
    
    return edges, line_image

image_path = 'photos/bird.jpg'

edges, line_image = hough_transform_lines(image_path)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(edges, cmap='gray')
axes[0].set_title("Detected Edges")
axes[0].axis("off")
axes[1].imshow(line_image, cmap='gray')
axes[1].set_title("Hough Transform Lines")
axes[1].axis("off")
plt.show()
