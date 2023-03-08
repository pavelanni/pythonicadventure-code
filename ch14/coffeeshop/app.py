import os
import json
import sqlite3

from flask import Flask, render_template, request

def save_order(order):
    con = sqlite3.connect("orders.db")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO orders(name,drink,flavor,topping) VALUES(?,?,?,?);",
        (order["name"], order["drink"], order["flavor"], order["topping"]),
    )
    con.commit()
    return

def get_orders():
    con = sqlite3.connect("orders.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM orders;")
    rows = cur.fetchall()

    return rows

def read_menu(filename):
    f = open(filename)
    temp = f.readlines()
    result = []
    for item in temp:
        new_item = item.strip()
        result.append(new_item)

    return result

drinks = read_menu("drinks.txt")
flavors = read_menu("flavors.txt")
toppings = read_menu("toppings.txt")

con = sqlite3.connect("orders.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS orders(name, drink, flavor, topping);")


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
        new_order = {"name": request.form["name"],
                     "drink": request.form["drink"],
                     "flavor": request.form["flavor"],
                     "topping": request.form["topping"]
                     }
        save_order(new_order)
        return render_template(
            "print.html", new_order=new_order
        )

    return render_template("order.html", drinks=drinks, flavors=flavors, toppings=toppings)

@app.route("/list", methods=["GET"])
def list():
    orders = get_orders()

    return render_template("list.html", orders=orders)
