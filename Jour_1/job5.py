class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def AfficherLesPoint(self):
        print(self.x , self.y)

    def AfficherX(self):
        print(self.x)

    def AfficherY(self):
        print(self.y)
      
    def ChangerX(self,newx):
        self.x=newx
        print(self.x)

    def ChangerY(self,newy):
        self.y=newy

coord = Point(255,378)
coord.AfficherLesPoint()
coord.AfficherX()
coord.AfficherY()
coord.ChangerX(25)
coord.ChangerY(345)