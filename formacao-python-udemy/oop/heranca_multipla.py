class Base1:
    def __init__(self,atributo1):
        self.atribuito1 = atributo1
    def Base1_print(self):
        print("Base 1")

class Base2:
    def __init__(self,atributo2):
        self.atribuito2 = atributo2
    def Base2_print(self):
        print("Base 2")

class MinhaClasse(Base1,Base2): # herdando mais de uma classe
    def __init__(self):
        Base1.__init__(self,10)
        Base2.__init__(self,20)