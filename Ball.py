import math


class Ball:
    def __init__(self, x, y, z, r) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.r = r
        self.rSq = r*r

        # debugg
        self.nStep = 2
        self.ksStep = 0.1
        self.kdStep = 0.1

    def setMaterialToMetal(self) -> None:
        self.Ks = 0.92
        self.Kd = 0.53
        self.n = 100
        self.hue = 25
        self.saturation = 57*255/100

    def setMaterialToWool(self) -> None:
        self.Ks = 0.15
        self.Kd = 0.85
        self.n = 100
        self.hue = 180
        self.saturation = 16*255/100

    def setMaterialToPlastic(self) -> None:
        self.Ks = 0.71
        self.Kd = 0.44
        self.n = 900
        self.hue = 0
        self.saturation = 100*255/100

    def setMaterialToWood(self) -> None:
        self.Ks = 0.1
        self.Kd = 0.80
        self.n = 400
        self.hue = 21
        self.saturation = 49*255/100

    def getZ(self, x, y,) -> float:
        return math.sqrt(self.rSq - (x - self.x)**2-(y-self.y)**2) + self.z

    def getKs(self) -> float:
        return self.Ks

    def getKd(self) -> float:
        return self.Kd

    def getN(self) -> float:
        return self.n

    def getHue(self) -> int:
        return self.hue

    def getSaturation(self) -> int:
        return self.saturation

    def getBallBrighness(self) -> int:
        return self.ballBrighness

    def isInBall(self, x, y) -> bool:
        return (x-self.x)**2 + (y-self.y)**2 <= self.rSq

    # for debbuging

    def increaseN(self) -> None:
        self.n += self.nStep

    def decreaseN(self) -> None:
        self.n -= self.nStep

    def increaseKs(self) -> None:
        self.Ks += self.ksStep

    def decreaseKs(self) -> None:
        self.Ks -= self.ksStep

    def increaseKd(self) -> None:
        self.Kd += self.kdStep

    def decreaseKd(self) -> None:
        self.Kd -= self.kdStep
