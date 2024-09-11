import cv2

# Read image
image = cv2.imread("D:/open cv/aplle image.jpg")

# Define ROI (Region of Interest)
roi = image[50:150, 100:200]

# Paste ROI onto another region
image[0:100, 0:100] = roi

# Save and display result
cv2.imwrite('image_with_roi.jpg', image)
cv2.imshow('Image with ROI', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
