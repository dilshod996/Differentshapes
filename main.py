import turtle
from turtle import Turtle
from random import choice

miny = Turtle()
miny.shape("arrow")
color = ["black", "green", "purple", "yellow", "blue", "red"]



def drawing_shape(number_of_sides):
    angle = 360 / number_of_sides
    for x in range(number_of_sides):

        miny.forward(100)
        miny.right(angle)


for side in range(3, 11):
    miny.color(choice(color))
    drawing_shape(side)


turtle.exitonclick()
