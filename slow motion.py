import cv2

# Capture video from the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Define the slow-motion factor (e.g., 2 means half speed, 4 means quarter speed)
slow_motion_factor = 4

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame is read correctly, ret is True
    if not ret:
        print("Error: Can't receive frame (stream end?). Exiting...")
        break

    # Display the resulting frame
    cv2.imshow('Slow Motion Video', frame)

    # Introduce a delay between frames to create slow motion
    if cv2.waitKey(int(1000 / 30) * slow_motion_factor) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
