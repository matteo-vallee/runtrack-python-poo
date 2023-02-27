class Produit:
    
    def __init__(self,nom,PrixHT,TVA):
        self.nom = nom
        self.PrixHT = PrixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.PrixHT * self.TVA 
    
    def Afficher(self):
        self.attributproduit = "nom du produit",self.nom,"Prix hors Taxe",self.PrixHT,"Taux de la TVA",self.TVA,"Prix tout taxe comprise",self.CalculerPrixTTC()
        return self.attributproduit
    
    def ChangerNom(self,Newnom):
        self.nom = Newnom

    def ChangerPrix(self,Newprix):
        self.PrixHT = Newprix

    def ChangerTVA(self,NewTVA):
        self.TVA = NewTVA

Produit1 = Produit("Casque",122,1.3)
print(Produit1.Afficher())
Produit1.ChangerNom("Ordinateur")
Produit1.ChangerPrix(1500)
Produit1.ChangerTVA(1.68)
print(Produit1.Afficher())