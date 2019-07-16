import numpy as np
import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture("video2.mp4")

def region_of_interest(image):
    polygons = np.array([[(315, 500),(820, 500),(650, 375),(530, 375)]])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image
    
while(True):
    ret, image = cap.read()
    lane_image = np.copy(image)

    gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)

    cropped_image = region_of_interest(canny)
    cv2.imshow("result", cropped_image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
