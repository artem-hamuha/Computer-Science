#rock paper scissors game
import random

rock = '''
    _______
---'      (____)
          (______)
          (_______)
          (_______)
---.______(_____)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#3 rules
#rock beats scissors
#scissors beats paper
#paper beats rock

move = int(input("Welcome to Rock, Paper, Scissors!\nChoose your move: enter 0 for rock, 1 for paper, 2 for scissors - "))
moves = [rock, paper, scissors]

comp_move = random.randint(0, 2)

print(moves[move])
print(f"\nComputer move:\n{moves[comp_move]}")

if moves[move] == rock and moves[comp_move] == scissors:
    print("You win!")
elif moves[comp_move] == rock and moves[move] == scissors:
    print("You Lose!")
elif moves[move] == scissors and moves[comp_move] == paper:
    print("You Win!")
elif moves[comp_move] == scissors and moves[move] == paper:
    print("You Lose!")
elif moves[move] == paper and moves[comp_move] == rock:
    print("You Win!")
elif moves[comp_move] == paper and moves[move] == rock:
    print("You Lose!")
else:
    print("You tied!")