from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Pag 2</h1>'

@app.route("/infos")
def infos():
    return "<h1>infos Sem Id</h1>"

@app.route("/infos/<id>")
def infos2(id: int):
    return f"<h1>infos id:{id}</h1>"

@app.route("/myinfo")
def myInfo():
    return render_template("index.html")



if __name__ == '__main__':
    app.run()
