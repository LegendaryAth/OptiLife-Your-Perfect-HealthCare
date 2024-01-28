import os
import cvzone
from cvzone.ClassificationModule import Classifier
import cv2

cap = cv2.VideoCapture(1)
classifier = Classifier('keras_model(1).h5', 'labels(1).txt')
font = cv2.FONT_HERSHEY_SIMPLEX
org = (750, 350)
fontScale = 1
color = (255, 0, 0)
thickness = 2
while True:
    _, img = cap.read()
    imgResize = cv2.resize(img, (454, 340))
    bg = cv2.imread('bgg3.png')
    prediction = classifier.getPrediction(img)
    classID = prediction[1]
    print(classID)
    if classID != 0:
        if classID == 1:
            bg = cv2.putText(bg, 'No Tumor', org, font,

                             fontScale, color, thickness, cv2.LINE_AA)
        elif classID == 2:
            bg = cv2.putText(bg, 'Pituitary', org, font,
                             fontScale, color, thickness, cv2.LINE_AA)
        elif classID == 3:
            bg = cv2.putText(bg, 'Meningioma', org, font,
                             fontScale, color, thickness, cv2.LINE_AA)
        elif classID == 4:
            bg = cv2.putText(bg, 'Glioma', org, font,
                             fontScale, color, thickness, cv2.LINE_AA)
    bg[148:148 + 340, 159:159 + 454] = imgResize
    # cv2.imshow("Image", img)
    cv2.imshow("Brain Tumor Detection", bg)
    cv2.waitKey(1)
