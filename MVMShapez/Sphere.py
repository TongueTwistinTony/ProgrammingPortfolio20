import math

class Sphere():
    pi = 3.14159265
    def __init__(self, r):
        self.r = r

    def getVolume(self):
      r = self.r
      volume = str((4/3)*math.pi*r*r*r)
      return volume

    def getSurfaceArea(self):
      r = self.r
      surfaceArea = str(4*math.pi*r*r)
      return surfaceArea
