'''
# 1 - Crie uma classe para representar um carro. Ele deve ter um atributo que 
# diga sua potência em cavalos. Outro atributo deve dizer quanto de gasolina 
# por quilômetros ele consome. Cria duas instâncias e mostre os valores.
'''

class Carro:
    def __init__(self,potencia,gasolina_por_quilometros):
        self.potencia = potencia
        self.gasolina_por_quilometros = gasolina_por_quilometros

carro1 = Carro(100,200)
carro2 = Carro(200,350.5)
print(f"Potência do carro 1:{carro1.potencia} cavalos")
print(f"Alcance do carro 1: {carro1.gasolina_por_quilometros} km/l")
print(f"Potência do carro 2:{carro2.potencia} cavalos")
print(f"Alcance do carro 2: {carro2.gasolina_por_quilometros} km/l")