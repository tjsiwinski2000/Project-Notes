import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
width_value=600
start_x_position= (width_value * -1)/2 +20
finish_x_position =start_x_position * -1 -10
screen.setup(width=width_value,height=400)

user_bet=screen.textinput(title="Make your bet", prompt="Which Turtle will win the race? Enter a color: ")
colors=["red","orange","yellow","green","blue","purple"]
y_positions = [ -70, -40,-10,20,50, 80]
all_turtles=[]

y_pos_start=-70
for turtle_index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=start_x_position, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > finish_x_position:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner.")


        rand_distance = random.randint(0,20)
        turtle.forward(rand_distance)
        # 1016-2025 making sure red wins, oddly doesn't work...
        if turtle.pencolor == 'red':
            turtle.forward(100)


screen.exitonclick()