class Character:
    _x = None
    _vx = None
    _ax = None

    _y = None
    _vy = None
    _ay = None

    def __init__(self, x, y) -> None:
        self.setX(x)


        self.setY(y)

    def setX(self, newX):
        self._x = newX

    def setY(self, newY):
        self._y = newY

    def getX(self):
        return self._x
    
    def getY(self):
        return self._y
    
    def move(self):
        self.setVx(self.getVx() + self.getAx())
        self.setX(self.getX() + self.getVx())

        self.setVy(self.getVy() + self.getAy())
        self.setY(self.getY() + self.getVy())

    def update(self):
        self.move()


    


    
        