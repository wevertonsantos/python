class ColecaoNumeros:
    def __init__(self,numero_maximo):
        self.max = numero_maximo
    def __iter__(self):
        self.numero_atual = 0
        return self
    
    def __next__(self): # vai retornar o próximo número
        if self.numero_atual <= self.max:
            retorno = self.numero_atual
            self.numero_atual += 1
            return retorno
        else:
            raise StopIteration
        
colecao = ColecaoNumeros(6) # deve ter 6 iterações