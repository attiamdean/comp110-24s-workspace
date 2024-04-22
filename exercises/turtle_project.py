"""Turtle drawing program."""

"""TODO: Describe your scene program."""
 
__author__ = "730607182"
 
from turtle import Turtle, colormode, done 
 
 
def main() -> None:
    """The entrypoint of my scene."""
    # TODO: Declare your Turtle variable(s) here.
    don: Turtle = Turtle()
    # TODO: Call the procedures you define and pass your Turtle(s) as an argument.
    draw_a_star(don, 0.0, 0.0, 100.0)
    done()
 
# TODO: Define the procedures for other components in your scene here.
def draw_a_star(a_turtle: Turtle, x: float, y: float, line_length: float) -> None:
    # move to the starting location
    a_turtle.penup()
    a_turtle.goto(x,y)
    a_turtle.pendown()
    a_turtle.left(30)
    # draw the star
    i: int = 0
    while i < 5:
        a_turtle.forward(line_length)
        a_turtle.left(144.25)
        i += 1

main()




 
# TODO: Use the __name__ is "__main__" idiom shown in class