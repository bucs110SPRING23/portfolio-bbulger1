import rectangle

class Surface:
    def __init__(self, filename, x, y, h, w):
        self.image = filename
        self.rect = rectangle.Rectangle(x, y, h, w)
    def getRect(self):
        return self.rect