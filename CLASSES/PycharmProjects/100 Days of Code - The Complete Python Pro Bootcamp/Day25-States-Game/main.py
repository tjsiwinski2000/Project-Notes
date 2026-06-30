#1103-2025
#... this code works [TJ Solution] ... instructor way was CLEANER, see main2.py
import turtle
import pandas
from label import Label

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_label = Label()


#Open 50_states.csv file
states = pandas.read_csv("50_states.csv")

game_on = True
correct_state_count = 0

while game_on:
    answer_state = screen.textinput(title = f"{correct_state_count} /50 States Correct", prompt ="What's another state's name")
    print(answer_state)
    if answer_state == "quit":
        game_on = False
    # Compare user input to panda DataFrame
    selected_state = states[states["state"] == answer_state.title()]
    print(f"count of matches: {selected_state.count().iloc[0]}")
    # If match found, update state label
    if selected_state.count().iloc[0] == 1:
        correct_state_count += 1
        new_x = int(selected_state.x.item())  #.item() returns only the value , preventing error
        new_y = int(selected_state.y.item())
        state_label.update_label(new_x, new_y, answer_state)






# Keep Screen Open , alternative to [screen.exitonclick() ]
turtle.mainloop()

