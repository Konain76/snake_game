from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


def up():
    snake.upper()


def down():
    snake.down()


def left():
    snake.left()


def right():
    snake.right()


screen.listen()
screen.onkey(key="Up", fun=up)
screen.onkey(key="Down", fun=down)
screen.onkey(key="Left", fun=left)
screen.onkey(key="Right", fun=right)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #to check collision with food

    if snake.head.distance(food) < 15:

        snake.extend_snake()
        scoreboard.increse()
        food.refresh()

    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        scoreboard.reset()
        snake.reset()

    for segment in snake.movement[1:len(snake.movement)]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
