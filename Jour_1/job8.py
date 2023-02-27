class Cercle:
    
  def __init__(self,rayon):
        self.rayon=rayon

  def ChangerRayon(self,newrayon):
      self.rayon= newrayon

  def Circonference(self):  
      return 2*3.14*self.rayon
      
  
  def Aire(self):
      return self.rayon * self.rayon *3.14
      
  
  def Diametre(self):
      return self.rayon*2
      
      
  def AfficherInfos(self):
      print("le rayon du cercle est de :",self.rayon,"La circonference du cercle est de :",self.Circonference(),"l'aire du cercle est de :",self.Aire(),"le diametre est de :",self.Diametre())

Cercle1=Cercle(4)
Cercle2=Cercle(7)
Cercle1.AfficherInfos()
Cercle2.AfficherInfos()