import math


class Light:

    def __init__(self, x, y, z, power) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.power = power
        self.step = 30

    def moveLightToRight(self) -> None:
        self.x += self.step

    def moveLightToLeft(self) -> None:
        self.x -= self.step

    def moveLightToUp(self) -> None:
        self.y -= self.step

    def moveLightToDown(self) -> None:
        self.y += self.step

    def moveLightInside(self) -> None:
        self.z -= self.step

    def moveLightOutside(self) -> None:
        self.z += self.step

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getZ(self):
        return self.z
