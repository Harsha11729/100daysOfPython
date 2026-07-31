# import colorgram
# colors=colorgram.extract('DF.jpeg',30)
# rgb=[]
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb.append(new_color)
from turtle import Turtle,Screen
import random
color_list=[(199, 159, 114), (69, 91, 129), (148, 85, 52), (218, 210, 115), (136, 160, 193), (27, 32, 47), (179, 161, 35), (58, 33, 22), (184, 145, 164), (123, 70, 93), (137, 175, 153), (76, 115, 78), (143, 25, 15), (61, 30, 41), (187, 97, 82), (120, 28, 43), (46, 59, 94), (99, 118, 172), (178, 96, 114), (33, 51, 44), (99, 159, 85), (66, 84, 23), (215, 174, 192), (217, 181, 172), (218, 206, 7), (159, 210, 191)]
tim=Turtle()
screen=Screen()
screen.colormode(255)
tim.penup()
tim.hideturtle()
tim.speed('fastest')

def dot_paint():
    x=0
    for _ in range(10):
        x += 15
        tim.goto(0, -200 + x)
        for _ in range(10):
            choose=random.randint(0,20)

            tim.forward(20)
            tim.dot(10,color_list[choose])

dot_paint()




screen.exitonclick()