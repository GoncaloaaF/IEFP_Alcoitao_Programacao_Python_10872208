import Aluno as al


aluno1 = al.Aluno("nome Original")
aluno2 = aluno1


print(f"nome Aluno1: {aluno1.nome}")
print(f"nome Aluno2: {aluno2.nome}")


aluno2.nome = "Novo Nome"

print("--------")
print(f"nome Aluno1: {aluno1.nome}")
print(f"nome Aluno2: {aluno2.nome}")