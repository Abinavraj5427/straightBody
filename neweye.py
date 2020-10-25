import cv2
import numpy as np
import  dlib
from math import hypot

cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(r"./shape_predictor_68_face_landmarks.dat")

def midpoint(p1, p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)

font = cv2.FONT_HERSHEY_COMPLEX
counter = 0
time_counter = 0
def get_blinking_ratio(eye_point, facial_landmarks):
    left_point = (facial_landmarks.part(eye_point[0]).x, facial_landmarks.part(eye_point[0]).y)
    right_point = (facial_landmarks.part(eye_point[3]).x, facial_landmarks.part(eye_point[3]).y)
    center_top = midpoint(facial_landmarks.part(eye_point[1]), facial_landmarks.part(eye_point[2]))
    center_bottom = midpoint(facial_landmarks.part(eye_point[5]), facial_landmarks.part(eye_point[4]))

    #hor_line = cv2.line(frame, left_point, right_point, (0,255,0),2)
    #ver_line = cv2.line(frame, center_top, center_bottom, (0,255,0), 2)

    hor_line_length = hypot((left_point[0]-right_point[0]), (left_point[1]- right_point[1]))
    ver_line_length = hypot((center_top[0]- center_bottom[0]), (center_top[1] - center_bottom[1]))
        #print(str(ver_line_length))
        #print(ver_line_length, hor_line_length)
    ratio = (hor_line_length/ver_line_length)
    return ratio

def get_gaze_ratio(eye_points, facial_landmarks):
    left_eye_region = np.array([(facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y),
                                (facial_landmarks.part(eye_points[1]).x, facial_landmarks.part(eye_points[1]).y),
                                (facial_landmarks.part(eye_points[2]).x, facial_landmarks.part(eye_points[2]).y),
                                (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y),
                                (facial_landmarks.part(eye_points[4]).x, facial_landmarks.part(eye_points[4]).y),
                                (facial_landmarks.part(eye_points[5]).x, facial_landmarks.part(eye_points[5]).y)], np.int32)
        #print(left_eye_region)
        #cv2.polylines(frame, [left_eye_region], True, (0,0,255),2)
        
    height, width, _ = frame.shape
    mask = np.zeros((height,width), np.uint8)
    cv2.polylines(mask, [left_eye_region], True, 255,2)
    cv2.fillPoly(mask, [left_eye_region], 255)
    left_eye = cv2.bitwise_and(gray, gray, mask=mask)

    min_x = np.min(left_eye_region[:, 0])
    max_x = np.max(left_eye_region[:, 0])
    min_y = np.min(left_eye_region[:, 1])
    max_y = np.max(left_eye_region[:, 1])

    gray_eye = left_eye[min_y:max_y, min_x: max_x]
        #gray_eye = cv2.cvtColor(eye, cv2.COLOR_BGR2GRAY)
    _, threshold_eye = cv2.threshold(gray_eye, 70, 255, cv2.THRESH_BINARY)
    height, width = threshold_eye.shape
    left_side_threshold = threshold_eye[0: height, 0: int(width/2)]
    left_side_white = cv2.countNonZero(left_side_threshold)

    right_side_threshold = threshold_eye[0: height, int(width/2):width]
    right_side_white = cv2.countNonZero(right_side_threshold)   
    if right_side_white == 0:
        return 0
    else:
        gaze_ratio = left_side_white/right_side_white
        return gaze_ratio
while True:
    time_counter +=1
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    for face in faces:
        x, y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()
        landmarks = predictor(gray, face)

        # BLINKING REGION OF CODE
        # cv2.rectangle(frame, (x,y),(x1,y1),(0,255,0),2)
        right_eye_ratio = get_blinking_ratio([36,37,38,39,40,41], landmarks)
        left_eye_ratio = get_blinking_ratio([42,43,44,45,46,47], landmarks)
        
        if left_eye_ratio > 5.4 and right_eye_ratio > 5.7:
            cv2.putText(frame, "Blinking", (50,150), font, 4, (255,0,0))

        #GAZE DECTECTION CODE
        
        #if right_side_white != 0:
            #gaze_ratio = left_side_white/right_side_white
        #if (right_side_white < 54 and right_side_white >= 5) and (left_side_white < 87 and left_side_white >= 35):
            #counter+=1
       # cv2.putText(frame, str(left_side_white), (50,100), font, 2, (0,0,255),3)
        #cv2.putText(frame, str(right_side_white), (50,150), font, 2, (0,0,255),3)
        


       

        #cv2.imshow("Eye", eye)
        gaze_ratio_left_eye= get_gaze_ratio([36,37,38,39,40,41], landmarks)
        gaze_ratio_right_eye = get_gaze_ratio([42,43,44,45,46,47], landmarks)
        gaze_ratio = (gaze_ratio_right_eye+gaze_ratio_left_eye)/2
        #cv2.putText(frame, str(gaze_ratio_left_eye), (50,100), font, 2, (0,0,255),3)
        cv2.putText(frame, str(gaze_ratio), (50,150), font, 2, (0,0,255),3)
        if gaze_ratio >= .57 and gaze_ratio <= 2.9:
            counter+=1
        #x =  landmarks.part(36).x
        #y = landmarks.part(36).y
        #cv2.circle(frame, (x,y), 3, (0,0,255),2)
        
    

    cv2.imshow("Frame",frame)
    print(counter, time_counter)
    key = cv2.waitKey(1)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    #if key == 27:
        #break

cap.release()
cv2.destroyAllWindows()



#left_point = (landmarks.part(36).x, landmarks.part(36).y)
        #right_point = (landmarks.part(39).x, landmarks.part(39).y)
        #center_top = midpoint(landmarks.part(37), landmarks.part(38))
        #center_bottom = midpoint(landmarks.part(41), landmarks.part(40))

        #hor_line = cv2.line(frame, left_point, right_point, (0,255,0),2)
        #ver_line = cv2.line(frame, center_top, center_bottom, (0,255,0), 2)

       # hor_line_length = hypot((left_point[0]-right_point[0]), (left_point[1]- right_point[1]))
        #ver_line_length = hypot((center_top[0]- center_bottom[0]), (center_top[1] - center_bottom[1]))
        #print(str(ver_line_length))
        #print(ver_line_length, hor_line_length)
        #ratio = (hor_line_length/ver_line_length)