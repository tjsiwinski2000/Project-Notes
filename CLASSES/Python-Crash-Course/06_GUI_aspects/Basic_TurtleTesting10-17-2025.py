import turtle 
import time

tim=turtle.Turtle()
tim.shape("turtle")
tim.color("dark turquoise")
tim.speed(0)

screen=turtle.Screen()

headings=[90,180,270,0]

for heading in headings:
  tim.setheading(heading)
  time.sleep(2)

screen.exitonclick()