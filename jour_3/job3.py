class Tache:
    
    def __init__(self,titre,description,statut):
        self.titre = titre
        self.description = description
        self.statut = statut
    
    def marquerCommeFinie(self,liste,tache):
        liste.supprimerTache(tache)
        if self.statut == "A faire" or self.statut == "a faire":
            self.statut = "Terminer"
        liste.ajouterTache(tache)

          



class ListeDeTaches:
    
    def __init__(self):
      self.taches = []

    def ajouterTache(self ,addtache): 
         self.taches.append(addtache)
    
    def supprimerTache(self,supprtache):
        self.taches.remove(supprtache)


    def afficherliste(self):
        for tache in self.taches:
            print(tache.titre,tache.description,tache.statut)

    def filterliste(self):
        for tache in self.taches:
            if tache.statut =="A faire":
                print(tache.titre,tache.description,tache.statut)

tache1= Tache("Meurtre","tuer Remi","A faire")
tache2= Tache("Meurtre","tuer Leo","A faire")
tache3= Tache("Meurtre","tuer Enzo","A faire")
ListeDeTaches1=ListeDeTaches()
ListeDeTaches1.ajouterTache(tache1)
ListeDeTaches1.ajouterTache(tache2)
ListeDeTaches1.ajouterTache(tache3)
ListeDeTaches1.supprimerTache(tache1)
tache3.marquerCommeFinie(ListeDeTaches1,tache3)
ListeDeTaches1.afficherliste()
ListeDeTaches1.filterliste()