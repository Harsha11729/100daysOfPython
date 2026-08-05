from turtle import Screen
import time
from player import Player
from car import Car
from scoreboard import Scoreboard
pos=[(370,10),(370,40),(370,70),(370,100),(370,140),(370,-40),(370,-80),(370,-150),(370,-200),(370,-280)]
cars=[]
def create_cars():
    for cor in pos:
        car = Car()
        car.goto(cor)
        cars.append(car)
def remove_cars():
    for car in cars:
        car.hideturtle()
    cars.clear()

scoreboard=Scoreboard()
player=Player()
screen=Screen()
screen.listen()
screen.onkeypress(player.move,"Up")
screen.tracer(0)
screen.setup(600,600)
screen.bgcolor('white')
is_game=True
create_cars()
while is_game:
    time.sleep(0.1)
    screen.update()
    for car in cars:
        if car.distance(player)<30:
            is_game=False
            scoreboard.game_over()
        else:
            car.move()
    if player.ycor()>200:
        player.start()
        scoreboard.level_up()
        scoreboard.writes()

screen.exitonclick()