from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    lista = ["Lisboa", "Porto","Braga","Sintra"]

    return render_template("index.html", state = lista)


if __name__ == '__main__':
    app.run()
