from Light import Light
import sys
import numpy as np
import math
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from typing import Tuple
from PyQt5.QtWidgets import *
from Ball import *


class Widget(QWidget):
    def __init__(self):
        self.screen_size = (800, 800)
        self.ballObject = Ball(240, 240, 0, 200)  # x, y, z, r
        self.LightObject = Light(440, 440, 400, 200)  # x, y, z, power
        super().__init__()

    def paintEvent(self, event):
        painter = QPainter(self)

        for x in range(self.screen_size[0]):
            for y in range(self.screen_size[1]):
                if not self.ballObject.isInBall(x, y):
                    painter.setPen(QPen(Qt.black,  1, Qt.SolidLine))
                    painter.drawPoint(x, y)
                else:
                    z = self.ballObject.getZ(x, y)

                    NormalVector = np.subtract([x, y, z], [
                        self.ballObject.x, self.ballObject.y, self.ballObject.z])

                    NormalNormalized = NormalVector / \
                        np.linalg.norm(NormalVector)

                    LightVector = np.subtract([x, y, z], [
                        self.LightObject.x, self.LightObject.y, self.LightObject.z])

                    LightNormalized = LightVector/np.linalg.norm(LightVector)

                    ObservatorVector = [0, 0, 1]

                    dot_product = np.dot(ObservatorVector, LightNormalized)
                    angle = np.arccos(dot_product)

                    Ia = 0
                    Ip = self.LightObject.power
                    Ka = 0.1
                    Ks = 0.25
                    Kd = 0.75
                    fatt = 0.8
                    n = 10
                    final = (Ia * Ka) + (fatt * Ip*Kd *
                                         np.dot(NormalNormalized, LightNormalized)) + \
                        (fatt*Ip*Ks*math.cos(angle)**n)

                    painter.setPen(
                        QPen(QColor.fromHsv(342, 71, 79 - final),  1, Qt.SolidLine))
                    painter.drawPoint(x, y)

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
