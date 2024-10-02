
import random
from turtle import *

# Screen

Screen()
title("Eid Mubarak !")
window_width()
window_height()
bgcolor('black')
hideturtle()
speed(0)


def Star_turtle(x, y):
    # Star
    import random
    penup()
    goto(x, y)
    colour = ['blue', 'red', 'white', 'green', 'gold', 'maroon', 'violet', 'magenta', 'purple', 'navy',
              'skyblue', 'cyan', 'turquoise', 'lightgreen', 'darkgreen', 'chocolate', 'brown', 'gray']
    j = random.randrange(0, 18)
    color(colour[j])
    pendown()
    forward(14)
    right(135)
    forward(12)
    right(145)
    forward(16)
    right(155)
    forward(16)
    right(145)
    forward(16)
    up()
    goto(0, 0)
    down()


def Moon_turtle():
    # Moon
    up()
    bgcolor('black')
    goto(0, 0)
    goto(-100, 20)
    begin_fill()
    color('white')
    circle(100)
    end_fill()

    up()
    goto(-90, 20)
    begin_fill()
    color('black')
    circle(96)
    end_fill()


def Write_turtle():
    color('white')
    penup()
    goto(-96, 41)
    pendown()
    write("Eid Mubarak", font=("Courier", 24, "normal"))


if __name__ == "__main__":
    for i in range(15):
        x = random.randrange(-250, 250, 20)
        y = random.randrange(-250, 250, 15)
        j = random.randrange(0, 18)
        Star_turtle(x, y)
    Moon_turtle()
    Write_turtle()

exitonclick()
