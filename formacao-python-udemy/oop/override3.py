class Veiculo:
    def __init__(self,marcha):
        self.marcha = marcha
    def aumenta_marcha(self):
        self.marcha += 1
        self.marcha = min(self.marcha,5)
    def diminui_marcha(self):
        self.marcha -= 1
        self.marcha = min(self.marcha,5)