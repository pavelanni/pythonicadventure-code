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


con = sqlite3.connect("orders.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS orders(name, drink, flavor, topping);")


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/order", methods=("GET", "POST"))
def order():
    if request.method == "POST":
        new_order = {
            "name": request.form["name"],
            "drink": request.form["drink"],
            "flavor": request.form["flavor"],
            "topping": request.form["topping"],
        }
        save_order(new_order)
        return render_template("print.html", new_order=new_order)

    return render_template("order.html")


@app.route("/list", methods=["GET"])
def list():
    orders = get_orders()

    return render_template("list.html", orders=orders)
