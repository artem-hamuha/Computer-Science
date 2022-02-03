#hursed painting
from turtle import Screen, Turtle
import turtle as t
import random

colors = [[160, 160, 160], [255, 119, 60], [127, 0, 255], [255, 0, 255], [32, 32, 32]]

t.colormode(255)
pen = Turtle()
pen.ht()
pen.speed('fast')
pen.penup()
pen.goto(-125, -25)
pen_location = [-125, -25]

for i in range(0, 10):
    pen_location[1] += 25
    pen.goto(pen_location)
    for i in range(0, 10):
        r_color = random.choice(colors)
        pen.color(r_color)
        pen.dot(20)
        pen.fd(25)




screen = Screen()
screen.exitonclick()