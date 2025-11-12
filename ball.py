from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self, default_step, shape = "circle", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.step = default_step
        self.color("white")
        self.penup()
        self.reset_pos()
        self.speed("fastest")
    
    def reset_pos(self):
        self.setposition(0, 0)
        self.setheading(random.randint(0,360))
    
    def move(self):
        self.forward(self.step)