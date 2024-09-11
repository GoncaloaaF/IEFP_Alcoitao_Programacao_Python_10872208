from flask import Flask, render_template, request, redirect
import uuid

app = Flask(__name__)

class Contacto:
    def __init__(self, nome, telefone):
        self.id = uuid.uuid4()
        self.nome = nome
        self.telefone = telefone



@app.route('/')
def hello_world():  # put application's code here

    ct = Contacto("nome", 12345)

    return render_template("homepage.html", ct=ct)


if __name__ == '__main__':
    app.run()
