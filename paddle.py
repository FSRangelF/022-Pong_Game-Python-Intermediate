from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, default_step, initial_x, screen_height, shape = "square", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.step = default_step
        self.screen_height = screen_height
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()
        self.setheading(90)
        self.teleport(x=initial_x, y=0)

    def up(self):
        if self.ycor() < self.screen_height/2 - 80:
            self.forward(self.step)

    def down(self):
        if self.ycor() > -self.screen_height/2 + 80:
            self.backward(self.step)
