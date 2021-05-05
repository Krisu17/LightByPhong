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
        self.screen_size = (400, 400)
        self.ballObject = Ball(200, 200, 0, 100)  # x, y, z, r
        self.ballObject.setMaterialToMetal()
        self.LightObject = Light(440, 440, 400, 150)  # x, y, z, power
        super().__init__()

    def paintEvent(self, event):
        painter = QPainter(self)
        ballBrighness = self.ballObject.getBallBrighness()
        ObservatorVector = [0, 0, 1]
        Ia = 60
        Ip = self.LightObject.power
        Ka = 0.4
        Ks = self.ballObject.getKs()
        Kd = self.ballObject.getKd()
        fatt = 0.8
        n = self.ballObject.getN()
        hue = self.ballObject.getHue()
        saturation = self.ballObject.getSaturation()

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

                    dot_product = np.dot(ObservatorVector, LightNormalized)
                    angle = np.arccos(dot_product)

                    final = (Ia * Ka) + (fatt * Ip*Kd *
                                         np.dot(NormalNormalized, LightNormalized)) + \
                        (fatt*Ip*Ks*math.cos(angle)**n)
                    final = final * 255 / 100
                    velocity = ballBrighness - final
                    if velocity < 0:
                        velocity = 0
                    if velocity > 255:
                        velocity = 255
                    painter.setPen(
                        QPen(QColor.fromHsl(hue, saturation, velocity),  1, Qt.SolidLine))
                    painter.drawPoint(x, y)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.LightObject.moveLightToUp()
            self.update()
        if event.key() == Qt.Key_Left:
            self.LightObject.moveLightToLeft()
            self.update()
        if event.key() == Qt.Key_Right:
            self.LightObject.moveLightToRight()
            self.update()
        if event.key() == Qt.Key_Down:
            self.LightObject.moveLightToDown()
            self.update()
        if event.key() == Qt.Key_PageUp:
            self.LightObject.moveLightInside()
            self.update()
        if event.key() == Qt.Key_PageDown:
            self.LightObject.moveLightOutside()
            self.update()
        if event.key() == Qt.Key_1:
            self.ballObject.setMaterialToMetal()
            self.update()
        if event.key() == Qt.Key_2:
            self.ballObject.setMaterialToWool()
            self.update()
        if event.key() == Qt.Key_3:
            self.ballObject.setMaterialToPlastic()
            self.update()
        if event.key() == Qt.Key_4:
            self.ballObject.setMaterialToWood()
            self.update()


        #for debbuging
        if event.key() == Qt.Key_PageUp:
            self.ballObject.increaseN()
            print("N = ", self.ballObject.getN())
            self.paintEvent(event)()
        if event.key() == Qt.Key_PageDown:
            self.ballObject.decreaseN()
            print("N = ", self.ballObject.getN())
            self.update()
        if event.key() == Qt.Key_P:
            self.ballObject.increaseKs()
            print("Ks = ", self.ballObject.getKs())
            self.update()
        if event.key() == Qt.Key_L:
            self.ballObject.decreaseKs()
            print("Ks = ", self.ballObject.getKs())
            self.update()
        if event.key() == Qt.Key_O:
            self.ballObject.increaseKd()
            print("Kd = ", self.ballObject.getKd())
            self.update()
        if event.key() == Qt.Key_K:
            self.ballObject.decreaseKd()
            print("Kd = ", self.ballObject.getKd())
            self.update()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.resize(400, 400)
    ex.show()
    sys.exit(app.exec_())
