import random

name = input("What is your name? ")

print("Good Luck ! ", name)

repeat = True
while repeat == True :
    fruits =  ['apple', 'olive', 'tomato', 'melon', 'litchi', 
    'mango', 'lime', 'kiwi', 'grapes', 'cherry',
    'banana', 'apricot', 'cucumber', 'guava', 'mulberry',
    'orange', 'papaya', 'pear', 'peach', 'berry']

    animals = ['ants', 'hippo', 'panda', 'giraffe', 'bat', 'bear',
    'catfish', 'cheetah', 'lizard', 'wolf', 'zebra', 'eagle',
    'cobra', 'goose', 'penguin', 'frog', 'mouse', 'flamingo',
    'rabbit', 'crow', 'whale', 'lion', 'monkey', 'ostrich',
    'peacock', 'raccoon', 'rhinoceros', 'sheep', 'dogs',
    'squirrel', 'tiger', 'vulture']

    accessories = ['ring', 'bangle', 'lipstick', 'handbag', 'crown',
    'necklace', 'watch', 'caps', 'glasses', 'wallet',
    'belts', 'comb', 'pendent', 'earring', 'scarf',
    'backpack', 'keychain', 'hairpin', 'shoes', 'hats',
    'jacket', 'boots', 'socks', 'stocking', 'muffler',
    'gloves', 'umbrella', 'ribbon']

    stationary = ['notebook', 'tape', 'pencil', 'eraser', 'sharpener',
    'files', 'fevicol', 'inkpot', 'chalk', 'duster',
    'glue', 'paper', 'cutter', 'chart', 'colours',
    'stapler', 'marker', 'staples', 'clips', 'calculator',
    'envelope', 'register']

    words = fruits + animals + accessories + stationary
    word = random.choice(words)
    print("Your word has", len(word), "letters.")

    print()

    if word in fruits:
        print("Your word is a Fruit.")
    elif word in accessories:
        print("Your word is related to Accessory.")
    elif word in stationary:
        print("Your word is related to Stationary.")
    elif word in animals:
        print("Your word is an Animal")
    print("Guess the characters")

    guesses = ''

    turns = 5

    while turns > 0:

        failed = 0

        for char in word:

            if char in guesses:
                print(char)

            else:
                print("_")

                failed += 1

        if failed == 0:
          
            print("You Win")


            print("The word is: ", word)
            break

        guess = input("guess a character:")

        guesses += guess

        if guess not in word:

            turns -= 1

            print("Wrong")

            print("You have", + turns, 'more guesses')

            if turns == 0:
                print("You Loose")
                play_again = input("Would you like to play again? Type Y for yes and N for No!")
                if play_again == "N":
                    repeat = False