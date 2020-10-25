import cv2
import firebase_admin


from firebase_admin import credentials
from firebase_admin import firestore

import numpy as py
# import firebase_setup


db = firestore.client()
# cap = cv2.VideoCapture(0)
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

total = 0


def shoulderProcess(raw):
    area = 0
# while True:
    doccount = 0
    # ret, raw = cap.read()
    imgorg = raw.copy()
    frame = cv2. cvtColor(imgorg, cv2.COLOR_BGR2HSV)
    frame = cv2.inRange(frame, (hue[0], sat[0], val[0]), (hue[1], sat[1], val[1]))
    ksize = int(6 * round(5) + 1)
    frame = cv2.GaussianBlur(frame, (ksize, ksize), round(5))
    frame = cv2.normalize(frame, frame, 0, 255, cv2.NORM_MINMAX)
    _, threshold = cv2.threshold(frame, 10, 255, cv2.THRESH_BINARY_INV)

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
            max_contour = len(contournew[i])
            max_contour_index = i

    if(len(contournew) > 0):
        largest_contour = contournew[max_contour_index]
        area = cv2.contourArea(largest_contour)
        print(area)

    Postures_ref = db.collection('Postures')
    query = Postures_ref.order_by('time', direction=firestore.Query.DESCENDING).limit(1)
    results = query.stream()
    print("Query")
    print(query)
    print(results)
    last_doc = list(results)[-1].to_dict()
    print(last_doc)
    doc_ref = db.collection('Postures').document(str(last_doc['total']))
    doc_ref.set({
        'area': area,
        'average': (last_doc['total']*last_doc['average']+area)/(last_doc['total']+1),
        'time': firestore.SERVER_TIMESTAMP,
        'total': last_doc['total']+1,
        'change': (area*100)/((last_doc['total']*last_doc['average']+area)/(last_doc['total']+1)),

     })



    #cv2.imshow("Frame", frame)
    #cv2.imshow("Threshold", threshold)
    #cv2.imshow("Contours", contour)
    # data = {
    #     u'area': area,
    #     u'average': average,
    #     u'time': fb.database.ServerValue.TIMESTAMP,
    #     u'total': total,
    #
    # }
    # db.collection(u'Posture').document(u'data').set(data)
    # total+=1

    # if cv2.waitKey(1) == ord('q'):
    #     break
    return contour