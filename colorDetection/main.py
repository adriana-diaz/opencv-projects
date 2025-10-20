import cv2
from PIL import Image
from util import get_limits

yellow = [0, 255, 255]  # Color amarillo en formato BGR
cap = cv2.VideoCapture(0)  # Open the default camera
while True:
    ret, frame = cap.read()  # Read a frame from the camera

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convert the frame to HSV color space

    lower_limits, upper_limits = get_limits(color=yellow)  # Get the lower and upper limits for the specified color

    mask = cv2.inRange(hsvImage, lower_limits, upper_limits)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    print(bbox)

    if bbox:
        x1, y1, x2, y2 = bbox
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Draw a rectangle around the detected color region

    cv2.imshow('Camera Feed', frame)  # Display the frame in a window

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit pressing 'q'
        break
cap.release()  # Release the camera
cv2.destroyAllWindows()  # Close all OpenCV windows

# This code captures video from the default camera and displays it in a window.

