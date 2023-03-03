class Personne:
    
    def __init__(self):
        self.age = 14


    def afficherage(self):
        print(self.age)

    def bonjours(self):
        print("Hello")

    def modifierage(self,MODage):
        self.age = MODage



class Eleve(Personne):
    
    def __init__(self):
        Personne.__init__(self)

    def allerencours(self):
        print("je vais en cours")

    def affichageage(self):
        print("j'ai",self.age,"ans")


class Professeur(Personne):
    
    def __init__(self,matiereEnseigner):
      self.matiereEnseigner = matiereEnseigner

    def enseigner(self):
        print("le cous va commencer")


Personne1 = Personne()
Eleve1 = Eleve()
Eleve1.affichageage()