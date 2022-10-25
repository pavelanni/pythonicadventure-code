# A simple web application.
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello/<name>")
def greet(name="Stranger"):
    return render_template("greeting.html", name=name)


@app.route("/order", methods=("GET", "POST"))
def order():
    if request.method == "POST":
        drink = request.form["drink"]
        print("Drink: ", drink)
        return render_template("print_drink.html", drink=drink)

    return render_template("forms.html")
