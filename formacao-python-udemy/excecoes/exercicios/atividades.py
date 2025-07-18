'''
1 - Crie uma função que receba duas strings que serão convertidas para
números para serem somadas, se ao realizar o casting ocorrer um erro, gere
uma exceção informando o motivo.
'''

def soma(s1,s2):
    try:
        return int(s1) + int(s2)
    except:
        print("Valores que você digitou não é válido")

print(soma('10','s'))

'''
2 - Crie uma função que receba uma lista e um número e retorne o elemento
da lista na posição deste número. Faça um tratamento para que caso haja um
acesso fora do índice a função retorne o valor None.
'''

def funcao(lista,num):
    try:
        return lista[num]
    except:
        return None

print(funcao([1,2,3,4,5,6],10))