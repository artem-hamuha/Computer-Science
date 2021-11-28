print('''
*******************************************************************************
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
print("Welcome to Treasure Island")
print("Your decisins will shape the story, survive and find the treasure or die.")

direction = input("You open your eyes and find yourself on an island where do you go. Left, right, or straight are your choices: ").lower()

if direction == "left":
    choice = input("""You end up finding a little hut with 3 doors\nthe red door\nthe blue door\nthe green door. Choices are:\nthe red door\nthe blue door\nthe green door - """).lower()
    if choice == "the read door":
        print("You got killed by a withch.")
        print("Game Over: You Lose.\n Thank You For Playing!\nGoodbye.")
    if choice == "the blue door":
        print("You walked in but, suddenly fell into a pit. You tryed to get out but, there was no way. You died of thirst.")
        print("Game Over: You Lose.\n Thank You For Playing!\nGoodbye.")
    if choice == "the green door":
        print("You walked in and found a treasure chest.")
        print("Game Over: You Win.\n Thank You For Playing!\nGoodbye.")
if direction == "right":
    print("You wanderd for 3 days and died of thirst.")
    print("Game Over: You Lose.\n Thank You For Playing!\nGoodbye")
if direction == "straight":
    print("You enter the jungle. A Grizly Bear attacks you; running is not a choice because its to fast. What will you do: stick, fighting skills, play dead - ").lower()
    if choice == "stick":
        print("You died. No stick can over power a bear.")
        print("Game Over: You Lose.\n Thank You For Playing!\nGoodbye")
    if choice == "fighting skills":
        print("You died. Your fighting skills are impressive but, they cant overpower a bear.")
        print("Game Over: You Lose.\n Thank You For Playing!\nGoodbye")
    if choice == "play dead":
        print("You died. The bear was really hungry and ate you.")
        print("Game Over: You Lose.\n Thank You For Playing!\nGoodbye")
else:
    print("That is not one of the choices. Play by the rules.\n Game Over: You Lose.")
    

