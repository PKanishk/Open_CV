import cv2

# Read base image
image = cv2.imread("D:/open cv/aplle image.jpg")

# Read watermark image
watermark = cv2.imread('watermark.png', cv2.IMREAD_UNCHANGED)

# Resize watermark to base image size
watermark = cv2.resize(watermark, (image.shape[1], image.shape[0]))

# Add watermark with transparency
output = cv2.addWeighted(image, 0.7, watermark, 0.3, 0)

# Save result
cv2.imwrite('watermarked_image.jpg', output)

# Display result
cv2.imshow('Watermarked Image', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
