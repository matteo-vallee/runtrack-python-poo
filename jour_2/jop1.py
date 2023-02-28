class Rectangle:
    
    def __init__(self):
        self.__largeur = None
        self.__longeur = None

    def taillemodif(self):
       self.__longeur = input("definir la longueur ") 
       self.__largeur = input("definir la largeur ")
       
   
    def affichertaille(self):
      return self.__largeur,self.__longeur
    
rectangle1 = Rectangle()
rectangle1.taillemodif()
print(rectangle1.affichertaille())
