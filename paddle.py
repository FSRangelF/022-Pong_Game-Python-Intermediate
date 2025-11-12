from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, default_step, initial_x, initial_y, shape = "square", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.step = default_step
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_len=4, stretch_wid=1, outline=1)
        self.penup()
        self.setheading(90)
        self.teleport(x=initial_x, y=initial_y)

    def up(self):
        self.forward(self.step)

    def down(self):
        self.backward(self.step)