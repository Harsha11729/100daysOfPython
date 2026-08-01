# from turtle import Turtle,Screen
# tim=Turtle()
# def move_for():
#     tim.forward(5)
# def move_back():
#     tim.backward(5)
# def move_clockwise():
#     curve=tim.heading()+10
#     tim.setheading(curve)
# def move_anti():
#     curve=tim.heading()-10
#     tim.setheading(curve)
# def cler_drw():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
# screen=Screen()
# screen.listen()
# screen.onkeypress(key="w",fun=move_for)
# screen.onkeypress(key="s",fun=move_back)
# screen.onkeypress(key="a",fun=move_clockwise)
# screen.onkeypress(key="d",fun=move_anti)
# screen.onkeypress(key="c",fun=cler_drw)
# screen.exitonclick()
from turtle import Turtle,Screen
import random
x=0
colours=['red','green','black','yellow']
screen=Screen()
screen.setup(500,400)
turtles=[]
for _ in range(4):
    t=Turtle()
    t.penup()
    t.shape('turtle')
    t.color(colours[_])
    turtles.append(t)
    t.goto(-230, -100+x)
    x+=50
bet=screen.textinput(title="Make your bet...",prompt="Enter the colour of turtle you guess to win:").lower()
is_game_on=True
while is_game_on:
    tur_for=random.randint(0,3)
    turtles[tur_for].forward(30)
    if turtles[tur_for].xcor()>247:
        is_game_on=False
        clr=turtles[tur_for].pencolor()
        print(clr)
if clr==bet:
    print("you won the bet")
else:
    print("you lost the bet")
screen.exitonclick()