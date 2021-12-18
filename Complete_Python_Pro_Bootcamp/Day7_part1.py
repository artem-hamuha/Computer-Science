import random
#Things to do to make hangman game

#auto pick random word
word_list = ["richard", "apple", "misconception"]

chosen_word = random.choice(word_list)
print(f"Hint {chosen_word} is trhe chosen word")
#ask for letter input
letter = input("Enter letter - ").lower()

#check if letter in word

if letter == chosen_word:
    print(f"it is {chosen_word} you win")
else:
    for l in chosen_word:
        if l == letter:
            print(l)
        else:
            print("-")
