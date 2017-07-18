from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
#setup(500,300)
#x_pos = -250
#y_pos = -150
#t.setposition(x_pos, y_pos)

### Write your code below:
setup(600,400)
x_pos = -100
y_pos = 0
t.setposition(x_pos, y_pos)
x_pos = -100
y_pos = 100
t.setposition(x_pos, y_pos)
x_pos = 0
y_pos = 100
t.setposition(x_pos, y_pos)
x_pos = 0
y_pos = 0
t.setposition(x_pos, y_pos)
penup()
forward(100)
pendown()
colormode(255)
pencolor(245,230,220)
forward(100)
left(120)
forward(100)
left(120)
forward(100)
left(120)


# Close window on click.
exitonclick()
