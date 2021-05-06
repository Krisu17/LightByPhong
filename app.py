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
        self.screen_size = (200, 200)
        self.ballObject = Ball(100, 100, 0, 50)  # x, y, z, r
        self.ballObject.setMaterialToMetal()
        self.LightObject = Light(120, 120, 400, 150)  # x, y, z, power
        self.Ia = 60
        self.Ka = 0
        self.fatt = 0.8

        super().__init__()

        if (len(sys.argv) > 1 and sys.argv[1] == "--debug"):
            nSlider = QSlider(Qt.Horizontal, self)
            nSlider.setGeometry(10, 10, 100, 10)
            nSlider.valueChanged[int].connect(self.changeN)
            self.labelN = QLabel("N=" + str(self.ballObject.n), self)
            self.labelN.setGeometry(110, 10, 50, 10)

            ksSlider = QSlider(Qt.Horizontal, self)
            ksSlider.setGeometry(10, 20, 100, 10)
            ksSlider.valueChanged[int].connect(self.changeKs)
            self.labelKs = QLabel("Ks=" + str(self.ballObject.Ks), self)
            self.labelKs.setGeometry(110, 20, 50, 10)

            kdSlider = QSlider(Qt.Horizontal, self)
            kdSlider.setGeometry(10, 30, 100, 10)
            kdSlider.valueChanged[int].connect(self.changeKd)
            self.labelKd = QLabel("Kd=" + str(self.ballObject.Kd), self)
            self.labelKd.setGeometry(110, 30, 50, 10)

            iaSlider = QSlider(Qt.Horizontal, self)
            iaSlider.setGeometry(10, 160, 100, 10)
            iaSlider.valueChanged[int].connect(self.changeIa)
            self.labelIa = QLabel("Ia=" + str(self.Ia), self)
            self.labelIa.setGeometry(110, 160, 50, 10)

            kaSlider = QSlider(Qt.Horizontal, self)
            kaSlider.setGeometry(10, 170, 100, 10)
            kaSlider.valueChanged[int].connect(self.changeKa)
            self.labelKa = QLabel("Ka=" + str(self.Ka), self)
            self.labelKa.setGeometry(110, 170, 50, 10)

            ipSlider = QSlider(Qt.Horizontal, self)
            ipSlider.setGeometry(10, 180, 100, 10)
            ipSlider.valueChanged[int].connect(self.changeIp)
            self.labelIp = QLabel("Ip=" + str(self.LightObject.power), self)
            self.labelIp.setGeometry(110, 180, 50, 10)

            fattSlider = QSlider(Qt.Horizontal, self)
            fattSlider.setGeometry(10, 190, 100, 10)
            fattSlider.valueChanged[int].connect(self.changeFatt)
            self.labelFatt = QLabel("fatt=" + str(self.fatt), self)
            self.labelFatt.setGeometry(110, 190, 50, 10)

    def changeN(self, value):
        self.ballObject.n = value * 100
        self.labelN.setText("N=" + str(self.ballObject.n*100))
        self.update()

    def changeKs(self, value):
        self.ballObject.Ks = value/100
        self.labelKs.setText("Ks=" + str(self.ballObject.Ks))
        self.update()

    def changeKd(self, value):
        self.ballObject.Kd = value/100
        self.labelKd.setText("Kd=" + str(self.ballObject.Kd))
        self.update()

    def changeIa(self, value):
        self.Ia = value
        self.labelIa.setText("Ia=" + str(self.Ia))
        self.update()

    def changeKa(self, value):
        self.Ka = value/100
        self.labelKa.setText("Ka=" + str(self.Ka))
        self.update()

    def changeIp(self, value):
        self.LightObject.power = value + 100
        self.labelIp.setText("Ip=" + str(self.LightObject.power))
        self.update()

    def changeFatt(self, value):
        self.fatt = value/100
        self.labelFatt.setText("fatt=" + str(self.fatt))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        ballBrighness = self.ballObject.getBallBrighness()
        ObservatorVector = [0, 0, -1]
        Ia = self.Ia
        Ip = self.LightObject.power
        Ka = self.Ka
        Ks = self.ballObject.getKs()
        Kd = self.ballObject.getKd()
        fatt = self.fatt
        n = self.ballObject.getN()
        hue = self.ballObject.getHue()
        saturation = self.ballObject.getSaturation()

        for x in range(self.screen_size[0]):
            for y in range(self.screen_size[1]):
                if not self.ballObject.isInBall(x, y):
                    # painter.setPen(QPen(Qt.black,  1, Qt.SolidLine))
                    # painter.drawPoint(x, y)
                    pass
                else:
                    z = self.ballObject.getZ(x, y)
                    NormalVector = np.subtract([x, y, z], [
                        self.ballObject.x, self.ballObject.y, self.ballObject.z])

                    NormalNormalized = NormalVector / \
                        np.linalg.norm(NormalVector)

                    LightVector = np.subtract([
                        self.LightObject.x, self.LightObject.y, self.LightObject.z], [x, y, z])

                    LightNormalized = LightVector/np.linalg.norm(LightVector)

                    dot_product = np.dot(ObservatorVector, LightNormalized)
                    angle = np.arccos(dot_product)
                    background = (Ia * Ka)
                    defiuzed = fatt * Ip*Kd * \
                        np.dot(NormalNormalized, LightNormalized)
                    speciular = (fatt*Ip*Ks*math.cos(angle)**n)
                    final = background + defiuzed + speciular
                    final = final * 255 / 100
                    velocity = final
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

        # for debbuging
        # if event.key() == Qt.Key_I:
        #     self.ballObject.increaseN()
        #     print("N = ", self.ballObject.getN())
        #     self.update()
        # if event.key() == Qt.Key_J:
        #     self.ballObject.decreaseN()
        #     print("N = ", self.ballObject.getN())
        #     self.update()
        # if event.key() == Qt.Key_P:
        #     self.ballObject.increaseKs()
        #     print("Ks = ", self.ballObject.getKs())
        #     self.update()
        # if event.key() == Qt.Key_L:
        #     self.ballObject.decreaseKs()
        #     print("Ks = ", self.ballObject.getKs())
        #     self.update()
        # if event.key() == Qt.Key_O:
        #     self.ballObject.increaseKd()
        #     print("Kd = ", self.ballObject.getKd())
        #     self.update()
        # if event.key() == Qt.Key_K:
        #     self.ballObject.decreaseKd()
        #     print("Kd = ", self.ballObject.getKd())
        #     self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.resize(200, 200)
    ex.show()
    sys.exit(app.exec_())
