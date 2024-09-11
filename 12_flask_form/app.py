from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class Aluno:
    def __init__(self, nome, turma):
        self.nome = nome
        self.turma = turma


alunos = [
    Aluno('Carlos', 'py2024'),
    Aluno('Ana', 'py2024'),
    Aluno('Rita', 'C++2024'),
    Aluno('Maria', 'py2022'),
    Aluno('Luis', 'py2022')
]

@app.route('/')
def hello_world():  # put application's code here
    return render_template("add_form.html")

@app.route('/txt_aleatorio', methods=['POST'])
def add_aluno():


    print(request.form)

    nome = request.form['nome_aluno']
    turma = request.form['turma_aluno']
    al = Aluno(nome, turma)
    alunos.append(al)

    return redirect(url_for("lista_alunos"))



@app.route('/alunos')
def lista_alunos():
    return render_template("lista_alunos.html",
                           al=alunos)











"""

Get  - Ler dados
Post - Escrever dados

"""

