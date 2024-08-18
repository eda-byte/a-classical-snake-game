from turtle import Turtle
from snake import Snake
ALIGNMENT= "center"
FONT=("Courier",24,"normal")

class Scoreboard(Turtle):
       # create_score()
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("White")
        self.penup()
        self.goto(0,270)

        self.hideturtle()


    def score_writer(self):
        self.write(f"Score: {self.score}",align= ALIGNMENT, font=("Arial", 24, "normal"))
        return self.score

    def increase_score(self):
            self.score=self.score+1

    def the_end(self):
        self.goto(0,0)
        self.write(f"Game Over.", align=ALIGNMENT, font=("Arial", 24, "normal"))
