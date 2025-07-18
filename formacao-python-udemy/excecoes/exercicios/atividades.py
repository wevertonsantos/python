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