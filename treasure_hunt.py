print("Welcome to the treasure island ")
print("Your mission is to find the treasure.")
path=input("Now are in the middle of the island ... There are two path in front of you .... You must choose 'left' or 'right' ?      ")
if path == "left":
    print(" Congrats!! You reached the river ")
    choice = input(" To reach other side of the river .. You wish to swim or you wait for the boat....type 'wait' or 'swim'    ")
    if choice == "wait":
        print("You reached the other side safely !")
        door = input(
            "There are three doors in front of you .. Red ,Blue and Violet... Now you have to choose the correct door to find treasure....type 'red' , 'blue' and 'violet'    ")
        if door=="red":
            print("You are a food to the hungry Lion ")
            print("Gme over!!")
        elif door == "blue":
            print("Congratulations!! You found the treasure")
        else:
           print("You enter the room full of poison!")
           print("Game over!!")
    else:
        print("Ohh No!! You are swept away by the current flow of the river ")
        print("Game over!!")
else:
    print("You fell into the hole")
    print("Game over!!")

