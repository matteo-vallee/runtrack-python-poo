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
    
Rectangle1 = Rectangle(15,45)
print(Rectangle1.aire())