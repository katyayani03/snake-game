from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Ariel", 14, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update()

    def increase_score(self):
        self.score += 1
        self.update()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f"GAME OVER!!!", align=ALIGNMENT, font=FONT)
