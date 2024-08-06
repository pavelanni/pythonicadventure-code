import msvcrt
import os

options = ['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Exit']

control = True
currentOption = 0	# Default Current selected option
while control:
    os.system('cls')  # Clear the consol
    print("Select an option:")
    for i in range(len(options)):
        if (currentOption == i) :
            print("->", i + 1, options[i])
        else:
            print("  ", i + 1, options[i])
    print("Move arrow keys to select, press Enter to confirm:")
    keypress = msvcrt.getch()
    if keypress == b'\xe0':
        keypress = msvcrt.getch()
        if keypress == b'H':	# Up arrow
            currentOption -= 1
            if currentOption < 0:
                currentOption = len(options) - 1
        elif keypress == b'P':	# Down arrow
            currentOption += 1
            if currentOption >= len(options):
                currentOption = 0
    