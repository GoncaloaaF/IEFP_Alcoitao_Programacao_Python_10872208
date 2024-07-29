from Contacto import Contacto

class Pessoa:
    def __init__(self,
                 nome: str,
                 idade: int,
                 contactos: Contacto):
        self.nome = nome
        self.idade = idade
        self.contactos = contactos

    def setContactos(self, contactos):
        self.contactos = contactos

    def showContactos(self):
        print(self.contactos)


    def showInfo(self):
        return self.nome, self.idade, self.contactos.telefone