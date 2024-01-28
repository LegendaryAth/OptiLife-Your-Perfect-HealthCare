import PyQt5
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QMovie
from OptiLife_Human_UI import Ui_MainWindow
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

    def startTask1(self):
        self.ui.movie = QtGui.QMovie('gifFile-ezgif.com-video-to-gif-converter.gif')
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        import os
        import cvzone
        from cvzone.ClassificationModule import Classifier
        import cv2

        cap = cv2.VideoCapture(1)
        classifier = Classifier('Lung_Scan/keras_model.h5', 'Lung_Scan/labels.txt')
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (750, 350)
        fontScale = 1
        color = (255, 0, 0)
        thickness = 2
        while True:
            _, img = cap.read()
            imgResize = cv2.resize(img, (454, 340))
            bg = cv2.imread('Lung_Scan/bgg2.png')
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
            cv2.imshow("Lung Cancer Detection", bg)
            cv2.waitKey(1)

    def startTask2(self):

        import os
        import cvzone
        from cvzone.ClassificationModule import Classifier
        import cv2

        cap = cv2.VideoCapture(1)
        classifier = Classifier('Brain_MRI/keras_model(1).h5', 'Brain_MRI/labels(1).txt')
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (750, 350)
        fontScale = 1
        color = (255, 0, 0)
        thickness = 2
        while True:
            _, img = cap.read()
            imgResize = cv2.resize(img, (454, 340))
            bg = cv2.imread('Brain_MRI/bgg3.png')
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
            cv2.imshow("Brain Tumor Detection", bg)
            cv2.waitKey(1)


    def startTask3(self):
        self.ui.movie = QtGui.QMovie('gifFile-ezgif.com-video-to-gif-converter.gif')
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        import os
        import cvzone
        from cvzone.ClassificationModule import Classifier
        import cv2

        cap = cv2.VideoCapture(1)
        classifier = Classifier('Skin_Cancer/keras_model(2).h5', 'Skin_Cancer/labels(2).txt')
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (750, 350)
        fontScale = 1
        color = (255, 0, 0)
        thickness = 2
        while True:
            _, img = cap.read()
            imgResize = cv2.resize(img, (454, 340))
            bg = cv2.imread('Skin_Cancer/bgg.png')
            prediction = classifier.getPrediction(img)
            classID = prediction[1]
            print(classID)
            if classID != 5:
                if classID == 1:
                    bg = cv2.putText(bg, 'Nevus', org, font,

                                    fontScale, color, thickness, cv2.LINE_AA)
                elif classID == 2:
                    bg = cv2.putText(bg, 'Melanoma', org, font,
                                    fontScale, color, thickness, cv2.LINE_AA)
                elif classID == 3:
                    bg = cv2.putText(bg, 'Dermatofibroma', org, font,
                                    fontScale, color, thickness, cv2.LINE_AA)
                elif classID == 4:
                    bg = cv2.putText(bg, 'Actinic Keratosis', org, font,
                                    fontScale, color, thickness, cv2.LINE_AA)
                else:
                    bg = cv2.putText(bg, 'Normal Skin', org, font,
                                    fontScale, color, thickness, cv2.LINE_AA)

            bg[148:148 + 340, 159:159 + 454] = imgResize
            cv2.imshow("Skin Cancer Detection", bg)
            cv2.waitKey(1)

app = QApplication(sys.argv)
oh_god_im_done = Main()