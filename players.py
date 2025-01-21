from turtle import Turtle
PLAYER_1_INITIAL_POS = (-350,0)
PLAYER_2_INITIAL_POS = (350,0)

class Players(Turtle):
    def __init__(self,player_num):
        super().__init__()

        self.player_num = player_num
        self.score = 0
        self.penup()
        self.speed(6)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=7,stretch_len=1)
        self.take_your_place(self.player_num)

    def take_your_place(self,player_num):
        if player_num == 1:
            self.goto(PLAYER_1_INITIAL_POS)
        else:
            self.goto(PLAYER_2_INITIAL_POS)

    def player_up(self):
        if self.ycor() < 190:
            self.goto(self.xcor(),self.ycor() + 38.33)

    def player_down(self):
        if self.ycor() > -190:
            self.goto(self.xcor(),self.ycor() - 38.33)




