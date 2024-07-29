class demoClass:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def __eq__(self, other):
        return self.id == other.id and self.nome == other.nome


    def __str__(self):
        return f'''
id:                     {self.id},
nome:                   {self.nome}'''


