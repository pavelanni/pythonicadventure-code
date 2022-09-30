import json

order = {"name": "Erik", "drink": "coffee", "flavor": "caramel", "topping": "chocolate"}

order1 = {
    "name": "Alex",
    "drink": "chocolate",
    "flavor": "vanilla",
    "topping": "caramel",
}

orders = []

orders.append(order)
orders.append(order1)

f = open("orders.json", "w")
json.dump(orders, f, indent=4)
f.close()

saved_orders = []
f = open("orders.json", "r")
saved_orders = json.load(f)
print(saved_orders)
