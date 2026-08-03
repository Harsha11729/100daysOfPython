from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen=Screen()
screen.tracer(0)
screen.setup(800,600)
screen.bgcolor('black')
screen.title('pong')
r_paddle=Paddle(350,0)
l_paddle=Paddle(-350,0)
x_score=0
y_score=0
ball=Ball()
scoreboard=ScoreBoard()
screen.update()
screen.listen()
screen.onkeypress(r_paddle.move_up,"Up")
screen.onkeypress(r_paddle.move_down,"Down")
screen.onkeypress(l_paddle.move_up,"w")
screen.onkeypress(l_paddle.move_down,"s")
is_game=True
while is_game:
    time.sleep(0.05)
    ball.move()
    screen.update()
    if ball.ycor() > 290 or ball.ycor() < -290:
       ball.y_bounce()
    if (ball.distance(r_paddle)<50 and ball.xcor()>320) or (ball.distance(l_paddle)<50 and ball.xcor()<-320):
        ball.x_bounce()
    if ball.xcor()>380:
        ball.reset_position()
        ball.x_bounce()
        scoreboard.l_score+=1
        scoreboard.update()
    if ball.xcor()<-380:
        ball.reset_position()
        ball.x_bounce()
        scoreboard.r_score += 1
        scoreboard.update()

screen.exitonclick()