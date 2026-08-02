from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score=0
        with open("data.txt",mode='r') as data:
            self.high_score=int(data.read())
        self.penup()
        self.color('white')
        self.goto(0, 260)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score={self.score} High Score:{self.high_score} ",False,'center',('Bold',16,'normal'))
    def reset_score(self):
        if self.score > self.high_score:
            self.high_score=self.score
            with open("data.txt",mode='w') as data:
                data.write(str(self.high_score))
        self.score=0
        self.update()
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", False, 'center', ('Bold', 22, 'normal'))
    def refresh(self):
        self.score += 1
        self.update()