import math

class Pyramid():
    def __init__(self, l, w, h):
        self.l = l
        self.w = w
        self.h = h
    def getVolume(self):
      l = self.l
      w = self.w
      h = self.h
      volume = str((l*w*h)/3)
      return volume
    def getSurfaceArea(self):
      l = self.l
      w = self.w
      h = self.h
      surfaceArea = str(l*w + l*(math.sqrt((((w/2)*(w/2))+(h*h)))) + w*(math.sqrt(((l/2)*(l/2))+(h*h))))
      return surfaceArea
