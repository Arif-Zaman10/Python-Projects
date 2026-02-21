from turtle import Turtle, Screen
import random

tim = Turtle()

direction = [ 0, 180, 270, 90]
colors = ["red", "blue", "green", "yellow", "purple", "orange"]
tim.pensize(15)
tim.speed("fastest")
for _ in range(50):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.right(random.choice(direction))


screen = Screen()
screen.exitonclick()