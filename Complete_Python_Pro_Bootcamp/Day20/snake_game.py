from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()

screen.update()
screen.onkeypress(snake.up, "w")
screen.onkeypress(snake.down, "s")
screen.onkeypress(snake.right, "d")
screen.onkeypress(snake.left, "a")

screen.listen()

game_on = True

while game_on:
    screen.update()
    time.sleep(.1)

    snake.move()


screen.exitonclick()