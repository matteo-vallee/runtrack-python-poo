class Animal:
    
    def __init__(self):
        self.age= 0 
        self.prenom=None

    def Vieillir(self):
        self.age +=1
        print("l'age de l'animal est de :",self.age)

    def Nommer(self,prenom):
        self.prenom = prenom
        print(self.prenom)

Animal1= Animal()
Animal1.Vieillir()
Animal1.Vieillir()
Animal1.Vieillir()
Animal1.Vieillir()
Animal1.Vieillir()
Animal1.Vieillir()
Animal1.Nommer("Narval")