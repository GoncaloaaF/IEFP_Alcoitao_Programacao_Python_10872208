from Contacto import Contacto
from Pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self,
                 nome: str,
                 idade: int,
                 contactos: Contacto,
                 turma: list[str]):

        super().__init__(nome, idade, contactos)
        self.turma = turma


    def add_turma(self, turma: str):
        self.turma.append(turma)

    def remove_turma(self, turma: str):
        self.turma.remove(turma)

