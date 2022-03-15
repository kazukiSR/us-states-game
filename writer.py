from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 10, "normal")


class Writer(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def writeState(self, state, pos):
        self.goto(pos[0], pos[1])
        self.write(f"{state}", align=ALIGNMENT, font=FONT)
