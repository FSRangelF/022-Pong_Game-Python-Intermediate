from turtle import Screen
from ball import Ball
from scoreboard import Score, Line
from paddle import Paddle
import time

SCREENSIZE_X = 1200
SCREENSIZE_Y = 800
DELAY = 0.05
MOVE_STEP = 30
BALL_SPEED = 20

# setup screen
screen = Screen()
screen.setup(width=SCREENSIZE_X, height=SCREENSIZE_Y)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

paddle_1 = Paddle(default_step=MOVE_STEP, initial_x=(SCREENSIZE_X/2)-40, initial_y=0 )
paddle_2 = Paddle(default_step=MOVE_STEP, initial_x=(-SCREENSIZE_X/2)+40, initial_y=0 )

line = Line(screen_height=SCREENSIZE_Y)

score_1 = Score(screen_height=SCREENSIZE_Y, initial_x=100)
score_2 = Score(screen_height=SCREENSIZE_Y, initial_x=-100)

ball = Ball(default_step=BALL_SPEED)

game_over = False

while not game_over:
    screen.update()
    ball.move()
    # Control direction
    screen.listen()
    screen.onkeypress(key="Up", fun=paddle_1.up)
    screen.onkeypress(key="Down", fun=paddle_1.down)
    screen.onkeypress(key="w", fun=paddle_2.up)
    screen.onkeypress(key="s", fun=paddle_2.down)

    # detect score
    if ball.xcor() <= -SCREENSIZE_X/2:
        score_1.increase_score()
        ball.reset_pos()

    if ball.xcor() >= SCREENSIZE_X/2:
        score_2.increase_score()
        ball.reset_pos()

    # detect collision with wall
    if ball.ycor() >= SCREENSIZE_Y/2 or ball.ycor() <= -SCREENSIZE_Y/2: 
        ball.bounce_wall()

    # detect collision with paddle_1
    if ball.xcor() >= paddle_1.xcor()-20 and ball.distance(paddle_1) < 40 : 
        ball.bounce_paddle()

    # detect collision with paddle_2
    if ball.xcor() <= paddle_2.xcor()+20 and ball.distance(paddle_2) < 40 : 
       ball.bounce_paddle()

    # game over condition
    if score_1.score >= 9 or score_2.score >= 9:
        score_1.game_over()
        game_over = True

    time.sleep(DELAY)

screen.exitonclick()