import cv2
import numpy as np

# Load the image
img = cv2.imread("D:/open cv/aplle image.jpg")

# Check if the image is loaded correctly
if img is None:
    print("Error: Image not found or failed to load.")
else:
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Define the sharpening kernel
    kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    
    # Apply the sharpening filter
    sharpened = cv2.filter2D(gray, -1, kernel)
    
    # Display the original and sharpened images
    cv2.imshow('Original', gray)
    cv2.imshow('Sharpened', sharpened)
    
    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
