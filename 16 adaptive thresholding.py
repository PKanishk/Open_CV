import cv2

# Read image in grayscale
image = cv2.imread("D:/open cv/aplle image.jpg", cv2.IMREAD_GRAYSCALE)

# Apply adaptive thresholding
adaptive_thresh_image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Display result
cv2.imshow('Adaptive Thresholding', adaptive_thresh_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
