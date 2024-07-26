class Carro:
    def __init__(self, cor, marca, modelo):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.ligdo = False

    def ligar(self):
        if not self.ligdo:
            self.ligdo = True

    def desligar(self):
        if self.ligdo:
            self.ligdo = False

    def acelerar(self):
        pass

    def travar(self):
        pass
