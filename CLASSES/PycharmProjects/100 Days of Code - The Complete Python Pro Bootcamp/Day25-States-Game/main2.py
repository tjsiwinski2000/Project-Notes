#1104-2025 redo state  challenge in instructor way

import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#Open 50_states.csv file
data = pandas.read_csv("50_states.csv")
# .state , use as attribute
state_list = data.state.to_list()

#init variables
game_on = True
FONT = ("Courier", 10, "normal")
guess_states = []
states_to_learn = []

#turtle for label
t = turtle.Turtle()
t.hideturtle()
t.penup()


while len(guess_states) < 50:
    answer_state = screen.textinput(title = f"{len(guess_states)} /50 States Correct", prompt ="What's another state's name")
    print(answer_state)
    if answer_state == "quit":
        break

    # User input a valid state
    answer_state = answer_state.title()
    if answer_state in state_list:
        guess_states.append(answer_state)
        state_data = data[data.state == answer_state]
                #Note state_data.x returns [%index%  %x.value%] why? panda series
        new_x = int(state_data.x.item())  #.item() returns only the value , preventing error
        new_y = int(state_data .y.item())
        #print(answer_state, new_x, new_y)
        t.goto(new_x,new_y)
        t.write(answer_state, font =FONT, align="center")


#states_to_learn.csv
# for item in state_list:
#     if item not in guess_states:
#         states_to_learn.append(item)
states_to_learn = [state for state in state_list if state not in guess_states]

new_data = pandas.DataFrame(states_to_learn)
new_data.to_csv("states_to_learn.csv")
#print(states_to_learn)
