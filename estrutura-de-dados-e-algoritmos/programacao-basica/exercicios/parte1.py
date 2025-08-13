'''
Ler dois números inteiros, executar e mostrar o resultado das seguintes operações: adição, subtração, multiplicação e divisão
'''

x = int(input('Digite um número inteiro: '))
y = int(input('Digite um segundo número inteiro: '))
print(x+y)
print(x-y)
print(x*y)
print(round(x/y,2))

'''
Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem
'''

tempo_gasto = float(input('Digite o tempo gasto na viagem: '))
velocidade_media = float(input('Digite a velocidade média na viagem: '))
distancia = tempo_gasto * velocidade_media
litros_usados = distancia / 12
print(f'Velocidade média: {velocidade_media}, tempo gasto: {tempo_gasto} e quantidade de litros utilizada na viagem: {round(litros_usados,2)}')