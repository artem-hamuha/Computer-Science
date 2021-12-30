logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

yes_no = ["yes", "no"]

print(logo)

print("Welcome to the calculator!")

old_num = None

def calculator():   
    while True:
        n1 = int(input("Enter number 1 - "))
        n2 = int(input("Enter number 2 - "))
        operation = input(f"{operations.keys()}\nChoose operation - ")

        while operation not in operations:
            print("Invalid input try again.")
            operation = input(f"{operations.keys()}\nChoose operation - ")

        old_num = operations[operation](n1, n2)
        print(f"{n1} {operation} {n2} = {old_num}")

        choice = input("Would you like to continue [yes/no] - ").lower()
        while choice not in yes_no:
            print("Invalid input, try again.")
            choice = input("Would you like to continue [yes/no] - ").lower()
        if choice == "no":
            print("Ok bye!")
            break
        else:
            pass

        same = input("Would you like to continue with the same number [yes/no] - ").lower()
        while choice not in yes_no:
            print("Invalid input, try again.")
            same = input("Would you like to continue with the same number [yes/no] - ").lower()   
        if same == "yes":
            print(f"Than type {old_num} into the number 1 slot")
        else:
            pass

calculator()

