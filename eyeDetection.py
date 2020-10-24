import cv2
import numpy as np


cap = cv2.VideoCapture(0)


eyes_cascade = cv2.CascadeClassifier(r"/Users/grantshim/OneDrive - The University of Texas at Austin/Hackathon/straightBody/cascades/haarcascade_eye.xml")

while True:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #changes frame to gray
    frame = cv2.GaussianBlur(frame, (7,7), 0)

    eyes = eyes_cascade.detectMultiScale(frame, 2.3, 4)

    for(x,y,w,h) in eyes:
        cv2.rectangle(frame,(x,y),(x+w, y+h), (0,255,0))
        cv2.putText(frame, 'Eye',(x,y),cv2.FONT_HERSHEY_COMPLEX, 0.5, (250,250,250),1)


    _, threshold = cv2.threshold(frame, 5, 255, cv2.THRESH_BINARY_INV)
    #the frame needs to be adjusted to find the eye in the camera

    cv2.imshow("Threshold", threshold)
    cv2.imshow("Frame",frame)

    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()