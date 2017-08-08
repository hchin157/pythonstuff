from turtle import *
import math

# Name your Turtle.
t = Turtle()

### Write your code below:
setup(600,400)

diamond = 10
#Diamonds are forever!
while diamond == 10:
    colormode(255)

    redString = input("Enter red value:")
    a = int(redString)
    greenString = input("Enter green value:")
    b = int(greenString)
    blueString = input("Enter blue value:")
    c = int(blueString)
    pencolor(a,b,c)

    count = 0
    sidesString = input("Enter the number of sides:")
    x = int(sidesString)

    fillcolor(a,b,c)
    begin_fill()
    while (count<x):
        forward(50)
        left(360 / x )
        count += 1
    end_fill()

# Close window on click.
exitonclick()
