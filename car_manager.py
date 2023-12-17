import random
from turtle import Turtle

# CONSTANTS
COLORS = ["red", "orange", "yellow", "blue", "purple", "green", "lightblue"]
STARTING_DISTANCE = 5
CARS_TO_CREATE = 20
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.car_speed = STARTING_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.car_list.append(new_car)

    def move_cars(self):
        for car in self.car_list:
            car.backward(self.car_speed)

    def speed_increment(self):
        self.car_speed += MOVE_INCREMENT

    def reset_position(self, car):
        new_y = random.randint(-260, 260)
        if car in self.car_list:
            car.goto(300, new_y)
            self.car_speed = 0.1
