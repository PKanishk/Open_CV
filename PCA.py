import cv2
import numpy as np

# Load the image in grayscale
image = cv2.imread("D:/open cv/cc.jpg", 0)

# Reshape the image into a 2D array (flattened form)
image_flattened = image.reshape(-1, image.shape[1])

# Compute mean and eigenvectors using PCA
mean, eigenvectors = cv2.PCACompute(image_flattened, mean=None)

# Specify the number of principal components to retain
n_components = 20

# Project the image data onto the reduced number of components
reduced_data = cv2.PCAProject(image_flattened, mean, eigenvectors[:n_components])

# Back-project the reduced data to reconstruct the image
reconstructed_image = cv2.PCABackProject(reduced_data, mean, eigenvectors[:n_components])

# Reshape the reconstructed image back to its original shape
reconstructed_image = reconstructed_image.reshape(image.shape)

# Compute explained variance ratio (i.e., the amount of information retained)
total_variance = np.sum(np.var(image_flattened, axis=0))
reduced_variance = np.sum(np.var(reduced_data, axis=0))
explained_variance_ratio = reduced_variance / total_variance

# Print the explained variance ratio
print(f"Explained variance ratio (information retained): {explained_variance_ratio * 100:.2f}%")

# Display the original and reconstructed images
cv2.imshow('Original Image', image)
cv2.imshow('Reconstructed Image', reconstructed_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
