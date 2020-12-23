from turtle import Turtle, Screen
import random

my_turtle = Turtle()

my_angle = 0
colors = ("blue", "dark orange", "red", "chartreuse", "medium purple", "magenta")

while my_angle != 360:
    my_turtle.pencolor(random.choice(colors))
    my_turtle.setheading(my_angle)
    my_turtle.circle(50)
    my_angle += 10





screen = Screen()
screen.exitonclick()