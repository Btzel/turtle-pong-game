from turtle import Turtle
FONT = ("Arial",48,"normal")


class Scoreboard(Turtle):
    def __init__(self,position,score):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.goto(position)
        self.score_updater(score)
    def score_updater(self,score):
            self.clear()
            self.write(arg=score,align="center",font=FONT)