class Vehicule:
    
    def __init__(self,marque,annee,prix):
        self.marque = marque
        self.annee = annee
        self.prix = prix

    def informationVehicule(self,modele):
        self.modele = modele
        print("la marque du vehicule est : ",self.marque,"Le modele du vehicule est : ",self.modele,"L'annee du vehicule est : ",self.annee,"Le prix du vehicule est : ",self.prix)

    def demarrer(self):
        print("Je demarre")
        

class Voiture(Vehicule):
    
    def __init__(self, marque, annee, prix):
        super().__init__(marque, annee, prix)
        self.portes = 4
    
    def informationVehicule(self, modele):
        self.modele = modele
        print("la marque du vehicule est : ",self.marque," Le modele du vehicule est : ",self.modele," L'annee du vehicule est : ",self.annee," Le prix du vehicule est : ",self.prix," Nombres de portes du vehicule est de :",self.portes)

    def demarrer(self):
        print("Je demarre , Je roule")

class Moto(Vehicule):
    
    def __init__(self, marque, annee, prix,):
        super().__init__(marque, annee, prix)
        self.roue = 2
 
    def informationVehicule(self, modele):
      self.modele = modele
      print("la marque du vehicule est : ",self.marque," Le modele du vehicule est : ",self.modele," L'annee du vehicule est : ",self.annee," Le prix du vehicule est : ",self.prix," Nombres de roue du vehicule est de :",self.roue)

    def demarrer(self):
      print("Je demarre , Je vroum vroum")


Voiture1 = Voiture("Honda",1999,2055)
Voiture1.informationVehicule("serie X")
Voiture1.demarrer()
Moto1 = Moto("Toyota",2015,3000)
Moto1.informationVehicule("serie A")
Moto1.demarrer()