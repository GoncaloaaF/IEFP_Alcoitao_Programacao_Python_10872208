import Contacto as ct


def soma(v1: int, v2: int) -> int:
    return v1 + v2


mtCt = ct.Contacto("Gonçalo",
                   21,
                   "goncalo@gmai.com",
                   "12324234324")

myCt2 = ct.Contacto(nome="Gonçalo",
                    idade=31,
                    email="goncalo@gmai.com",
                    telefone="12324234324"
                    )
