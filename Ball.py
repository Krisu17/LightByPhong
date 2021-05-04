import math


class Ball:
    def __init__(self, x, y, z, r) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.r = r

    def getZ(self, x, y,) -> float:
        return math.sqrt(self.r**2 - (x - self.x)**2-(y-self.y)**2) + self.z

    def isInBall(self, x, y) -> bool:
        return (x-self.x)**2 + (y-self.y)**2 <= self.r**2
