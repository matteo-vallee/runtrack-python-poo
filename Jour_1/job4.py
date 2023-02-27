class Personne:
  def __init__(self,nom,prenom):
      self.nom = nom
      self.prenom = prenom

  def SePresenter(self):
    print("bonjour je suis",self.prenom,self.nom)

Personne1 = Personne("Vallee","Matteo")
Personne2 = Personne("Vidal-Michell","Remi")
Personne1.SePresenter()
Personne2.SePresenter()