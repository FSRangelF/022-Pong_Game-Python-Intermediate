from turtle import Turtle

class Score(Turtle):

    def __init__(self, shape = "classic", undobuffersize = 1000, visible = False):
        super().__init__(shape, undobuffersize, visible)











class Line(Turtle):

    def __init__(self, screen_height, shape = "square", undobuffersize = 1000, visible = False):
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.speed("fastest")
        self.width(20)
        self.setheading(90)
        self.teleport(x=0, y=-screen_height/2)
        while self.ycor() < screen_height/2:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(60)