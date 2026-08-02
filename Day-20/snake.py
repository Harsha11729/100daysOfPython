from turtle import Turtle

st_pos=[(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.segment = []
    def create(self):
        for pos in st_pos:
            self.add_seg(pos)
    def add_seg(self,pos):
        t = Turtle()
        t.shape("square")
        t.color("white")
        t.penup()
        t.goto(pos)
        self.segment.append(t)
    def clear_snake(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
    def reset(self):
        self.create()
    def extend(self):
        self.add_seg(self.segment[-1].position())
    def move(self,distance):
        for seg in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg - 1].xcor()
            new_y = self.segment[seg - 1].ycor()
            self.segment[seg].goto(new_x, new_y)
        self.segment[0].forward(distance)
    def up(self):
        if self.segment[0].heading()!=270:
            self.segment[0].setheading(90)
    def down(self):
        if self.segment[0].heading() != 90:
            self.segment[0].setheading(270)
    def right(self):
        if self.segment[0].heading()!=180:
            self.segment[0].setheading(0)
    def left(self):
        if self.segment[0].heading()!=0:
            self.segment[0].setheading(180)
