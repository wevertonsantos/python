class Base:
    def __init__(self):
        pass

class Herdeiro(Base):
    def __init__(self):
        pass

classe = Base()
e_base = isinstance(classe, Base) # verificando se a instancia do objeto é do tipo base classe
print(e_base)

classe = Herdeiro()
e_base = isinstance(classe,Base) 
e_herdero = isinstance(classe,Herdeiro) # verificação se classe herdada é do tipo base
print(e_base)
print(e_herdero)