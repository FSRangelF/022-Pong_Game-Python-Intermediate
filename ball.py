from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self, default_step, shape = "circle", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.ball_speed = default_step
        self.color("white")
        self.penup()
        self.reset_pos()
        self.speed("fastest")
    
    def reset_pos(self):
        self.setposition(0, 0)
        self.ball_speed = 10
        self.setheading(random.choice([random.randint(0,45), random.randint(135, 225), random.randint(315, 360)]))
    
    def move(self):
        self.forward(self.ball_speed)

    def bounce_wall(self):
        angle_bounce = -self.heading()
        self.setheading(angle_bounce)
    
    def bounce_paddle(self):
        angle_bounce = -self.heading() - 180
        self.setheading(angle_bounce)
        self.ball_speed *= 1.2