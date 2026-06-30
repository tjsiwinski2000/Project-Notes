from turtle import Turtle, Screen

#Initialize turle
tim = Turtle()
tim.shape("turtle")
tim.color("dark turquoise")
screen= Screen()

#Turtle to draw dashed line
# for _ in range(20):
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()
#     tim.forward(5)

#Create list of ten hero names
import heroes
# for _ in range(10):
#     print(heroes.gen())


# tim.left(100) sets an orientation
tim.penup()
y_start = screen.window_height() /2 -20
tim.goto(0,y_start)
tim.pendown()


#Triangle
for _ in range(3):
    tim.forward(100)
    tim.right(120)
#Square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
# #Pentagon
# for _ in range(5):
#     tim.forward(120)
#     tim.right(72)
#Hexagaon

#Challenge square, pentagon... decagon
COLOR_LIST = [
    'red', 'blue', 'green', 'yellow', 'purple', 'orange',
    'cyan', 'magenta', 'turquoise', 'gold', 'coral', 'skyblue',
    'lightgreen', 'darkred', 'violet', 'navy', 'brown', 'pink'
]
import  random
num_sides = [4,5,6,7,8,9,10]
len_side =99
for sides in num_sides:
    len_side += 1
    angle = 360/sides
    color=random.choice(COLOR_LIST)
    for _ in range(sides):
        tim.color(color)
        tim.forward(len_side)
        tim.right(angle)


#Lines below needed for screen persistence
screen.exitonclick()