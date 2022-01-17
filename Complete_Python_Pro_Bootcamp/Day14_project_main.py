from Day14_project_data import data, logo, vs
import random
import os

higher_lower = ["higher", "lower"]

game_over = False
while not game_over:
    p1 = random.choice(range(0, len(data)))
    p2 = random.choice(range(0, len(data)))
    while p1 == p2:
        p2 = random.choice(range(0, len(data)))

    p1_ = data[p1]
    p2_ = data[p2]   

    print(logo)
    print(f"Who has more foloowers on Instagram\n{p1_}\n{vs}\n{p2_}")
    game_over = True
    