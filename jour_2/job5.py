class Voiture:
    
    def __init__(self):
        self.__marque = None
        self.__Modele = None
        self.__annee = None
        self.__kilometrage = None
        self.en_marche = False
        self.__reservoir = 50

    def modification_info(self):
      self.__marque += input("entrer la marque du vehicule ")
      self.__Modele += input("entrer le modele du vehicule ")
      self.__annee += input("entrer l'annee du vehicule ")
      self.__kilometrage += input("entrer le kilometrage du vehicule")

    def affichage_info(self):
        return  self.__marque ,self.__Modele, self.__annee ,self.__kilometrage 

    def demarrer(self):
        if self.__verifier_plein() > 5:
          self.en_marche = True
        else:
            pass

    def arreter(self):
        self.en_marche = False

  
    def __verifier_plein(self):
        return self.__reservoir