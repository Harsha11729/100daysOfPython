from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score=0
        self.r_score=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update()
    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("courier", 80, "normal"))

