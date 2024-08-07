import uuid


class Contacto:
    def __init__(self, nome: str, telefone: str, email: str = None):
        self.__id = uuid.uuid4()
        self.nome = nome
        self.email = email
        self.telefone = telefone


    def __eq__(self, other):
        return self.__id == other.__id
