import cv2
import numpy as np

# Function to detect the shape of the contour
def detect_shape(c):
    # Approximate the contour to reduce the number of points
    shape = "unidentified"
    peri = cv2.arcLength(c, True)  # Calculate the contour perimeter
    approx = cv2.approxPolyDP(c, 0.04 * peri, True)  # Approximate the contour
    
    # If the shape has 3 vertices, it is a triangle (not relevant here but included)
    if len(approx) == 3:
        shape = "triangle"
    # If the shape has 4 vertices, it could be a square or rectangle
    elif len(approx) == 4:
        (x, y, w, h) = cv2.boundingRect(approx)
        aspect_ratio = w / float(h)
        # A square will have an aspect ratio close to 1
        if 0.95 <= aspect_ratio <= 1.05:
            shape = "square"
        else:
            shape = "rectangle"
    # If the shape has more than 4 vertices, it is a circle (or close to it)
    elif len(approx) > 4:
        shape = "circle"
    
    return shape

# Load the image
image = cv2.imread("D:/open cv/cc.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur to reduce noise and improve contour detection
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply edge detection (Canny) to detect edges
edges = cv2.Canny(blurred, 50, 150)

# Find contours from the edges
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Loop over each contour and detect the shape
for c in contours:
    # Get the moments of the contour to calculate the center
    M = cv2.moments(c)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        cX, cY = 0, 0

    # Detect the shape of the contour
    shape = detect_shape(c)

    # Draw the contour and the name of the shape on the image
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    cv2.putText(image, shape, (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

# Display the output image with shapes identified
cv2.imshow('Detected Shapes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
