import cv2

# Read image in grayscale
image = cv2.imread("D:/open cv/aplle image.jpg", cv2.IMREAD_GRAYSCALE)

# Apply Otsu thresholding
_, otsu_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Display result
cv2.imshow('Otsu Thresholded Image', otsu_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
