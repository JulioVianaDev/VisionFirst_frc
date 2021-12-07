import cv2
#webcam index =0 by default
cap = cv2.VideoCapture(0)
while True:
 #_is a throwway variable
 _,frame = cap.read()
 cv2.imshow("CameraStream",frame)
 cv2.waitKey(1)
 