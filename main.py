from turtle import Screen
from ball import Ball
from scoreboard import Score, Line
from paddle import Paddle
import time

SCREENSIZE_X = 1200
SCREENSIZE_Y = 800
DELAY = 0.05
MOVE_STEP = 20

# setup screen
screen = Screen()
screen.setup(width=SCREENSIZE_X, height=SCREENSIZE_Y)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

paddle_1 = Paddle(default_step=MOVE_STEP, initial_x=(SCREENSIZE_X/2)-40, initial_y=0 )
paddle_2 = Paddle(default_step=MOVE_STEP, initial_x=(-SCREENSIZE_X/2)+40, initial_y=0 )

line = Line(screen_height=SCREENSIZE_Y)

ball = Ball(default_step=2*MOVE_STEP)

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

    time.sleep(DELAY)

screen.exitonclick()