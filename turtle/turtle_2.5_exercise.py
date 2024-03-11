import turtle
from turtle import Turtle,Screen
import random
tom=Turtle()
s1=Screen()
tom.speed("fastest")
tom.width(10)
turtle.colormode((255))
tom.color("red","yellow")
tom.begin_fill()
while True:
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    tom.pencolor((r,g,b))
    tom.circle(100)
    tom.lt(15)
    if tom.heading()==0:
        break
tom.end_fill()

s1.exitonclick()