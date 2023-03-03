class Rectangle:
    
    def __init__(self,longueur,largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def getlongueur(self):
        return self.__largeur
    
    def getlargeur(self):
      return self.__largeur
  
    def setlargeur(self,largeur):
       self.__largeur = largeur

    def setlongueur(self,longueur):
      self.__longueur = longueur
    
    def perimetre(self):
        return (self.__largeur + self.__longueur)*2
    
    def surface(self):
        return self.__longueur * self.__largeur
    
class Parallélépipède(Rectangle):
   
    def __init__(self, longueur, largeur,hauteur):
      Rectangle.__init__(self,longueur,largeur)
      self.hauteur = hauteur
  
    def volume(self):
       return self.getlargeur() * self.getlongueur() * self.hauteur
    
Rectangle1 =Rectangle(15,18)
Parallélépipède1 = Parallélépipède(15,18,30)
print(Rectangle1.surface())
print(Rectangle1.perimetre())
print(Parallélépipède1.volume())