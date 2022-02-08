from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 450)
screen.bgcolor("black")

t_colors = ["red", "yellow", "blue", "white", "green"]
y_cords = [-60, -20, 20, 60, 100]
all_turtles = []

for index in range(5):
    pen = Turtle()
    pen.speed("slowest")
    pen.shape("turtle")
    pen.up()
    pen.color(t_colors[index])
    pen.goto(-225, y_cords[index])
    all_turtles.append(pen)

ways_to_move = random.randint(1, 10)

user_bet = int(screen.textinput("Make your bet.", "Bet: "))

while not user_bet:
    user_bet = int(screen.textinput("No bet entered", "Bet: "))

user_turtle = screen.textinput("Pick your turtle.", "Turtle color: ").lower()

while user_turtle not in t_colors:
    user_turtle = screen.textinput("Turtle not found.", "Turtle color: ").lower()

race_on = True

while race_on:
    for turtle in all_turtles:

        if turtle.xcor() > 240:

            if user_turtle == turtle.pencolor():
                print(f"{turtle.pencolor().title()} turtle wins!\nYou win {user_bet * 2}$!")
                race_on = False
            
            else:
                print(f"{turtle.pencolor().title()} turtle wins!\nYou lose {user_bet}$!")
                race_on = False

        r_distance = random.randint(1, 10)
        turtle.forward(r_distance)
    


    

screen.exitonclick()

