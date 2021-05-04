from Light import Light
import sys
import numpy
import math
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from typing import Tuple
from PyQt5.QtWidgets import *
from Ball import *

MATERIAL_COLOR = Qt.red


class Widget(QWidget):
    def __init__(self):
        self.screen_size = (800, 800)
        self.ballObject = Ball(240, 240, 0, 200)  # x, y, z, r
        self.LightObject = Light(440, 440, 400, 20)  # x, y, z, power
        super().__init__()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(MATERIAL_COLOR,  1, Qt.SolidLine))
        painter.setBrush(QBrush(MATERIAL_COLOR, Qt.SolidPattern))

        painter.drawEllipse(self.ballObject.x - self.ballObject.r, self.ballObject.y-self.ballObject.r,
                            self.ballObject.r*2, self.ballObject.r*2)  # tutaj poczatek rysowania jest w lewym gornym rogu dlatego odejmowane tez odejmowana jest dlugosc promienia od srodka

        painter.setPen(QPen(Qt.black,  1, Qt.SolidLine))
        for x in range(self.screen_size[0]):
            for y in range(self.screen_size[1]):
                if not self.ballObject.isInBall(x, y):
                    painter.drawPoint(x, y)
                else:


                    # def keyPressEvent(self, event):
                    #     ROTATION_STEP = numpy.radians(0.8)
                    #     if event.key() == Qt.Key_PageUp:
                    #         self.transformAllBy(0, -12, 0)
                    #     if event.key() == Qt.Key_PageDown:
                    #         self.transformAllBy(0, 12, 0)
                    #     if event.key() == Qt.Key_Left:
                    #         self.transformAllBy(12, 0, 0)
                    #     if event.key() == Qt.Key_Right:
                    #         self.transformAllBy(-12, 0, 0)
                    #     if event.key() == Qt.Key_Up:
                    #         self.transformAllBy(0, 0, -12)
                    #     if event.key() == Qt.Key_Down:
                    #         self.transformAllBy(0, 0, 12)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.resize(800, 800)
    ex.show()
    sys.exit(app.exec_())
