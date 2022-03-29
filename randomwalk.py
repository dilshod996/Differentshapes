import turtle
from turtle import Turtle
import random

bully = Turtle()
colors = ["red", "blue", "yellow", "green", "lightblue", "purple", "black"]
destinations = [0, 90, 180, 270]
bully.speed(5)
bully.pensize(7)
lines = 0
while True:
    lines+=1
    if lines <= 100:

        bully.forward(20)
        bully.right(random.choice(destinations))
        bully.color(random.choice(colors))
    else:
        turtle.exitonclick()

