from Contacto import Contacto
class Agenda:

    def __init__(self, nome: str):
        self.nome = nome
        self.listaContatos: list[Contacto] = []


    def adicionarContato(self,
                         nome: str = None,
                         telefone: str = None,
                         email: str = None,
                         contacto: Contacto = None):

        if contacto is not None:
            self.listaContatos.append(contacto)
            return

        ct = Contacto(nome, telefone, email)
        self.listaContatos.append(ct)

    def listarContatos(self):
        for ct in self.listaContatos:
            print(ct)

    def removerContato(self, contacto: Contacto):
        pass

    def atualizarContato(self, contacto: Contacto):
        pass



