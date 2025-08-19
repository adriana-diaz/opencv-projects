import numpy as np
import cv2


def get_limits(color):

    c = np.uint8([color])
    hsv_color = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)[0][0]

    lower_limits = np.array([hsv_color[0] - 10, 100, 100])
    upper_limits = np.array([hsv_color[0] + 10, 255, 255])

    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit