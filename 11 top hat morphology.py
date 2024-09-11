import cv2
import numpy as np

# Read image in grayscale
image = cv2.imread("D:/open cv/aplle image.jpg", cv2.IMREAD_GRAYSCALE)

# Define kernel
kernel = np.ones((5, 5), np.uint8)

# Apply top hat (image - opened image)
top_hat_image = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)

# Display result
cv2.imshow('Top Hat Image', top_hat_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
