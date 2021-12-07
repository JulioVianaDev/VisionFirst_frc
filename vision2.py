import cv2
import numpy as np
#webcam index = 0 default
frame =cv2.imread("image.png")
lower_green = np.array([60,125,110])
upper_green = np.array([100,255,255])
frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
frame_inrange = cv2.inRange(frame_hsv,lower_green,upper_green)
cv2.imshow("Camera Stream", frame_inrange)
cv2.waitKey(0)