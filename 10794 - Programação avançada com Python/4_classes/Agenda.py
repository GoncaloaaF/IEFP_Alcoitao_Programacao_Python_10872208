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

<<<<<<< HEAD
        # garantir que não é adicionados duas vezes o mesmo contacto

        if Contacto is not None:
=======
        if contacto is not None:
>>>>>>> 938f46a5651f835f8bca83264cb708803b37324a
            self.listaContatos.append(contacto)
            return

        ct = Contacto(nome, telefone, email)
        self.listaContatos.append(ct)

    def listarContatos(self):
        for ct in self.listaContatos:
            print(ct)

    def removerContato(self, contacto: Contacto):

        if contacto in self.listaContatos:
            self.listaContatos.remove(contacto)


    def atualizarContato(self, contacto: Contacto):
        pass

    def find_contactoByName(self,name: str) -> Contacto:
        pass
