import os
import cvzone
from cvzone.ClassificationModule import Classifier
import cv2

cap = cv2.VideoCapture(1)
classifier = Classifier('keras_model(3).h5', 'labels(3).txt')
font = cv2.FONT_HERSHEY_SIMPLEX
org = (750, 350)
fontScale = 1
color = (255, 0, 0)
thickness = 2
while True:
    _, img = cap.read()
    imgResize = cv2.resize(img, (454, 340))
    bg = cv2.imread('bgg4.png')
    prediction = classifier.getPrediction(img, draw=False)
    classID = prediction[1]
    print(classID)
    if classID != 0:
        if classID == 1:
            bg = cv2.putText(bg, 'Healthy', org, font,fontScale, color, thickness, cv2.LINE_AA)
        elif classID == 2:
            bg = cv2.putText(bg, 'Unhealthy', org, font,fontScale, color, thickness, cv2.LINE_AA)

    bg[148:148 + 340, 159:159 + 454] = imgResize
    cv2.imshow("Lung Cancer Detection", bg)
    cv2.waitKey(1)
