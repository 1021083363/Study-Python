import uturtle

turtle = uturtle.Turtle()

def rect(x, y, color, x2, y2):
    width = abs(x2 - x)
    height = abs(y2 - y)
    turtle.pencolor(color)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.fillcolor(color)
    # turtle.color(color, color)
    turtle.begin_fill()
    turtle.fd(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.end_fill()

def france():
    rect(-120, 160, 'black', 120, -160)
    rect(-75, 50, 'blue', -25, -50)
    rect(-25, 50, 'white', 25, -50)
    rect(25,  50, 'red', 75,   -50)

turtle.clear()
turtle.speed(0)
#turtle.delay(0)
france()
