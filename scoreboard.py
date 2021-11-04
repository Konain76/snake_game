from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard,self).__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(arg=f"Score:{self.score}", align="center", font=("arial", 24, "normal"))
        self.hideturtle()
        self.update()

    def update(self):

        self.write(arg=f"Score:{self.score} High score: {self.high_score}", align="center", font=("arial", 24, "normal"))
        self.clear()
    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update()

    def increse(self):
        self.score += 1
        self.update()



