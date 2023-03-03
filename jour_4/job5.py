class Forme:
    
    def __init__(self) -> None:
        pass
    
    def aire(self):
        return 0
    

class Rectangle(Forme):
    
    def __init__(self,longueur,largeur):
        super().__init__()
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        return self.longueur * self.largeur
    
class Cercle(Forme):
    
    def __init__(self,radius):
        super().__init__()
        self.radius = radius

    def aire(self):
        return self.radius*self.radius*3.14
    
Rectangle1 = Rectangle(15,45)
Cercle1 = Cercle(24)
print(Cercle1.aire())
print(Rectangle1.aire())