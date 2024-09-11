import cv2

# Read image
image = cv2.imread("D:/open cv/aplle image.jpg")

# Apply Gaussian Blur
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Display result
cv2.imshow('Gaussian Blur', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
