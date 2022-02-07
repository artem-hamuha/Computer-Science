from turtle import Turtle, Screen, screensize

pen = Turtle()
screen = Screen()
screen.setup(500, 450)
screen.bgcolor("black")

t_colors = ["red", "yellow", "blue", "brown", "green"]

pen.speed("normal")
pen.shape("turtle")
pen.up()
pen.color("red")

pen2 = pen.clone()
pen2.color("blue")

pen3 = pen.clone()
pen3.color("yellow")

pen4 = pen.clone()
pen4.color("brown")

pen5 = pen.clone()
pen5.color("green")

pen.goto(-225, -60)
pen2.goto(-225, -20)
pen3.goto(-225, 20)
pen4.goto(-225, 60)
pen5.goto(-225, 100)

user_bet = screen.textinput("Make your bet.", "Amount of money: ")
user_turtle = screen.textinput("Pick your turtle.", "Turtle color: ")

while user_turtle not in t_colors:
    user_turtle = screen.textinput("Turtle not found.", "Turtle color: ")



screen.exitonclick()

