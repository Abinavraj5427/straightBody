import cv2
import numpy as py


cap = cv2.VideoCapture(0)
hue = [0,180]
sat = [0, 255]
val = [0, 117]

while True:
    ret, frame = cap.read()
    frame = cv2. cvtColor(frame, cv2.COLOR_BGR2HSV)
    frame = cv2.inRange(frame, (hue[0], sat[0], val[0]), (hue[1], sat[1], val[1]))
    #_, threshold = cv2.threshold(frame, , 255, cv2.THRESH_BINARY_INV)



    cv2.imshow("Frame", frame)
    #cv2.imshow("Threshold", threshold)

    if cv2.waitKey(1) == ord('q'):
        break