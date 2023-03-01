class Ville:
    
    def __init__(self,nom ,nombrehabitant):
        self.__nom = nom
        self.__nombrehabitant = nombrehabitant

    
    def sethabitant(self):
        self.__nombrehabitant+=1


    def affichernombrehabitant(self):
      print(self.__nombrehabitant)


class Personne:

    def __init__(self,age,nomP,lieu): 
        self.__age = age
        self.__nomP = nomP
        self.__lieu = lieu

        
    def AjouterPopulation(self):
       self.__lieu.sethabitant()
      
        

ville1 = Ville("Paris",1000000)
ville2 = Ville("Marseille",861635)

personne1 = Personne(45,"Jhon",ville1)
personne2 = Personne(4,"Myrtille",ville1)
personne3 = Personne(18,"Chloe",ville2)

ville1.affichernombrehabitant()
ville2.affichernombrehabitant()
personne1.AjouterPopulation()
personne2.AjouterPopulation()
personne3.AjouterPopulation()
ville1.affichernombrehabitant()
ville2.affichernombrehabitant()
