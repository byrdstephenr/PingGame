from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


#Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((250, 0))
#Second Paddle
l_paddle = Paddle((-250, 0))

ball = Ball()
scoreboard = Scoreboard()




screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(.11)
    screen.update()
    ball.move()
    # Collision with walls
    if ball.ycor() > 280 or ball.ycor() < -260:
        ball.bounce_y()


#Collision with Paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 230 or ball.distance(l_paddle) < 50 and ball.xcor() < -230:
        ball.bounce_x()

#Detect when paddle misses ball/passes end
    if ball.xcor() > 280:
        ball.reset_position()
        scoreboard.l_point()
    elif ball.xcor() < -280:
        ball.reset_position()
        scoreboard.r_point()


#Keep Score



screen.exitonclick()