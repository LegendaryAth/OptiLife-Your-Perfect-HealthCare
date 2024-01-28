import PyQt5
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QMovie
from OptiLife_Main_UI import Ui_MainWindow as Ui_MainWindow_Main
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from cvzone.ClassificationModule import Classifier
import cv2
from OptiLife_Human_UI import Ui_MainWindow
class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    



startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow_Main()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask1)
        self.ui.pushButton_2.clicked.connect(self.startTask2)


    def Human(self):
        pass

    def Lung_Scan(self):
        cap = cv2.VideoCapture(0)
        classifier = Classifier('keras_model.h5', 'labels.txt')
        while True:
            _, img = cap.read()
            prediction = classifier.getPrediction(img)
            print(prediction)
            cv2.imshow("CAMERA", img)
            cv2.waitKey(1)

    def Brain_MRI(self):
        cap = cv2.VideoCapture(0)
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
            if classID == 0:
                bg = cv2.putText(bg, 'Glioma', org, font,

                                fontScale, color, thickness, cv2.LINE_AA)
            elif classID == 1:
                bg = cv2.putText(bg, 'Meningioma', org, font,
                                fontScale, color, thickness, cv2.LINE_AA)
            elif classID == 2:
                bg = cv2.putText(bg, 'Pituitary Tumor', org, font,
                                fontScale, color, thickness, cv2.LINE_AA)
            elif classID == 3:
                bg = cv2.putText(bg, 'No Tumor Detected', org, font,
                                fontScale, color, thickness, cv2.LINE_AA)

            bg[148:148 + 340, 159:159 + 454] = imgResize
            cv2.imshow("Brain Tumor Detection", bg)
            cv2.waitKey(1)

    def lung(self):
        self.ui.movie = QtGui.QMovie('gifFile-ezgif.com-video-to-gif-converter.gif')
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.Lung_Scan()
        

    def brain(self):
        
        self.ui.movie = QtGui.QMovie('gifFile2-ezgif.com-video-to-gif-converter.gif')
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.Brain_MRI()

app = QApplication(sys.argv)
oh_god_im_done = Main()
oh_god_im_done.show()
exit(app.exec_())