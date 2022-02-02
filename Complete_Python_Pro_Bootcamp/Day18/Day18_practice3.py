import turtle as t
import random

pen = t.Turtle()
t.colormode(255)
pen.ht()
pen.speed("fastest")

def r_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

on = True

for i in range(0, 5000):
    pen.pencolor(r_color())
    pen.circle(100)
    pen.goto(0, 0)
    pen.left(1)

screen = t.Screen()
screen.exitonclick()