from turtle import Turtle
import random
import math
import time
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.random_direction_list = []
        self.ball_direction = self.random_direction()
        self.is_score = False

    def random_direction(self):
        self.random_direction_list.append(random.randint(105, 165))
        self.random_direction_list.append(random.randint(195, 255))
        self.random_direction_list.append(random.randint(15,75))
        self.random_direction_list.append(random.randint(285,335))
        direction = random.choice(self.random_direction_list)
        self.random_direction_list.clear()
        return direction

    def move(self):
        cur_pos = self.pos()
        radian = math.radians(self.ball_direction)
        target_position = (cur_pos[0] + math.cos(radian) * 4, cur_pos[1] + math.sin(radian) * 4)
        self.goto(target_position[0] ,target_position[1])

    def border_collision(self):
        if self.ycor() > 260 or self.ycor() < -260:
            self.ball_direction = 360 - self.ball_direction

    def score(self,player1,player2,p1_scoreboard,p2_scoreboard):
        if self.xcor() > 359:
            player1.score += 1
            self.is_score = True
        elif self.xcor() < -360:
            player2.score += 1
            self.is_score = True
        if self.is_score:
            p1_scoreboard.score_updater(player1.score)
            p2_scoreboard.score_updater(player2.score)
            self.hideturtle()
            self.goto(0, 0)
            self.showturtle()
            self.ball_direction = self.random_direction()
            time.sleep(0.1)
            self.is_score = False

    def player_collision(self,player_pos):
        if self.xcor() > 320 or self.xcor() < -320:
            if self.distance(player_pos) < 70:
                self.ball_direction = (180 - self.ball_direction) % 360




