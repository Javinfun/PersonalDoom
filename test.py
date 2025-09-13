import turtle
screen = turtle.Screen()
screen.setup(1280, 720, startx=100, starty=100)

t = turtle.Turtle()
turtle.bgcolor('black')
turtle.color('yellow')
turtle.speed(1)
turtle.right(90)

turtle.circle(100)
if (turtle.right(0)):
    turtle.right(45)