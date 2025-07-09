class Veiculo:
    def __init__(self,marcha):
        self.marcha = marcha
    def aumenta_marcha(self):
        self.marcha += 1
        self.marcha = min(self.marcha,5)
    def diminui_marcha(self):
        self.marcha -= 1
        self.marcha = min(self.marcha,5)

class Palio(Veiculo):
    def __init__(self, marcha):
        Veiculo.__init__(self,marcha)

class EcoSport(Veiculo):
    def __init__(self, marcha):
        Veiculo.__init__(self,marcha)

    def aumenta_marcha(self): # sobrescrevendo aumenta marcha da classe pai
        self.marcha += 1
        self.marcha = min(self.marcha,6)