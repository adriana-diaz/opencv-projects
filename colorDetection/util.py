import numpy as np
import cv2


def get_limits(color):

    color_array = np.uint8([[color]])
    hsv_color = cv2.cvtColor(color_array, cv2.COLOR_BGR2HSV)[0][0]

    lower_h = max(int(hsv_color[0]) - 10, 0)
    upper_h = min(int(hsv_color[0]) + 10, 179)

    lower_limit = np.array([lower_h, 100, 100], dtype=np.uint8)
    upper_limit = np.array([upper_h, 255, 255], dtype=np.uint8)

    return lower_limit, upper_limit