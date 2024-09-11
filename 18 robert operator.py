import cv2
import numpy as np

# Read the image in grayscale
image = cv2.imread("D:/open cv/aplle image.jpg", cv2.IMREAD_GRAYSCALE)

# Define Roberts Cross kernels
kernel_x = np.array([[1, 0], [0, -1]], dtype=int)
kernel_y = np.array([[0, 1], [-1, 0]], dtype=int)

# Apply the Roberts operator using filter2D
roberts_x = cv2.filter2D(image, -1, kernel_x)
roberts_y = cv2.filter2D(image, -1, kernel_y)

# Combine the results
roberts_combined = np.sqrt(np.square(roberts_x) + np.square(roberts_y))
roberts_combined = np.uint8(roberts_combined)

# Display the results
cv2.imshow('Roberts X', roberts_x)
cv2.imshow('Roberts Y', roberts_y)
cv2.imshow('Roberts Combined', roberts_combined)

# Wait and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()

# Optionally save the results
cv2.imwrite('roberts_x.jpg', roberts_x)
cv2.imwrite('roberts_y.jpg', roberts_y)
cv2.imwrite('roberts_combined.jpg', roberts_combined)
