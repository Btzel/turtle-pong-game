from turtle import Screen

class GameScreen:
    def __init__(self):
        self.screen = Screen()
        self.screen.bgcolor("black")
        self.screen.setup(width=800,height=600)
        self.screen.title("Pong")

    def player_1_listener(self,player_up,player_down):
        self.screen.listen()
        self.screen.onkey(key="w",fun=player_up)
        self.screen.onkey(key="s",fun=player_down)

    def player_2_listener(self,player_up,player_down):
        self.screen.listen()
        self.screen.onkey(key="Up", fun=player_up)
        self.screen.onkey(key="Down", fun=player_down)