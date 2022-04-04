from turtle import  Turtle

INITIAL_SPEED = 0.05
class Ball(Turtle) :
    def __init__(self):
        super(Ball, self).__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = INITIAL_SPEED

    def move(self):
            self.setpos(x=self.xcor()+self.x_move,y=self.ycor()+self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = INITIAL_SPEED
        self.bounce_x()

