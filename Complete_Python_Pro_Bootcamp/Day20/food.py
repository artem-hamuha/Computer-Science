from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(.4, .4)
        self.color("red")
        self.penup()
        self.speed("fastest")
        self.goto(random.randint(-290, 290), random.randint(-290, 290))

    def respawn(self):
        self.goto(random.randint(-290, 290), random.randint(-290, 290))
