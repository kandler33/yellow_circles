import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from random import randint


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 180, 75))
        self.pushButton.setMinimumSize(QtCore.QSize(180, 75))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Новая окружность"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushButton_handler)
        self.circle_parameters = []

    def pushButton_handler(self):
        rad = randint(20, 200)
        x, y = randint(0, 500 - rad), randint(0, 500 - rad)
        rect = QRect(x, y, rad, rad)
        color = QColor(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        self.circle_parameters.append((rect, color))
        self.update()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        for rect in self.circle_parameters:
            self.draw_circle(painter, *rect)

    def draw_circle(self, painter, rect, color):
        painter.setBrush(QBrush(color))
        painter.drawEllipse(rect)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
