import random
import turtle
turtle.colormode(255)
screen=turtle.Screen()

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rcolor =  (r, g, b)
    return rcolor

tim=turtle.Turtle()
tim.shape("turtle")
tim.color("dark turquoise")
tim.speed(0)

# 1013-2025 created random art with circles START
# tim.penup()
# #x_start = screen.window_width() /2 -20
# x_start = 0- screen.window_width() /2  +100
# tim.goto(x_start,0)
# tim.pendown()
#
# for _ in range(100):
#     tim.circle(100)
#     tim.forward(5)
#     tim.color(random_color())
#
# tim.setheading(270)
# tim.forward(-1)
# tim.setheading(180)
#
# for _ in range(100):
#     tim.circle(100)
#     tim.forward(5)
#     tim.color(random_color())
# 1013-2025 created random art with circles END

# distance between circles
off_set = 5

# number of times to iterate the for loop, note: division returns float
number_of_iterations = int(360/off_set)

for _ in range(number_of_iterations):
    tim.color(random_color())
    tim.circle(100)
    #tim.left(random.randint(10,15))
    tim.left(off_set)
screen=turtle.Screen()
screen.exitonclick()

