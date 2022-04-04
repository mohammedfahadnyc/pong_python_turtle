from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x_cor,y_cor):
        super(Paddle, self).__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.goto(x=x_cor,y=y_cor)


    def move_up(self):
            self.sety(self.ycor() + 20)

    def move_down(self):
            self.sety(self.ycor() - 20)