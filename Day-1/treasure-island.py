print(
    '''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = (input("You are at a crossroad, where do you want to go left or right?\n")).lower()

if direction == "left":
    travel = input("You have come to the lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat or type 'swim' to siwm across.\n").lower()
    if travel == "wait":
        door = input("You have arrived at the island unharmed. There is a house with 3 doors. Which door you want to enter through - Red, Yellow or Blue?\n").lower()
        if door == "yellow":
            print("Yeyy, you found the Treasure! You win!")
        elif door == "blue":
            print("You have entered the room of Beasts, Game over!")
        elif door == "red":
            print("You have entered the room of Fire, Game over!")
    else:
        print("You got attached by angry trout. Game over!")
else:
    print("You fell into a hole. Game over!")