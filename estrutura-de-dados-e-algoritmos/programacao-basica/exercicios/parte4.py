'''
Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros e os armazene dentro de uma lista. Após a leitura, crie outra estrutura de repetição para somar todos os valores digitados
'''


numeros = []
for _ in range(0,5):
    n = int(input("Digite um número: "))
    numeros.append(n)

soma = 0
for numero in numeros:
    soma += numero
print(f"Soma dos números: {soma}")

'''
Crie um dicionário para armazenar o nome e a nota de 3 alunos, fazendo a leitura dos valores por meio de uma estrutura de repetição. Depois, crie uma nova estrutura de repetição para somar todas as notas e retornar a média
'''

notas_alunos = {
    'Maicon':10,
    'Leonardo':8,
    'Felipe':7
}

soma = 0
for nota in notas_alunos.values():
    soma += nota
print(f"Média: {round(soma/len(notas_alunos),2)}")

'''
Dada a matriz abaixo, construa uma estrutura de repetição para percorrer e somar todos os elementos da matriz
'''
import numpy as np

matriz = np.array([[3, 4, 1],
                   [3, 1, 5]])

soma = 0
for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        soma += matriz[i][j]
print(f"Soma dos elementos da matriz é: {soma}")