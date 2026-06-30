import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

my_player=Player()
screen.listen()
screen.onkey(my_player.go_up,"Up")

my_car_mamager = CarManager()
my_scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    my_car_mamager.create_car()
    my_car_mamager.move_cars()

    #Detect Collision
    for car in my_car_mamager.all_cars:
        if my_player.distance(car) < 20:
            my_scoreboard.game_over()
            game_is_on = False

    #Detect Succesful Turtle Crossomg
    if my_player.is_at_finish_line():
        my_player.go_to_start()
        my_car_mamager.level_up()
        my_scoreboard.increase_score()

    screen.update()

screen.exitonclick()
