import colorgram
from turtle import Turtle, Screen
import random


def get_colors(image):
    colors = colorgram.extract(image, 10)
    colors_rgb = []
    for color in colors:
        colors_rgb.append((color.rgb[0], color.rgb[1], color.rgb[2]))
    return colors_rgb


my_colors = get_colors("dots.jpeg")
print(my_colors)

my_turtle = Turtle()
screen = Screen()
screen.colormode(255)

position_y = -300
for _ in range(10):
    my_turtle.penup()
    position_y += 50
    my_turtle.goto(-400, position_y)
    for _ in range(10):
        my_turtle.dot(20, random.choice(my_colors))
        my_turtle.penup()
        my_turtle.forward(50)
        my_turtle.pendown()


screen.exitonclick()


