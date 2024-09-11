import cv2
import numpy as np

# Read image in grayscale
image = cv2.imread("D:/open cv/aplle image.jpg", cv2.IMREAD_GRAYSCALE)

# Define Prewitt kernels
kernel_x = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
kernel_y = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])

# Apply Prewitt filter
prewitt_x = cv2.filter2D(image, -1, kernel_x)
prewitt_y = cv2.filter2D(image, -1, kernel_y)

# Combine both directions
prewitt_combined = np.hypot(prewitt_x, prewitt_y)

# Display result
cv2.imshow('Prewitt Edge Detection', prewitt_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
