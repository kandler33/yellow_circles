import sys

from PyQt5 import uic
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super(MyWidget, self).__init__()
        uic.loadUi('Ui.ui', self)
        self.pushButton.clicked.connect(self.pushButton_handler)
        self.rects = []

    def pushButton_handler(self):
        rad = randint(20, 200)
        x, y = randint(0, 500 - rad), randint(0, 500 - rad)
        rect = QRect(x, y, rad, rad)
        self.rects.append(rect)
        self.update()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        for rect in self.rects:
            self.draw_circle(painter, rect)

    def draw_circle(self, painter, rect):
        painter.setBrush(QBrush(QColor(255, 255, 0)))
        painter.drawEllipse(rect)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
