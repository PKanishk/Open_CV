import cv2

# Capture video from the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Define the fast-motion factor (e.g., 2 means double speed, 4 means quadruple speed)
fast_motion_factor = 1

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame is read correctly, ret is True
    if not ret:
        print("Error: Can't receive frame (stream end?). Exiting...")
        break

    # Display the resulting frame
    cv2.imshow('Fast Motion Video', frame)

    # Reduce the delay between frames to create fast motion
    if cv2.waitKey(int(1000 / 30) // fast_motion_factor) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
