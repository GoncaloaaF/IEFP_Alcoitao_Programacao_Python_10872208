from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


'''

<url>?nome=goncalo&escola=IEFP

https://fad.iefp.pt/course/view.php?id=2124

http://127.0.0.1:5000/pag2?nome=goncalo
'''
@app.route('/pag2')
def pag2():
    nome = request.args.get('nome')
    escola = request.args.get('escola')
    return f"<h1>{nome} : {escola}</h1>"


'''
<url>/goncalo
https://fad.iefp.pt/course/2124
'''
@app.route('/pag3/<nome>')
def pag3(nome:str):
    return f'<h1>{nome}</h1>'



if __name__ == '__main__':
    app.run()


