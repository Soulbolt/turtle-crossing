import random
from turtle import Turtle

# CONSTANTS
COLORS = ["red", "orange", "yellow", "blue", "purple"]
STARTING_DISTANCE = 5
CARS_TO_CREATE = 20
MOVE_INCREMENT = 10


class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.create_cars()

    def create_cars(self):
        for num in range(CARS_TO_CREATE):
            random_x = random.randint(-200, 300)
            random_y = random.randint(-260, 260)
            self.add_car(random_x, random_y)

    def add_car(self, x, y):
        new_car = Turtle(shape="square")
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=2, stretch_len=1)
        new_car.left(90)
        new_car.goto(x, y)
        self.car_list.append(new_car)

    def move(self):
        for car in self.car_list:
            new_x = car.xcor() - MOVE_INCREMENT
            for dist in range(10):
                if car.xcor() > -320:
                    car.goto(new_x, car.ycor())

    def reset_position(self, car):
        new_y = random.randint(-260, 260)
        if car in self.car_list:
            car.goto(300, new_y)
