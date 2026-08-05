from turtle import Turtle
import random
class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(1,4)
        self.color(random.choice(['blue','green','red','orange','pink']))
        self.x_move=20
        self.speed('slow')
    def move(self):
        x=self.xcor()+self.x_move
        self.goto(x,self.ycor())
    def inc_speed(self):
        self.x_move-=20
