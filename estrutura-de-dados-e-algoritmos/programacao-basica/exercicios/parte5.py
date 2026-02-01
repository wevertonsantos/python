'''

Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. A fórmula de conversão é F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit e C é a temperatura em graus Celsius
- Função para ler e retorna o valor da temperatura (não recebe parâmetro)
- Função para fazer o cálculo (recebe como parâmetro a temperatura em graus Celsius)
- Função para mostrar o resultado, recebendo como parâmetro o valor e fazendo a impressão

'''

def temperatura_celsius():
    c = int(input("Digite a temperatura em Celsius: "))
    return c

def temperatura_fahrenheit(temperatura_celsius):
    f = ((9 * temperatura_celsius + 160) / 5)
    return f

def resultado_conversao(temperatura_fahrenheit):
    f = temperatura_fahrenheit
    print(f"Essa foi a temperatura convertida para Fahrenheit: {f}")

c = temperatura_celsius()
f = temperatura_fahrenheit(c)
resultado_conversao(f)

'''
Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem

- Função para ler os valores (não recebe parâmetro e retorna os dois valores)
- Função para calcular a distância (recebe como parâmetro o tempo e a velocidade e retorna a distância)
- Função para calcular a quantidade de litros (recebe como parâmetro a distância e retorna os litros)
- Função para apresentar o resultado (recebe como parâmetro os valores e somente imprime o resultado)
'''

def tempo_gasto_velocidade_media():
    tempo_gasto = int(input("Digite o tempo gasto na viagem: "))
    velocidade_media = int(input("Digite a velocidade média durante viagem: "))
    return tempo_gasto,velocidade_media

def calcular_distancia(tempo_gasto,velocidade_media):
    distancia = tempo_gasto * velocidade_media
    return distancia

def calcular_quantidade_litros(distancia):
    litros_usados = distancia / 12
    return litros_usados

tempo_gasto,velocidade_media = tempo_gasto_velocidade_media()
distancia = calcular_distancia(tempo_gasto,velocidade_media)
litros_usados = calcular_quantidade_litros(distancia)

def mostrar_resultado(tempo_gasto,velocidade_media,distancia,litros_usados):
    print(f"Tempo gasto: {tempo_gasto}, velocidade média: {velocidade_media}, distancia: {distancia} e litros usados: {litros_usados}")

mostrar_resultado(tempo_gasto,velocidade_media,distancia,litros_usados)