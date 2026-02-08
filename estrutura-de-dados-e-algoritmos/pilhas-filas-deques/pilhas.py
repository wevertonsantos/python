import numpy as np

class Pilha:
    def __init__(self,capacidade):
        self.__capacidade = capacidade
        self.__topo = -1
        self.__valores = np.empty(self.__capacidade,dtype=int)

    def __pilhar_cheia(self):
        if self.__topo == self.__capacidade - 1:
            return True
        else:
            return False
        
    def __pilha_vazia(self):
        if self.__topo == -1:
            return True
        else:
            return False
        
    def empilhar(self,valor):
        if self.__pilhar_cheia():
            print('A pilha está cheia')
        else:
            self.__topo += 1
            self.__valores[self.__topo] = valor
    
    def desempilhar(self):
        if self.__pilha_vazia():
            print("A pilha está vazia")
        else:
            self.__topo -= 1

    def ver_topo(self):
        if self.__topo != -1:
            return self.__valores[self.__topo]
        else:
            return -1
        
pilha = Pilha(5)
print(pilha.ver_topo())
pilha.empilhar(1)
print(pilha.ver_topo())