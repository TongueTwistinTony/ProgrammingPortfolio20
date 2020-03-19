class Box():
    def __init__(self, w, l, h):
        self.w = w
        self.l = l
        self.h = h

    def getVolume(self):
      l = self.l
      w = self.w
      h = self.h
      volume = str(l*w*h)
      return volume
        
    def getSurfaceArea(self):
      l = self.l
      w = self.w
      h = self.h
      surfaceArea = str(2*l*w + 2*h*w + 2*h*l)
      return surfaceArea
