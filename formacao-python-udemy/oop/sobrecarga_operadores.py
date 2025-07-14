class MeuNumero:
    def __init__(self,numero):
        self.numero = numero
    def __add__(self,outro): # operação de soma
        return self.numero + outro.numero
    
num1 = MeuNumero(10)
num2 = MeuNumero(20)
print(num1 + num2)