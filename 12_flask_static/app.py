from flask import Flask, render_template, request, redirect


app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("homepage.html")


if __name__ == '__main__':
    app.run()
