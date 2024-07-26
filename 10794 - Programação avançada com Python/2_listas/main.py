

nomes = ["Nome1", "Nome2", "Nome3", "Nome4", "Nome5"]
print(nomes)

print(nomes[0])
print(nomes[2])

nomes.append("Nome6")

print(nomes)

nomes.insert(2, "Novo nome no index 2")
print(nomes)

print("-----")

for nome in nomes:
    print(nome)

print("-----")


nomes[0] = "Novo nome ma pos 0"

print(nomes)

print("-----")


nomes.remove("Novo nome ma pos 0")

print(nomes)

print("-----")

nomes.pop(1)

print(nomes)

print("-----")

print(nomes.count("Nome5"))
nomes.append("Nome5")
nomes.append("Nome5")
nomes.append("Nome5")

print(nomes.count("Nome5"))

print("-----")
print(nomes.__len__())
print(len(nomes))

print("-----")
print(nomes)
# range(lb, up, step)
print(nomes[0:8:2])

print("-----")
print(nomes)
print(nomes[-1])
print(nomes[::-1])
print("-----")