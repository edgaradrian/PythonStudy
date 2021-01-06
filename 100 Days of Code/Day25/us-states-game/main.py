import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct", prompt="What's another state's name").capitalize()
    data_states = pandas.read_csv("50_states.csv")
    all_states = data_states["state"].to_list()
    print(all_states)

    if answer_state in all_states:
        guessed_states.append(answer_state)
        turtle = turtle.Turtle()
        turtle.hideturtle()
        turtle.penup()
        state = data_states[data_states["state"] == answer_state]
        turtle.goto(int(state["x"]), int(state["y"]))
        turtle.write(answer_state)


screen.exitonclick()