from turtle import Turtle

class Borders(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed(6)
        self.penup()
        self.goto(-370,270)
        self.color("white")
        self.draw_borders()

    def draw_borders(self):
        self.pensize(width=2)
        self.pendown()
        self.goto(370,270)
        self.goto(370,-270)
        self.goto(-370,-270)
        self.goto(-370,270)