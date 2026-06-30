from turtle import Turtle
FONT = ("Courier", 10, "normal")

class Label(Turtle):
   def __init__(self):
       super().__init__()
       self.penup()
       self.hideturtle()


   def update_label(self,x,y,name):
       #moves turtle to position and write name
       self.goto(x,y)
       self.write(name, font =FONT, align="center")