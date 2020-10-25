import cv2
import numpy as py
import firebase

cap = cv2.VideoCapture(0)
hue = [0, 255]
sat = [0, 255]
val = [0, 110]
min_area = 18000.0
min_perimeter = 0
min_width = 0
max_width = 1000
min_height = 0
max_height = 1000
solidity = [0, 100]
max_vertices = 18000
min_vertices = 0
min_ratio = 0
max_ratio = 1000
# max_left_point = 0
# max_right_point = 0
area = 0
total = 0

db = firebase.get_db()
fb = firebase.get_firebase()
fs = firebase.get_firestore()
while True:
    doccount = 0
    ret, raw = cap.read()
    imgorg = raw.copy()
    frame = cv2. cvtColor(imgorg, cv2.COLOR_BGR2HSV)
    frame = cv2.inRange(frame, (hue[0], sat[0], val[0]), (hue[1], sat[1], val[1]))
    ksize = int(6 * round(5) + 1)
    frame = cv2.GaussianBlur(frame, (ksize, ksize), round(5))
    frame = cv2.normalize(frame, frame, 0, 255, cv2.NORM_MINMAX)
    _, threshold = cv2.threshold(frame, 5, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(frame, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    input_contours = contours
    output = []
    for contour in input_contours:
        x, y, w, h = cv2.boundingRect(contour)
        if (w < min_width or w > max_width):
            continue
        if (h < min_height or h > max_height):
            continue
        area = cv2.contourArea(contour)
        if (area < min_area):
            continue
        if (cv2.arcLength(contour, True) < min_perimeter):
            continue
        hull = cv2.convexHull(contour)
        solid = 100 * area / cv2.contourArea(hull)
        if (solid < solidity[0] or solid > solidity[1]):
            continue
        if (len(contour) < min_vertices or len(contour) > max_vertices):
            continue
        ratio = (float)(w) / h
        if (ratio < min_ratio or ratio > max_ratio):
            continue
        output.append(contour)
    contournew = output

    contour = cv2.drawContours(imgorg, contournew, -1, (0, 0, 255), 3)

    # GETS THE MAXIMUM LENGTH CONTOUR
    max_contour = 0
    max_contour_index = 0
    for i in range(len(contournew)):
        if max_contour < len(contournew[i]):
            max_contour_index = i

    if(len(contournew) > 0):
        largest_contour = contournew[max_contour_index]
        area = cv2.contourArea(largest_contour)
        print(area)
    # for i in range(len(largest_contour)):
        # print(contour[i][0])
        # if (max_left_point < contour[i][0]):
        #     max_left_point = contour[i][0]


    #print(contour)
    docs = db.collection(u'Postures').stream()
    Postures_ref = db.collection(u'Postures')
    query = Postures_ref.order_by(
        u'Postures', direction=fs.Query.DESCENDING).limit(1).get()

    print("lastdoc")
    for lastdoc in query:
        print(lastdoc.to_dict())
        print(lastdoc.id)

    cv2.imshow("Frame", frame)
    cv2.imshow("Threshold", threshold)
    cv2.imshow("Contours", contour)
    # data = {
    #     u'area': area,
    #     u'average': average,
    #     u'time': fb.database.ServerValue.TIMESTAMP,
    #     u'total': total,
    #
    # }
    # db.collection(u'Posture').document(u'data').set(data)
    # total+=1

    if cv2.waitKey(1) == ord('q'):
        break