STARTING = [(0, 0), (-20, 0), (-40, 0)]
from turtle import Turtle
class Snake:
    def __init__(self):

        self.movement = []
        self.create_snake()
        self.head = self.movement[0]

    def create_snake(self):

        for i in STARTING:
            self.add_box(i)

    def add_box(self, position):
        turtle = Turtle()
        turtle.penup()
        turtle.shape("square")
        turtle.color("white")
        turtle.goto(position)
        self.movement.append(turtle)

    def reset(self):
        for seg in self.movement:
            seg.goto(1000, 1000)
        self.movement.clear()
        self.create_snake()
        self.head = self.movement[0]

    def extend_snake(self):
        self.add_box(self.movement[-1].position())

    def move(self):
        for i in range(len(self.movement) - 1, 0, -1):
            n_x = self.movement[i - 1].xcor()
            n_y = self.movement[i - 1].ycor()
            self.movement[i].goto(n_x, n_y)
        self.movement[0].forward(20)

    def upper(self):
        self.movement[0].setheading(90)

    def down(self):
        self.movement[0].setheading(270)

    def left(self):
        self.movement[0].setheading(180)

    def right(self):
        self.movement[0].setheading(0)















