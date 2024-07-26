def soma(val1: int, val2: int) -> str:
    print(val1.numerator)
    return val1 + val2


def ola_mundo(nome: str, ano: int) -> str:
    return f"Ola Mundo {nome}!! no ano de {ano}"


"""
adapte a func ola_mundo2 para caso o local não seja indicado o seu retrun ser apenas 

"Ola Mundo {nome}!! no ano de {ano}" 

"""
def ola_mundo2(nome: str, ano: int = 2001, local: str = None) -> str:
    return f"Ola Mundo {nome}!! no ano de {ano} em {local}"