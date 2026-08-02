from turtle import Screen

from scoreboard import ScoreBoard
from snake import Snake
import time
from food import Food
screen=Screen()
screen.tracer(0)
screen.listen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
snake=Snake()
snake.create()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
food=Food()
scoreboard=ScoreBoard()
is_on=True
while is_on:
    time.sleep(0.1)
    snake.move(20)
    screen.update()
    if snake.segment[0].distance(food)<15:
        food.refresher()
        scoreboard.refresh()
        snake.extend()

    if snake.segment[0].xcor()>278 or snake.segment[0].xcor()<-278 or snake.segment[0].ycor()>278 or snake.segment[0].ycor()<-278:
        snake.clear_snake()
        snake.reset()
        scoreboard.reset_score()
    for segment in snake.segment[1:]:
        if snake.segment[0].distance(segment)<10:
            is_on=False
            scoreboard.reset_score()





screen.exitonclick()