from Aluno import Aluno
from Professor import Professor
from  Contacto import Contacto

print("Herança")


ct = Contacto("tlm", "morada", "email")
al = Aluno("Carlos",
           30,
           ct,
           "py")

prof = Professor("Jonath",
                 30,
                 Contacto("tlm prof", "morada prof", "email prof"),
                 ["py", "java"])



al.showContactos()
prof.showContactos()

myLista = [al, prof]
print("--" * 10)

for i in myLista:
    print(i.showInfo())