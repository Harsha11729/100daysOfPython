# from turtle import Turtle ,Screen
# turtle=Turtle()
# for i in range(4):
#     turtle.forward(100)
#     turtle.left(90)
# screen=Screen()
# screen.exitonclick()
# from turtle import Turtle,Screen
# tim=Turtle()
# for i in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
# screen=Screen()
# screen.exitonclick()
# from turtle import Turtle,Screen
# tim=Turtle()
# x=3
# degree=0
# while x<11:
#     degree = 360 / x
#     for i in range(x):
#         tim.forward(100)
#         tim.right(degree)
#     x += 1
# screen=Screen()
# screen.exitonclick()
# from turtle import Turtle,Screen
# import random
# colour=['LightSkyBlue','Chocolate','LawnGreen','OldLace','MediumVioletRed','SeaGreen','LightCyan']
# tim=Turtle('turtle')
# screen=Screen()
# screen.colormode(255)
# def choose_colour():
#     r=random.randint(0,255)
#     g=random.randint(0,255)
#     b=random.randint(0,255)
#     random_color=(r,g,b)
#     return random_color
#
# tim.pensize(10)
# tim.speed('fastest')
# for i in range(200):
#     color=random.randint(0,6)
#     choice=random.choice([0,90,180,270])
#     tim.color(choose_colour())
#     tim.setheading(choice)
#     tim.forward(20)
# screen.exitonclick()
import random
from turtle import Turtle,Screen
screen=Screen()
screen.colormode(255)
def choose_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color
tim=Turtle()
tim.speed('fastest')
def circles(no_of_gaps):
    for _ in range(int(360/no_of_gaps)):
        tim.color(choose_color())
        tim.circle(100)
        tim.setheading(tim.heading() + no_of_gaps)
circles(3)

screen.exitonclick()


