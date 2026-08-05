from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pre="Level:"
        self.level=1
        self.writes()
    def writes(self):
        self.clear()
        self.goto(120, 200)
        self.write(self.level, align="center", font=("courier", 80, "normal"))
        self.goto(-100, 200)
        self.write(self.pre, align="center", font=("courier", 80, "normal"))
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=("courier",40,"normal"))
    def level_up(self):
        self.level+=1
