from turtle import Turtle

parts_loc = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
    
    def create_snake(self):
        for i in parts_loc:
            snake = Turtle("square")
            snake.up()
            snake.color("green")
            snake.goto(i)
            self.snake_body.append(snake)

    def move(self):
        for i in range(2, 0, -1):
            place = self.snake_body[i - 1]
            snake = self.snake_body[i]
            snake.goto(place.pos())
    
        self.head.fd(20)
    
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

