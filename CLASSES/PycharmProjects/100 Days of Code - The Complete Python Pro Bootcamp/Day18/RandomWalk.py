import random
import turtle

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rcolor =  (r, g, b)
    return rcolor

DIRECTION_LIST=[0,90,180,270]

tim=turtle.Turtle()
turtle.colormode(255)

for _ in range(200):
    tim.speed(10)
    tim.width(8)
    tim.color(random_color())
    tim.forward(28)
    angle = random.choice(DIRECTION_LIST)
    tim.setheading(angle)


screen=turtle.Screen()
screen.exitonclick()