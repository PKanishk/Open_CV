import cv2
import numpy as np

# Load the video
cap = cv2.VideoCapture(0)  # Use 0 for the default webcam

# Take the first frame and convert it to grayscale
ret, first_frame = cap.read()
prev_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)

# Create a mask for drawing the optical flow (using HSV color space)
mask = np.zeros_like(first_frame)
mask[..., 1] = 255

while cap.isOpened():
    # Read the next frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the current frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate dense optical flow using Farneback's method
    flow = cv2.calcOpticalFlowFarneback(prev_gray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)

    # Compute the magnitude and angle of the flow vectors
    magnitude, angle = cv2.cartToPolar(flow[..., 0], flow[..., 1])

    # Set the hue according to the angle of flow
    mask[..., 0] = angle * 180 / np.pi / 2

    # Set the value according to the magnitude (normalized to [0, 255])
    mask[..., 2] = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)

    # Convert the mask to a BGR image for visualization
    rgb_flow = cv2.cvtColor(mask, cv2.COLOR_HSV2BGR)

    # Display the optical flow
    cv2.imshow("Optical Flow", rgb_flow)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Update the previous frame to the current one
    prev_gray = gray

# Release the video capture and close windows
cap.release()
cv2.destroyAllWindows()
