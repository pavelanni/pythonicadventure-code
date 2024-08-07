import msvcrt
import os

options = ['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Exit']
control = True
currentOption = 0

def printMenu(title, choices, currentOption):
    print(title)
    print(len(title) * "-")
    for i in range(len(choices)):
        if (currentOption == i) :
            print("->", i + 1, choices[i])
        else: 
            print("  ",i + 1, choices[i])
    print("Move arrow keys to select, press Enter to confirm:")

def checkKeyPress(key): 
    if key == b'\xe0': # Arrow key
        key = msvcrt.getch()
        if key == b'H':	# Up arrow
            return -1
        elif key == b'P':	# Down arrow
            return 1
    elif key == b'\r': # Enter key
        return False
    return 0


while control:
    os.system('cls')  # Clear the consol
    printMenu("Main Menu", options, currentOption)
    keypress = msvcrt.getch()
    validKeyPress = checkKeyPress(keypress)

    if validKeyPress is not False:
        currentOption = currentOption + validKeyPress
        if currentOption < 0:
            currentOption = len(options) - 1
        elif currentOption >= len(options):
            currentOption = 0
    else: 
        if currentOption == len(options) - 1:
            control = False
        else:
            print("You selected:", options[currentOption])
            os.system('pause')
    
    

