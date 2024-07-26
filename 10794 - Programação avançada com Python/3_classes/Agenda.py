from Contacto import Contacto
class Agenda:

    def __init__(self, nome: str):
        self.nome = nome
        self.listaContatos: list[Contacto] = []


