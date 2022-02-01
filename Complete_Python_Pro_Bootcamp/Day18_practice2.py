from turtle import Turtle
from turtle import Screen
import random

pen = Turtle()
pen.ht()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
pen.pensize(15)
pen.speed(10)


for i in range(10000):
    pen.color(random.choice(colours))
    pen.right(random.choice(directions))
    pen.fd(30)


window = Screen()
window.exitonclick()