from turtle import Screen, Turtle
screen = Screen()

###TODO 4: CREATE BALL AND MAKE IT MOVE
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 8
        self.y_move = 6
        self.ball_speed = 0.1

    def ball_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self): #for bouncing off top/bottom wall
        self.y_move *= -1
        self.ball_speed *= 0.9
    def bounce_x(self): #for bouncing off paddles
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_ball(self):
        self.goto(0,0)
        self.bounce_x()

    def ball_speed(self):
        ball_speed = 1
        while game_is_on:
            x