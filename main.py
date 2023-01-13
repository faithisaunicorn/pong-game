import turtle as t

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

###TODO 1: CREATE SCREEN
screen = t.Screen()
screen.setup(width= 800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350,0)) #put in double brackets so it's accepted as a tuple instead of 2 separate args
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.ball_move()

    ###TODO 5: DETECT COLLISION W WALL (TOP & BOTTOM ONLY) AND BOUNCE
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    ###TODO 6: DETECT COLLISION W PADDLE
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    ###TODO 7: DETECT WHEN PADDLE MISSES
    if ball.xcor() > 360: #R paddle loses
        ball.reset_ball()
        scoreboard.l_point()

    if ball.xcor() < -360: #L paddle loses
        ball.reset_ball()
        scoreboard.r_point()


screen.exitonclick()