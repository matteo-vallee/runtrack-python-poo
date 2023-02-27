class Personnage:
    
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def Gauche(self):
        self.x -=1

    def Droite(self):
        self.x +=1

    def Haut(self):
        self.y +=1

    def Bas(self):
        self.y -=1

    def position(self):
        print(self.x,self.y)

Personnage1 = Personnage(12,15)
Personnage1.Droite()
Personnage1.Droite()
Personnage1.Haut()
Personnage1.position()