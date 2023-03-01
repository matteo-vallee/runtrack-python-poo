class CompteBancaire:
    
    def __init__(self,numcomp,nom,prenom,solde,decouvert):
        self.__nom = nom
        self.__numcomp = numcomp
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print("numero de compte :",self.__numcomp,"Nom proprietaire : ",self.__nom,"Prenom proprietaire : ",self.__prenom,"Solde proprietaire : ",self.__solde)
        
    def affichersolde(self):
        return self.__solde
    
    def versement(self,montantADD):
        self.__solde += montantADD
        
    def retrait(self,montantSPR):
          if self.__decouvert ==True or self.__solde >= montantSPR :
            self.__solde -= montantSPR
            self.agios()

    def agios(self):
        if self.__solde < 0:
            self.__solde *= 1.07 

    '''def virement(self,montantVER,compte,ref):
        ref.__solde -= montantVER
        compte.__solde += montantVER'''
    
    #ref n'est pas necessaire vu que on appel deja le compte dans la demande de virement
     
    def virement(self,montantVER,compte):
      self.__solde -= montantVER
      compte.__solde += montantVER
      self.agios()

CompteBancaire1 = CompteBancaire(145,"Vidal","Remi",100,True)
CompteBancaire2 = CompteBancaire(280,"Vallee","Matteo",6000,True)

print(CompteBancaire1.affichersolde())
CompteBancaire1.versement(200)
print(CompteBancaire1.affichersolde())
CompteBancaire1.retrait(685)
print(CompteBancaire1.affichersolde())
CompteBancaire2.virement(400,CompteBancaire1)
#Avec ref : CompteBancaire2.virement(400,CompteBancaire1,CompteBancaire2)
print(CompteBancaire1.affichersolde())
print(CompteBancaire2.affichersolde())