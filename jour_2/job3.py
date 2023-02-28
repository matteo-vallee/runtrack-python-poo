class Livre:
  
  def __init__(self):
    self.__titre = None
    self.__auteur = None
    self.__nombredepages = 0
    self.__disponible= True

  def modifattr(self):
    self.__auteur = input("entrer le nom de l'auteur ")
    self.__titre = input("entrer le nom du livre ")
    self.__nombredepages = int(input("entrer le nombre de pages du livre "))
    self.condition()

  def resultpositif(self):
    return self.__auteur , self.__titre , self.__nombredepages
  
  def condition(self):
    if self.__nombredepages > 0 :
      print(self.resultpositif())
    else:
      print("entrer un nombre valable de pages (nombre entier superieur a 0) ")
      self.resutnegatif()

  def resutnegatif(self):
    self.__nombredepages = int(input("entrer le nombre de pages du livre "))
    self.condition()



  def verification(self):
      if self.__disponible == True:
        return True
      else :
        print("le livre a deja été emprunter ")
        return False
        
  def emprunter(self):
    if self.verification() == True:
      self.__disponible = False
      return True
    else:
      return False

  def rendre(self):
    if self.emprunter() == True:
      self.__disponible = True
      print("vous venez de rendre le livre")
    else:
      print("vous ne pouvez pas rendre le livre ")



cas1= Livre()
cas1.modifattr()
cas1.rendre()