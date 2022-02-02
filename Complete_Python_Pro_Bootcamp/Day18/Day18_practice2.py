import turtle as t
from turtle import Screen
import random

pen = t.Turtle()
pen.ht()
t.colormode(255)

def r_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

directions = [0, 90, 180, 270]
pen.pensize(15)
pen.speed(10)

for i in range(10000):
    pen.color(r_color())
    pen.right(random.choice(directions))
    pen.fd(30)


window = Screen()
window.exitonclick()