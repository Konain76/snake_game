from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super(Food, self).__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        x_axis = random.randint(-280, 280)
        y_axis = random.randint(-280, 280)
        self.goto(x_axis, y_axis)