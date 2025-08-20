import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

turtle = turtle.Turtle()
turtle.hideturtle()
turtle.penup()

data = pandas.read_csv("50_states.csv")
list_of_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"Guess the State {len(guessed_states)}/50", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break
    if answer_state in list_of_states:
        guessed_states.append(answer_state)
        turtle.goto(data[data.state == answer_state].x.item(), data[data.state == answer_state].y.item())
        turtle.write(answer_state)


states_to_learn = data[data.isin(guessed_states).state == False]
states_to_learn.to_csv("states_to_learn.csv")