import cv2

# Read the image
image = cv2.imread("D:/open cv/aplle image.jpg")

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Get image dimensions
height, width = gray_image.shape

# Mirror lower half to upper half
gray_image[:height//2, :] = gray_image[height//2:, :]

# Save result
cv2.imwrite('output_image.jpg', gray_image)

# Display result
cv2.imshow('Mirrored Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
