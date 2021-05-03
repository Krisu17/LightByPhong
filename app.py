import sys
import numpy
import math
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from typing import Tuple
from PyQt5.QtWidgets import *


class Widget(QWidget):
    def __init__(self):
        self.screen_size = (800, 800)
        super().__init__()

    def paintEvent(self, event):
        colors = [Qt.red, Qt.blue, Qt.green, Qt.yellow, Qt.magenta, Qt.gray]
        painter = QPainter(self)

        # painter.setPen(QPen(Qt.red,  8, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))

        painter.drawEllipse(40, 40, 400, 400)


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
