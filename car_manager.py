from turtle import Turtle

# CONSTANTS
COLORS = ["red", "orange", "yellow", "blue", "purple"]
STARTING_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()