from turtle import Turtle

# CONSTANTS
COLORS = ["red", "orange", "yellow", "blue", "purple"]
STARTING_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=2, stretch_len=1)
        self.penup()
        self.left(90)
        # self.goto(-60, 0)

    def move(self):
        new_x = self.xcor() - MOVE_INCREMENT
        for dist in range(10):
            if self.xcor() > -320:
                self.goto(new_x, self.ycor())
