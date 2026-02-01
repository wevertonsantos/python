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