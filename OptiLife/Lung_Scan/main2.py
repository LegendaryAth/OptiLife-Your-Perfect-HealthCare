import os
import cvzone
from cvzone.ClassificationModule import Classifier
import cv2

cap = cv2.VideoCapture(1)
classifier = Classifier('keras_model.h5', 'labels.txt')
font = cv2.FONT_HERSHEY_SIMPLEX
org = (750, 350)
fontScale = 1
color = (255, 0, 0)
thickness = 2
while True:
    _, img = cap.read()
    imgResize = cv2.resize(img, (454, 340))
    bg = cv2.imread('bgg2.png')
    prediction = classifier.getPrediction(img, draw=False)
    classID = prediction[1]
    print(classID)
    if classID != 3:
        if classID == 0:
            print(0)
            bg = cv2.putText(bg, 'Normal', org, font,fontScale, color, thickness, cv2.LINE_AA)
        elif classID == 1:
            print(1)
            bg = cv2.putText(bg, 'Viral Pneumonia', org, font,fontScale, color, thickness, cv2.LINE_AA)
        elif classID == 2:
            print(2)
            bg = cv2.putText(bg, 'Covid-19', org, font,fontScale, color, thickness, cv2.LINE_AA)

    bg[148:148 + 340, 159:159 + 454] = imgResize
    # cv2.imshow("Image", img)
    cv2.imshow("Lung Cancer Detection", bg)
    cv2.waitKey(1)
