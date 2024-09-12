import cv2
import numpy as np
image = cv2.imread("D:/open cv/aplle image.jpg", 0) 
seed_point = (100, 100) 
threshold = 10 

height, width = image.shape
segmented_image = np.zeros_like(image)
visited = np.zeros_like(image, dtype=bool)
region = [seed_point]
segmented_image[seed_point] = 255
visited[seed_point] = True
neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
while region:
    current_pixel = region.pop(0)
    current_intensity = image[current_pixel]
    for n in neighbors:
        new_pixel = (current_pixel[0] + n[0], current_pixel[1] + n[1])
        if 0 <= new_pixel[0] < height and 0 <= new_pixel[1] < width:
            if not visited[new_pixel]:
                neighbor_intensity = image[new_pixel]
                if abs(int(current_intensity) - int(neighbor_intensity)) <= threshold:
                    segmented_image[new_pixel] = 255
                    region.append(new_pixel)
                    visited[new_pixel] = True
cv2.imshow('Original Image', image)
cv2.imshow('Region-Growing Segmented Image', segmented_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
