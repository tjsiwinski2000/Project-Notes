from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left=0
        self.score_right=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        #moves turtle to position and writes score_left value
        self.goto(-100,200)
        self.write(self.score_left, font =FONT, align="center")
        #moves turtle to position and writes score_right value
        self.goto(100, 200)
        self.write(self.score_right, font=FONT, align="center")

    def l_point(self):
        self.score_left += 1
        self.update_scoreboard()

    def r_point(self):
        self.score_right += 1
        self.update_scoreboard()

