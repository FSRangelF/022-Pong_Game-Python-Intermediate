from turtle import Turtle

ALIGMENT = "center"
FONT = ("Courier", 72, "bold")

class Score(Turtle):

    def __init__(self, screen_height, initial_x, shape = "classic", undobuffersize = 1000, visible = False):
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.teleport(x=initial_x, y=(screen_height/2-120))  
        self.refresh_score()

    def increase_score(self):
        self.score += 1
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(arg=f"{self.score}",  align=ALIGMENT, font=FONT)
    
    def game_over(self):
        self.teleport(0,0)
        self.write(arg="GAME OVER",  align=ALIGMENT, font=FONT)

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