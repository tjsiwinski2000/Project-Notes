from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#set up a screen
screen = Screen()
screen.setup()
screen.setup(width=800, height = 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

#draw the net
net = Turtle()
net.penup()

net.goto(0,450)
net.setheading(270)
net.forward(20)
net.color("white")
net.hideturtle()

for _ in range(20):
    net.pendown()
    net.forward(22)
    net.penup()
    net.forward(22)

# paddle section
r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_delay)
    screen.update() #turns on animation *after* screen is set up
    ball.move()
    #detect collision
    if ball.ycor() >280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with r_paddle or l_paddle
    if ball.xcor() > 320 and ball.distance(r_paddle)< 50  or ball.xcor() < -320 and ball.distance(l_paddle) <50:
        #increase ball speed by reducing delay
        ball.ball_delay *= .80
        print(f"ball delay {ball.ball_delay}")
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.score_left +=1
        scoreboard.update_scoreboard()


    #Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.score_right += 1
        scoreboard.update_scoreboard()


screen.exitonclick()