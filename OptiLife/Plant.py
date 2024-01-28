import PyQt5
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QMovie
from OptiLife_Plant_UI import Ui_MainWindow
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from cvzone.ClassificationModule import Classifier
import cv2

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()
startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask1)
        self.ui.pushButton_2.clicked.connect(self.startTask2)
        self.ui.pushButton_3.clicked.connect(self.startTask3)
        self.ui.pushButton_4.clicked.connect(self.startTask4)
        self.ui.pushButton_4.clicked.connect(self.startTask4)
        self.ui.pushButton_5.clicked.connect(self.startTask5)


    def startTask1(self):
        import os
        import cvzone
        from cvzone.ClassificationModule import Classifier
        import cv2

        cap = cv2.VideoCapture(1)
        classifier = Classifier('Apple/keras_model(3).h5', 'Apple/labels(3).txt')
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (750, 350)
        fontScale = 1
        color = (255, 0, 0)
        thickness = 2
        while True:
            _, img = cap.read()
            imgResize = cv2.resize(img, (454, 340))
            bg = cv2.imread('Apple/bgg4.png')
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
    def startTask2(self):
        import os
        import cvzone
        from cvzone.ClassificationModule import Classifier
        import cv2

        cap = cv2.VideoCapture(1)
        classifier = Classifier('Cherry/keras_model.h5', 'Cherry/labels.txt')
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (750, 350)
        fontScale = 1
        color = (255, 0, 0)
        thickness = 2
        while True:
            _, img = cap.read()
            imgResize = cv2.resize(img, (454, 340))
            bg = cv2.imread('Cherry/bgg7.png')
            prediction = classifier.getPrediction(img)
            classID = prediction[1]
            print(classID)
            if classID != 2:
                if classID == 0:
                    bg = cv2.putText(bg, 'Unhealthy', org, font,

                                    fontScale, color, thickness, cv2.LINE_AA)
                elif classID == 1:
                    bg = cv2.putText(bg, 'Healthy', org, font,
                                    fontScale, color, thickness, cv2.LINE_AA)

            bg[148:148 + 340, 159:159 + 454] = imgResize
            cv2.imshow("Brain Tumor Detection", bg)
            cv2.waitKey(1)

    def startTask3(self):
        import os
        import cvzone
        from cvzone.ClassificationModule import Classifier
        import cv2

        cap = cv2.VideoCapture(1)
        classifier = Classifier('Corn/keras_model.h5', 'Corn/labels.txt')
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (750, 350)
        fontScale = 1
        color = (255, 0, 0)
        thickness = 2
        while True:
            _, img = cap.read()
            imgResize = cv2.resize(img, (454, 340))
            bg = cv2.imread('Corn/bg.jpg')
            prediction = classifier.getPrediction(img, draw=False)
            classID = prediction[1]
            print(classID)
            if classID != 2:
                if classID == 0:
                    print(0)
                    bg = cv2.putText(bg, 'Healthy', org, font,fontScale, color, thickness, cv2.LINE_AA)
                elif classID == 1:
                    print(1)
                    bg = cv2.putText(bg, 'Unhealthy', org, font,fontScale, color, thickness, cv2.LINE_AA)

            bg[148:148 + 340, 159:159 + 454] = imgResize
            cv2.imshow("Lung Cancer Detection", bg)
            cv2.waitKey(1)
    def startTask4(self):
        import os
        import cvzone
        from cvzone.ClassificationModule import Classifier
        import cv2

        cap = cv2.VideoCapture(1)
        classifier = Classifier('Grape/keras_model.h5', 'Grape/labels.txt')
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (750, 350)
        fontScale = 1
        color = (255, 0, 0)
        thickness = 2
        while True:
            _, img = cap.read()
            imgResize = cv2.resize(img, (454, 340))
            bg = cv2.imread('Grape/bgg8.jpg')
            prediction = classifier.getPrediction(img)
            classID = prediction[1]
            print(classID)
            if classID != 2:
                if classID == 0:
                    bg = cv2.putText(bg, 'Healthy', org, font,

                                    fontScale, color, thickness, cv2.LINE_AA)
                elif classID == 1:
                    bg = cv2.putText(bg, 'Unhealthy', org, font,
                                    fontScale, color, thickness, cv2.LINE_AA)

            bg[148:148 + 340, 159:159 + 454] = imgResize
            cv2.imshow("Brain Tumor Detection", bg)
            cv2.waitKey(1)
    def startTask5(self):
        import os
        import cvzone
        from cvzone.ClassificationModule import Classifier
        import cv2

        cap = cv2.VideoCapture(1)
        classifier = Classifier('Peach/keras_model(4).h5', 'Peach/labels(4).txt')
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (750, 350)
        fontScale = 1
        color = (255, 0, 0)
        thickness = 2
        while True:
            _, img = cap.read()
            imgResize = cv2.resize(img, (454, 340))
            bg = cv2.imread('Peach/bg.jpg')
            prediction = classifier.getPrediction(img)
            classID = prediction[1]
            print(classID)
            if classID != 0:
                if classID == 1:
                    bg = cv2.putText(bg, 'Healthy', org, font,

                                    fontScale, color, thickness, cv2.LINE_AA)
                elif classID == 2:
                    bg = cv2.putText(bg, 'Unhealthy', org, font,
                                    fontScale, color, thickness, cv2.LINE_AA)

            bg[148:148 + 340, 159:159 + 454] = imgResize
            cv2.imshow("Brain Tumor Detection", bg)
            cv2.waitKey(1)


app = QApplication(sys.argv)
oh_god_im_done = Main()