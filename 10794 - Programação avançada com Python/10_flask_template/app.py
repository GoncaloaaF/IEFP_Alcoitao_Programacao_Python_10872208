from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():  # put application's code here
    return render_template("index.html")


@app.route('/pag2')
def pag2():  # put application's code here
    return render_template("pag2.html")



@app.route('/pag3')
def pag3():  # put application's code here
    return render_template("pag3.html")


@app.route('/pag4')
def pag4():  # put application's code here
    return render_template("pag3.html")



if __name__ == '__main__':
    app.run()
