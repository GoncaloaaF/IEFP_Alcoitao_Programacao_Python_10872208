from flask import Flask, render_template, request
app = Flask(__name__)

class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

@app.route('/')
def home():  # put application's code here
    return render_template("index.html",
                           titulo="Home Page")


@app.route('/pag2')
def pag2():  # put application's code here

    aluno = Aluno("Rita", 18)

    return render_template("pag2.html",
        titulo = aluno.nome,
        aluno = aluno
    )





@app.route('/pag3/<nome>')
def pag3(nome:str):  # put application's code here
    return render_template("pag3.html",
                           titulo = "Pagina 3",
                           nome = nome)



'''


?nome=<nome_usr>&idade=<idade_usr>
'''

@app.route('/pag4')
def pag4():
    nome = request.args.get('nome')
    idade = request.args.get('idade')
    idade = int(idade)

    al = Aluno(nome, idade)

    return render_template("pag4.html",
                           titulo = "Pagina 4",
                           aluno = al)




if __name__ == '__main__':
    app.run()
