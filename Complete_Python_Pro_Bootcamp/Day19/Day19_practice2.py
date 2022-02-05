from turtle import Turtle, Screen

pen = Turtle()
pen.speed("normal")

def fd():
    pen.fd(5)

def back():
    pen.back(5)

def right():
    pen.right(5)

def left():
    pen.left(5)

def clear():
    pen.clear()
    pen.up()
    pen.home()
    pen.down()

screen = Screen()
screen.listen()

screen.onkeypress(fd, "w")
screen.onkeypress(back, "s")
screen.onkeypress(right, "d")
screen.onkeypress(left, "a")
screen.onkey(clear, "v")

screen.exitonclick()