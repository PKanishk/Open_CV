import cv2
import numpy as np

# Read image in grayscale
image = cv2.imread("D:/open cv/aplle image.jpg", cv2.IMREAD_GRAYSCALE)

# Define kernel
kernel = np.ones((5, 5), np.uint8)

# Apply black hat (closed image - image)
black_hat_image = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)

# Display result
cv2.imshow('Black Hat Image', black_hat_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
