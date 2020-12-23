from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

#Challenge 1
for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)

#Challenge 2
timmy_the_turtle.goto(100,-100)
for _ in range(10):
    timmy_the_turtle.forward(5)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(5)
    timmy_the_turtle.pendown()

#Challenge 3
timmy_the_turtle.goto(-200,-100)
for sides in range(3,11):
    angle = 360 / sides
    for _ in range(sides):
        timmy_the_turtle.right(angle)
        timmy_the_turtle.forward(100)

screen = Screen()
screen.exitonclick()