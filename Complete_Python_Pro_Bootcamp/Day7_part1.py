import random
#Things to do to make hangman game

#auto pick random word
word_list = ["richard", "apple", "misconception"]
chosen_word = random.choice(word_list)
#adding lives and keeping track of them
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = range(len(stages))

#for testing purposes
print(f"Hint, {chosen_word} is the chosen word")

#ask for letter input
letter = input("Enter letter - ").lower()


#check if letter in word and loop game
display = []
for _ in range(len(chosen_word)):
    display += "_"

game_over = False
while game_over == False:
    if lives == 0:
        print(stages[lives])
        print("Game Over, You Lose!")
        game_over = True

    elif letter == chosen_word:
        print(f"It is {chosen_word}, you win!")
        
    else:
        count = 0
        for l in chosen_word:
            if l == letter:
                display[count] = letter
                count += 1
            else:
                count += 1
        

