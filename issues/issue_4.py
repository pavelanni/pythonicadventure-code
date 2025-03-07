drinks = ("Chocolate", "Coffee", "Decaf")
z = 1
for d in drinks:
    print(z, d)
    z = z + 1
drink = input ("Please enter your drink: ")
flavours = ("Caramel", "Chocolate", "Peppermint", "Raspberry", "Plain")
z = 1
for f in flavours:
    print(z, f)
    z = z + 1
flavour = input ("Please enter your flavour: ")
toppings = ("Chocolate", "Cinnamon", "Caramel")
z = 1
for t in toppings:
    print(z, t)
    z = z + 1
topping = input ("Please enter your topping: ")

print("Here is your order: ")
print("Main product: ", drinks[int(drink) - 1])
print("Flavour: ", flavours[int(flavour) - 1])
print("Topping: ", toppings[int(topping) - 1])
print("It's Always A Pleasure Serving You!")