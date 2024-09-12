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

# Initialize a contour around the shape (circle in this case)
s = np.linspace(0, 2 * np.pi, 400)
x = 100 + 50 * np.cos(s)  # Initial x-coordinates of the contour
y = 100 + 50 * np.sin(s)  # Initial y-coordinates of the contour
init_contour = np.array([x, y]).T

# Perform Active Contour (Snakes) algorithm
snake = active_contour(smoothed_image, init_contour, alpha=0.015, beta=10, gamma=0.001)

# Plot the results
fig, ax = plt.subplots(figsize=(7, 7))
ax.imshow(gray, cmap=plt.cm.gray)
ax.plot(init_contour[:, 0], init_contour[:, 1], '--r', lw=3, label='Initial Contour')
ax.plot(snake[:, 0], snake[:, 1], '-b', lw=3, label='Detected Contour')
ax.legend(loc='best')
plt.show()
