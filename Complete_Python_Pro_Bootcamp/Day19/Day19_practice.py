import turtle as t

pen = t.Turtle()




window = t.Screen()
window.listen()

def move():
    pen.fd(5)

window.onkey(move, "w")
window.exitonclick()