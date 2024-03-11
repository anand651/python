import turtle
from turtle import Turtle,Screen
import random
tom=Turtle()
s1=Screen()
tom.speed("fastest")
turtle.colormode((255))
for _ in range(50):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    tom.pencolor((r,g,b))
    tom.dot(20)
    x=random.randint(-400,200)
    y=random.randint(-400,200)
    # tom.penup()
    tom.goto((x,y))
    # tom.pendown()



s1.exitonclick()