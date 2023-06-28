from turtle import Turtle

SHAPE = "square"
COLOR = "white"
UP = 90
DOWN = 270

#Create and Move Paddle
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.shapesize(stretch_len=.5, stretch_wid=5)
        self.penup()
        position = self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)




