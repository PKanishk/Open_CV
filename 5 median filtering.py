import numpy as np
import cv2

# Create dataset
data = np.array([3, 5, 8, 12, 7, 10, 15, 20, 18, 22, 25, 28, 30], dtype=np.uint8)

# Reshape data to 1x13 (image format)
data_image = np.expand_dims(data, axis=0)

# Apply Median filter
filtered_data = cv2.medianBlur(data_image, 3)

print("Original Data: ", data)
print("Filtered Data: ", filtered_data.flatten())
