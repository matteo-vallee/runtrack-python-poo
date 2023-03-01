class Joueur:
    
    def __init__(self,nom,numero,position,nombredebutMarque,passdecisive,cartonjaunes,cartonrouges):
       self.nom = nom
       self.numero = numero
       self.position = position
       self.nombredebutMarque = nombredebutMarque 
       self.passdecisive = passdecisive
       self.cartonjaunes = cartonjaunes
       self.cartonrouges = cartonrouges

    def marquerUnBut(self,nombredebut):
        self.nombredebutMarque = nombredebut
  
    def effectuerUnePasseDecisive(self,passde):
        self.passdecisive = passde


    def recevoirUnCartonJaune(self,cartonJ):
        self.cartonjaunes = cartonJ
 
      
    def recevoirUnCartonRouge(self,cartonR):
        self.cartonrouges = cartonR

    def afficherStatistiques(self):
        print("Nom du joueur : ",self.nom,"Numero du joueur : ",self.numero,"Position du joueur : ",self.position,"Nombre de but marquer par le joueur : ",self.nombredebutMarque,"Passe decisive du Joueur : ",self.passdecisive,"cartons Jaunes du joueur : ",self.cartonjaunes,"cartons rouges du joueur",self.cartonrouges)
        


class Equipe:
    
    def __init__(self,nom):
        self.nom = nom
        self.listedejoueur = []


    def ajouterJoueur(self,addjoueur):
        self.listedejoueur.append(addjoueur)
        
    def AfficherStatistiquesJoueurs(self):
        for joueur in self.listedejoueur:
            print(joueur.nom,joueur.numero,joueur.position,joueur.nombredebutMarque,joueur.passdecisive,joueur.cartonjaunes,joueur.cartonrouges)
        

    def mettreAJourStatistiquesJoueur(self,choixjoueur):
        for _ in self.listedejoueur:
            self.listedejoueur.remove(choixjoueur)
            self.listedejoueur.append(choixjoueur)

       

Joueur1 = Joueur("Zidane",21,"Millieu de terrain",2,5,2,1)
Joueur2 = Joueur("Neymar",10,"Attaquant",4,8,5,0)
Joueur3 = Joueur("Mbappe",7,"Attaquant",8,9,1,0)
Equipe1 = Equipe("France")      
Equipe1.ajouterJoueur(Joueur1)
Equipe1.ajouterJoueur(Joueur2)
Equipe1.ajouterJoueur(Joueur3)
Equipe1.AfficherStatistiquesJoueurs()
Joueur1.marquerUnBut(8)
Equipe1.mettreAJourStatistiquesJoueur(Joueur1)
Equipe1.AfficherStatistiquesJoueurs()
