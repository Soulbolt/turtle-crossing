from turtle import Turtle

# CONSTANTS
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
GAME_OVER = "Game Over"


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 1
        super().clear()
        self.update_scoreboard()

    def score_increment(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-280, 260)
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(GAME_OVER, align=ALIGNMENT, font=FONT)
