from Contacto import Contacto
from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self,
                 nome:str ,
                 idade:int,
                 contactos:Contacto,
                 turma:str):
        super().__init__(nome, idade, contactos)
        self.turma = turma
        self.lista_notas = []


    def add_nota(self, notas: float):
        self.lista_notas.append(notas)

    def get_media(self) -> float:
        # implementar como challenge
        return 0.0


    def showInfo(self):
        return self.turma, super().showInfo()


