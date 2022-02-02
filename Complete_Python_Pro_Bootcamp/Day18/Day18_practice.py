from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.shape("triangle")

my_turtle.color("cyan")
my_turtle.pencolor("blue")

#square
my_turtle.fd(150)
my_turtle.left(90)
my_turtle.fd(150)
my_turtle.left(90)
my_turtle.fd(150)
my_turtle.left(90)
my_turtle.fd(150)

#dashed line
for i in range(8):
     my_turtle.fd(10)
     my_turtle.pu()
     my_turtle.fd(10)
     my_turtle.pd()

#square to decagon
def draw_figure(turtle, sides):
    angle = 360/ sides
    for i in range(0, sides):
        turtle.fd(100)
        turtle.right(angle)

i = 4
while i <= 10:
    draw_figure(my_turtle, i)
    i += 1




screen = Screen()
screen.exitonclick()