class Operation:
    def __init__(self,nombre1,nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def printnombre(self):
        print(self.nombre1,self.nombre2)


object1 = Operation(6,8)
object1.printnombre()