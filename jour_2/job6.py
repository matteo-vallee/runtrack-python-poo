class Commande:
    
    def __init__(self,plat,statut):
        self.__numero_de_commande = None
        self.__liste_de_plat_commandes = plat
        self.__statut_de_la_commande= statut

    def addplat(self):
      self.__liste_de_plat_commandes += input("rentrer le plat que vous voulez commander ")
      self.__statut_de_la_commande = "en cours"
    
    def annulcommand(self):
       self.__statut_de_la_commande = "annuler"

    
