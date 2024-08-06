import msvcrt

options = ['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Exit']

control = True
while control:
    print("Select an option:")
    for i in range(len(options)):
        print(i + 1, options[i])
    print("Please select the option by number: ", end="")
    keypress = msvcrt.getch()
    print(keypress)
    input()