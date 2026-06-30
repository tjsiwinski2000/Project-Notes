#1013-2025 - output Hirst style painting
# - clever use of colorgram to scrape colors from an image (of a Hirst Painting)
# - clever solution by Angela Yu to create the row of dots w/o undue work
# - test change TJS

import colorgram

# extracting colors from image.jpg via cologram library
# colors = colorgram.extract('image.jpg',50)
#
# color_list=[]
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     tuple=(r,g,b)
#     color_list.append(tuple)
# print(f"{len(color_list)} items in the list ")
# print(f"\n{color_list}")

# requirements: 10 by 10 pattern of dots via turtle

# NOTE: color_list = colors extracted ^ , manually removed background colors (white, beige ...)
color_list= [(142, 80, 52), (68, 95, 148), (154, 170, 186), (156, 183, 164), (156, 61, 81), (197, 196, 177), (183, 140, 156), (91, 155, 106), (155, 158, 61), (112, 106, 168), (176, 100, 119), (68, 130, 101), (184, 196, 189), (36, 57, 112), (38, 42, 73), (201, 185, 192), (75, 152, 158), (73, 36, 38), (69, 40, 38), (189, 189, 199), (204, 186, 183), (132, 39, 44), (134, 41, 37), (177, 197, 201), (159, 111, 106), (70, 75, 48)]
import random
#debug -> print(random.choice(color_list))
import turtle
tim = turtle.Turtle()
turtle.colormode(255)
screen=turtle.Screen()
tim.shape("turtle")
tim.color("dark turquoise")
tim.speed(0)

# # move turtle to starting position
#x_start = 0- screen.window_width() /2  +20
tim.penup()
#tim.goto(x_start,0)
tim.setheading(225)
tim.forward(300)
tim.setheading(0)


def draw_row():
    for _ in range(11):
        tim.pendown()
        tim.dot(20,random.choice(color_list) )
        tim.penup()
        tim.forward(50)

#TJS: 1013-2025 Angela Yu solution was pretty clever
# Fundamentally my flow was completely WRONG
for _ in range(11):
    draw_row()
    # next six lines move the turtle back to start position [BUT ONE ROW UP]
    tim.setheading(90)
    tim.penup()
    tim.forward(50)
    tim.setheading(180)
    tim.forward(550)
    tim.setheading(0)


screen.exitonclick()