from turtle import Screen
from ball import Ball
from scoreboard import Score, Line
from paddle import Paddle
import time

SCREENSIZE_X = 800
SCREENSIZE_Y = 600
DELAY = 0.05
MOVE_STEP = 40
DETECTION_TRESHOLD = 50
SPACER = 20
game_over = False
ball_speed = 10

# setup screen
screen = Screen()
screen.setup(width=SCREENSIZE_X, height=SCREENSIZE_Y)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_1 = Paddle(default_step=MOVE_STEP, initial_x=(SCREENSIZE_X/2)-SPACER, screen_height=SCREENSIZE_Y)
paddle_2 = Paddle(default_step=MOVE_STEP, initial_x=(-SCREENSIZE_X/2)+SPACER, screen_height=SCREENSIZE_Y)

line = Line(screen_height=SCREENSIZE_Y)

score_1 = Score(screen_height=SCREENSIZE_Y, initial_x=5*SPACER)
score_2 = Score(screen_height=SCREENSIZE_Y, initial_x=-5*SPACER)

ball = Ball(default_step=ball_speed)

# Control direction
screen.listen()
screen.onkeypress(key="Up", fun=paddle_1.up)
screen.onkeypress(key="Down", fun=paddle_1.down)
screen.onkeypress(key="w", fun=paddle_2.up)
screen.onkeypress(key="s", fun=paddle_2.down)

while not game_over:
    screen.update()
    ball.move()

    # detect score
    if ball.xcor() <= -SCREENSIZE_X/2:
        score_1.increase_score()
        ball.reset_pos()

    if ball.xcor() >= SCREENSIZE_X/2:
        score_2.increase_score()
        ball.reset_pos()

    # detect collision with wall
    if ball.ycor() >= SCREENSIZE_Y/2 - SPACER or ball.ycor() <= -SCREENSIZE_Y/2 + SPACER:  
        ball.bounce_wall()

    # detect collision with paddle_1
    if ball.xcor() >= paddle_1.xcor()-SPACER and ball.distance(paddle_1) < DETECTION_TRESHOLD : 
        ball.bounce_paddle()

    # detect collision with paddle_2
    if ball.xcor() <= paddle_2.xcor()+SPACER and ball.distance(paddle_2) < DETECTION_TRESHOLD : 
       ball.bounce_paddle()

    # game over condition
    if score_1.score >= 9 or score_2.score >= 9:
        score_1.game_over()
        game_over = True

    time.sleep(DELAY)

screen.exitonclick()