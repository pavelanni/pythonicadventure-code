drinks = ["chocolate", "coffee", "decaf"]
flavors = ["caramel", "vanilla", "peppermint", "raspberry", "plain"]
toppings = ["chocolate", "cinnamon", "caramel"]

print(drinks)

print("--------------------------------------------")
print("Drinks:")
i = 1
for d in drinks:
    print(i,d)
    i += 1
drinkIndex = int(input("Please select the drink by number: ")) - 1


print("your selected drink is: ", drinks[drinkIndex])
