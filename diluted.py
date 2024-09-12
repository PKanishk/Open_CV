import cv2
import numpy as np
image = cv2.imread("D:/open cv/download.jpeg", cv2.IMREAD_GRAYSCALE)
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
kernel = np.ones((5, 5), np.uint8)
dilated_image = cv2.dilate(binary_image, kernel, iterations=1)
cv2.imshow('Original Image', binary_image)
cv2.imshow('Dilated Image', dilated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
