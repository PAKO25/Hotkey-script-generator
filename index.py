import time
import json
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
mouse = MouseController()
keyboard = KeyboardController()


koraki = []

print("Make sure your script is in the same directory and named script.json!")
save = int(input("Hello! Have you already written a script and want to import it (1) or do you want to write a new one(0)?"))
if (save == 1):
    with open('script.json', 'r') as f:
        koraki = json.load(f)
else:
    print("OK, here are the rules for creating a script: \n")
    print("If you want to press a certain letter, just write it down and press enter.")
    print("If you want to hold a key, write it after the command 'hold' (hold <key_to_hold>) and press enter. \n")
    print("If you want to move the mouse cursor, do it like: move <relative/absolute> <x> <y>")
    print("If you want to press/hold your mouse do it like: mouse <press/hold> <left/right/middle>")
    print("If you want to get the coords of you cursor use the command 'coords' and wait for 5 seconds (so you have time to move your cursor). \n")
    print("And lastly if you want the program to halt for a certain amount of seconds: wait <seconds>")
    print("When you are done writing your script stop writing it with the keyword 'end'.")



    nadaljuj = True 
    while nadaljuj:
        push = input("Enter a new command: ")
        push = push.split(" ")
        if (push[0] == "end"):
            nadaljuj = False
        elif (push[0] == "coords"):
            time.sleep(5)
            print(mouse.position)
        else:
            koraki.append(push)


    print('\n' * 150)
    print ("yes(1)    no(0)")
    save = int(input("Do you want to save the script you just wrote?"))
    if (save == 1):
        with open('script.json', 'w') as f:
            json.dump(koraki, f)
            print("Your script was saved in script.json")
            time.sleep(2)


def execute():
    for ukaz in koraki:
        match ukaz[0]:

            case "wait":
                time.sleep(int(ukaz[1]))

            case "hold":
                keyboard.press(ukaz[1])

            case "mouse":
                button = Button.left
                if (ukaz[2] == "right"):
                    button = Button.right
                elif (ukaz[2] == "middle"):
                    button = Button.middle
                if (ukaz[1] == "press"):
                    mouse.press(button)
                    mouse.release(button)
                else:
                    mouse.press(button)
            
            case "move":
                if (ukaz[1] == "relative"):
                    mouse.move(int(ukaz[2]), int(ukaz[3]))
                else:
                    mouse.position = (int(ukaz[2]), int(ukaz[3]))
                    
            case _:
                keyboard.press(ukaz[0])
                keyboard.release(ukaz[0])

    execute()



print('\n' * 150)
print("The program will start in 10 seconds.")
time.sleep(3)
execute()