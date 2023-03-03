

class Carte:
    
    def __init__(self):
        self.paquet = {"Pique":[],"Trefle":[],"Coeur":[],"Carreaux":[]}
       # self.listecouleur = ["Pique","Trefle","Coeur","Carreaux"]
    
    def initialisation(self):
        for couleur in list(self.paquet.keys()) :
          self.paquet[couleur].append({couleur:"2"})
          self.paquet[couleur].append({couleur:"3"})
          self.paquet[couleur].append({couleur:"4"})
          self.paquet[couleur].append({couleur:"5"})
          self.paquet[couleur].append({couleur:"6"})
          self.paquet[couleur].append({couleur:"7"})
          self.paquet[couleur].append({couleur:"8"})
          self.paquet[couleur].append({couleur:"9"})
          self.paquet[couleur].append({couleur:"10"})
          self.paquet[couleur].append({couleur:"Valet"})
          self.paquet[couleur].append({couleur:"Dame"})
          self.paquet[couleur].append({couleur:"Roi"})
          self.paquet[couleur].append({couleur:"AS"})
        print(self.paquet)


            
         

class Regle():
    
    def __init__(self):
        self.carteJ = 2
    
    #def distrubution(self,choix):
      
jeudecarte = Carte()
jeudecarte.initialisation()