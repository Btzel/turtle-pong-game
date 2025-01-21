from gamescreen import GameScreen
from players import Players
from borders import Borders
from ball import Ball
from scoreboard import Scoreboard


screen = GameScreen()
player1 = Players(player_num=1)
player2 = Players(player_num=2)
player1.speed("fastest")
player2.speed("fastest")
borders = Borders()
p1_scoreboard = Scoreboard((-50,200),player1.score)
p2_scoreboard = Scoreboard((50,200),player2.score)
ball = Ball()

screen.player_1_listener(player1.player_up,player1.player_down)
screen.player_2_listener(player2.player_up,player2.player_down)

game_is_on = True

while game_is_on:
    ball.player_collision(player1.pos())
    ball.player_collision(player2.pos())
    ball.border_collision()
    ball.move()
    ball.score(player1,player2,p1_scoreboard,p2_scoreboard)

screen.screen.exitonclick()