import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import color, io
from skimage.filters import gaussian
from skimage.segmentation import active_contour

# Load the image
image = io.imread("D:/open cv/aplle image.jpg")

# Convert to grayscale
gray = color.rgb2gray(image)

# Apply Gaussian filter to smooth the image and reduce noise
smoothed_image = gaussian(gray, sigma=3)

# Initialize a contour as a square
square_x = np.array([50, 150, 150, 50, 50])  # x-coordinates of the square's corners
square_y = np.array([50, 50, 150, 150, 50])  # y-coordinates of the square's corners
init_contour = np.array([square_x, square_y]).T

# Perform Active Contour (Snakes) algorithm
snake = active_contour(smoothed_image, init_contour, alpha=0.015, beta=10, gamma=0.001)

# Plot the results
fig, ax = plt.subplots(figsize=(7, 7))
ax.imshow(gray, cmap=plt.cm.gray)
ax.plot(init_contour[:, 0], init_contour[:, 1], '--r', lw=3, label='Initial Square Contour')
ax.plot(snake[:, 0], snake[:, 1], '-b', lw=3, label='Detected Contour')
ax.legend(loc='best')
plt.show()
