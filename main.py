import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
    # Detect when player reaches the goal (top wall)
    if player.ycor() > 280:
        car_manager.speed_increment()
        player.reset_position()
        scoreboard.score_increment()
    # Detect when the car reaches the left wall
    # for car in car_manager.car_list:
    #     if car.xcor() < -300:
    #         car_manager.reset_position(car)
    # Detect collision with player
    for car in car_manager.car_list:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
