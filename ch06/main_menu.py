def main_menu():
    while True:
        order = get_order()
        print("Check your order:")
        print_order(order)
        confirm = input("Confirm? Press Y to confirm, N to cancel: ")
        if confirm == "Y" or confirm == "y":
            save_order(order)
            print("Thanks for your order:")
            print_order(order)
        else:
            continue


def get_order():
    return {}


def print_order(order):
    print(order)
    return


def save_order(order):
    print("Saving order...")
    return


main_menu()
