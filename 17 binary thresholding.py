import cv2

# Read image in grayscale
image = cv2.imread("D:/open cv/aplle image.jpg", cv2.IMREAD_GRAYSCALE)

# Apply binary thresholding
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Display result
cv2.imshow('Binary Thresholding', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
