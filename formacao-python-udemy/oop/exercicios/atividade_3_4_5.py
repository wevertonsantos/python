'''
3 - Crie uma classe base que represente um veículo. 
Os atributos devem ser peso do veiculo, número de rodas e potência. 
Em seguida crie três classes que herdam esse veículo: ônibus, carro e moto. 
Crie uma instância de cada tipo e imprima as instâncias
'''

class Veiculo:
    def __init__(self,peso,rodas,potencia):
        self.peso = peso
        self.rodas = rodas
        self.potencia = potencia
    def __lt__(self,outro) :
        return self.potencia < outro.potencia
    def __gt__(self, outro):
        return self.potencia > outro.potencia

    def distancia_percorrida(self):
        return (self.peso / self.potencia) * 1000

class Onibus(Veiculo):
    def __init__(self, peso, potencia, rodas):
        Veiculo.__init__(self, peso, potencia, rodas)

class Carro(Veiculo):
    def __init__(self, peso, potencia, rodas):
        Veiculo.__init__(self, peso, potencia, rodas)

class Moto(Veiculo):
    def __init__(self, peso, potencia, rodas):
        Veiculo.__init__(self, peso, potencia, rodas)

onibus = Onibus(1000,400,6)
print(f"Ônibus: Peso {onibus.peso} Potência {onibus.potencia} Rodas: {onibus.rodas}")
print(f"Distância percorrida ônibus: {onibus.distancia_percorrida():.2f}")
carro = Carro(300,100,4)
print(f"Carro: Peso {carro.peso} Potência {carro.potencia} Rodas: {carro.rodas}")
print(f"Distância percorrida carro: {carro.distancia_percorrida():.2f}")
moto = Moto(100,50,2)
print(f"Moto: Peso {moto.peso} Potência {moto.potencia} Rodas: {moto.rodas}")
print(f"Distância percorrida moto: {moto.distancia_percorrida():.2f}")

print(onibus > carro)
print(onibus < moto)
print(moto > carro)