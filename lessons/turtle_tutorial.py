"""Turtle tutorial"""

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
bob: Turtle = Turtle()

leo.penup()
leo.goto(-200,200)
leo.pendown()

i: int = 0
while (i < 3):
    leo.forward(400)
    leo.right(120)
    i += 1
done()


