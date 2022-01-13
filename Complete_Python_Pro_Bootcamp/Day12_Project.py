import random
import os

logo = """   _____                                _______   _                _   _                       _                   
  / ____|                              |__   __| | |              | \ | |                     | |                  
 | |  __   _   _    ___   ___   ___       | |    | |__     ___    |  \| |  _   _   _ __ ___   | |__     ___   _ __ 
 | | |_ | | | | |  / _ \ / __| / __|      | |    | '_ \   / _ \   | . ` | | | | | | '_ ` _ \  | '_ \   / _ \ | '__|
 | |__| | | |_| | |  __/ \__ \ \__ \      | |    | | | | |  __/   | |\  | | |_| | | | | | | | | |_) | |  __/ | |   
  \_____|  \__,_|  \___| |___/ |___/      |_|    |_| |_|  \___|   |_| \_|  \__,_| |_| |_| |_| |_.__/   \___| |_|
"""

yes_no = ["yes", "no"]

easy_hard = ["easy", "hard"]

def game():

    game_over = False

    while not game_over:
        print(logo)
        print("\nI am thinking of a number between between 0 and 100")
        dificulty = input("\nSelect Dificulty: Easy or Hard\n").lower()
    
        while dificulty not in easy_hard:
            print("\nInvalid Input")
            dificulty = input("\nSelect Dificulty: Easy or Hard\n").lower()
    
        if dificulty == "easy":
            attempts = 10
        elif dificulty == "hard":
            attempts = 5

        num = random.randint(0, 100)  

        while attempts != 0:
            guess = int(input("\nTake a guess\n"))

            if attempts == 0:
                print("\nYou have run out of attempts\nYou Lose")
            if guess == num:
                attempts -= 1
                print(f"\nThats right I was thinking of {num}")
                attempts = 0
            if guess != num:
                attempts -= 1
                print("\nWrong guess")
                if guess > num:
                    print("\nToo High")
                if guess < num:
                    print("\nToo Low")
                print(f"\nYou have {attempts} attempts left")
            
        
        game_over = input("\nWould you like to play again: Yes or No\n").lower()

        while game_over not in yes_no:
            print("\nInvalid Input")
            dificulty = input("\nWould you like to play again: Yes or No\n").lower()
    
        if game_over == "yes":
            game_over = False
            if os.name == "nt":
                command = 'cls'
            os.system(command)
        else:
            game_over = True

game()
