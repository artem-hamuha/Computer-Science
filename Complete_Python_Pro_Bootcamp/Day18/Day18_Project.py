#hursed painting
from turtle import Turtle
import colorgram

colors = colorgram.extract("image.jpg", 6)
print(colors)

pen = Turtle()