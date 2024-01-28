import PyQt5
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QMovie
from OptiLife_Main_UI import Ui_MainWindow as Ui_MainWindow_Main
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from cvzone.ClassificationModule import Classifier
import cv2
from OptiLife_Human_UI import Ui_MainWindow as Ui_MainWindow_Human
from OptiLife_Plant_UI import Ui_MainWindow as Ui_MainWindow_Plant
import Human
import Plant

class MainThread1(QThread):
    def __init__(self):
        super(MainThread1, self).__init__()

    def run(self):
        self.TaskExecution()

class Main1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow_Main()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.Human)
        self.ui.pushButton_2.clicked.connect(self.Plant)


    def Human(self):
        Human.oh_god_im_done.show()
        Human.app.exec_()

    def Plant(self):
        Plant.oh_god_im_done.show()
        Plant.app.exec_()


app = QApplication(sys.argv)
oh_god_im_done = Main1()
oh_god_im_done.show()
exit(app.exec_())
