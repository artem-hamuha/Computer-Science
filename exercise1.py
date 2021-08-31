import random

def base():
    print("Enter [1] to get a random 3 digit number")
    print("Enter [2] to exit the program")
    
base()
option = int(input(""))
        
while option != 0:
    if option == 1:
        print(random.randrange(100, 999))
    elif option == 2:
        print("Thank you for using the program. Goodbye.")
        break
    else: 
        print("Invalid option, try again")
    
    print()
    base()
    option = int(input(""))
