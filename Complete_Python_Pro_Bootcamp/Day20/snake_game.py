from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

parts_loc = [(0, 0), (-20, 0), (-40, 0)]

snake_body = []

for i in parts_loc:
    snake = Turtle("square")
    snake.up()
    snake.color("green")
    snake.goto(i)
    snake_body.append(snake)

screen.update()

game_on = True

while game_on:
    screen.update()
    time.sleep(.1)
    for i in range(2, 0, -1):
        place = snake_body[i - 1]
        snake = snake_body[i]
        snake.goto(place.pos())
    
    snake_body[0].fd(20)



screen.exitonclick()