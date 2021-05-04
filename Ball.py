import math


class Ball:
    def __init__(self, x, y, z, r) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.r = r
        self.rSq = r*r

    def setMaterialToMetal(self) -> None:
        self.Ks = 0.50
        self.Kd = 0.95
        self.n = 60
        self.hue = 271
        self.saturation = 24
        self.ballBrighness = 80
    
    def setMaterialToWool(self) -> None:
        self.Ks = 0.25
        self.Kd = 0.75
        self.n = 10
        self.hue = 297
        self.saturation = 86
        self.ballBrighness = 79
    
    def setMaterialToPlastic(self) -> None:
        self.Ks = 0.15
        self.Kd = 0.90
        self.n = 250
        self.hue = 112
        self.saturation = 100
        self.ballBrighness = 94
    
    def setMaterialToWood(self) -> None:
        self.Ks = 0.91
        self.Kd = 0.80
        self.n = 20
        self.hue = 20
        self.saturation = 52
        self.ballBrighness = 60
    

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
