import random
 
someWords = "apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon"
 
someWords = someWords.split(' ')

word = random.choice(someWords)

tries = len(word) + 2
prompt = ["_" for x in word]
word_prompt = [i for i in word]

while tries != 0:
    print(prompt, "\n")
    guess = input("Try to guess a letter or word\nHINT the word is a fruit\n")

    if word == guess:
        print(f"Congrats, you win!\nThe word was {word}")
        tries = 0

    else:
        for i in word_prompt:
            if i == guess:
                prompt[word_prompt.index(i)] = guess

        if guess not in prompt:
            print(prompt, "\n")
            print("The letter wasnt found\n")
            tries -= 1
            if tries == 0:
                print(f"You lose!\nThe word was {word}")
        
        else:
            print(prompt, "\n")
            print("Here is where your letter was found\n")