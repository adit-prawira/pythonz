from turtle import Turtle, Screen
import random

turtle = Turtle()
colors  = ["red","green","blue","orange","purple","pink","yellow"]
turtle.shape("turtle")

min_sides = int(input("Enter minimum number of sides to drawn on the GUI: "))
max_sides = int(input("Enter maximum number of sides to drawn on the GUI: "))

def draw_shaped(n_sides):
    angle = 360/n_sides
    for _ in range(n_sides):
        turtle.forward(100)
        turtle.right(angle)
        

for sides in range (min_sides, max_sides):
    draw_shaped(sides)
    turtle.color(random.choice(colors))
    
screen = Screen()
screen.exitonclick()