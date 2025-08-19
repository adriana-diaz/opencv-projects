import cv2
from util import get_limits

pink = [203, 192, 255]  # Color rosado en formato BGR
cap = cv2.VideoCapture(0)  # Open the default camera
while True:
    ret, frame = cap.read()  # Read a frame from the camera

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convert the frame to HSV color space

    lower_limits, upper_limits = get_limits(color=pink)  # Get the lower and upper limits for the specified color

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    cv2.imshow('Camera Feed', mask)  # Display the frame in a window

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit pressing 'q'
        break
cap.release()  # Release the camera
cv2.destroyAllWindows()  # Close all OpenCV windows

# This code captures video from the default camera and displays it in a window.

