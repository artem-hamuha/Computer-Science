import random

def number_guessing(a: int, b: int):
    tries = 10
    ran_num = random.randint(a, b)
    guess = None

    while tries > 0 and guess != ran_num:
        guess = int(input("Guess The Number\n\n"))

        if guess > ran_num:
            tries -= 1
            if tries == 0:
                print(f"\nYou lose as you ran out of tries!\nThe number was {ran_num}.")
            else:
                print("\nTry something less\n")

        if guess < ran_num:
            tries -= 1
            if tries == 0:
                print(f"\nYou lose as you ran out of tries!\nThe number was {ran_num}.")
            else:
                print("\nTry something more\n")

        if guess == ran_num:
            print(f"\nWith {tries} guesses remaining you win, the number was {ran_num}!")

number_guessing(0, 100)

