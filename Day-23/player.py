from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.start()
        self.shape('turtle')
        self.setheading(90)
        self.y_move = 20
        self.color('black')
    def start(self):
        self.goto(0, -270)
    def move(self):
        y = self.ycor() + self.y_move
        self.goto(self.xcor(), y)
