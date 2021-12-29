import turtle 

painter = turtle.Turtle()
screen = turtle.Screen()

screen.bgcolor("black")
painter.pencolor("red")

for i in range(50):
    painter.forward(100)
    painter.left(125)
    
turtle.done()