class Student:
    
    def __init__(self):
        self.__nom = "jhon"
        self.__prenom = "Doe"
        self.__numerodetud = 145
        self.__nombredecredit = 0
        self.__level = self.__studenteval()

    def addcredit(self):
        self.__nombredecredit += int(input("rentrer un nombre de credit "))
        if self.__nombredecredit >=0 :
            self.__level = self.__studenteval()
            return self.__nombredecredit
        else :
            print("le nombre de credit n'est pas valable")
            self.addcredit()
  
    def __studenteval(self):
        
        if self.__nombredecredit >= 90 :
            return"Exellent"
        if self.__nombredecredit >= 80 :
            return"Tres bien"
        if self.__nombredecredit >= 70 :
            return"Bien"
        if self.__nombredecredit >= 60 :
            return"Passable"
        if self.__nombredecredit < 60 : 
            return"Insuffisant"
        
    def studentinfo(self):
        print("Nombre de credit :",self.__nombredecredit)
        print("Nom :",self.__nom)
        print("Prenom",self.__prenom)
        print("Numero d'etudiant",self.__numerodetud)
        print("level",self.__level)
        

etudiant1 = Student()
print("le nombre de credit de jhon doe est de ",etudiant1.addcredit())
print("le nombre de credit de jhon doe est de ",etudiant1.addcredit())
print("le nombre de credit de jhon doe est de ",etudiant1.addcredit())
etudiant1.studentinfo()