from turtle import Turtle,Screen
tom=Turtle()
s1=Screen()
tom.speed("fast")
tom.color("red","yellow")
tom.begin_fill()
while True:
    tom.forward(200)
    tom.lt(170)
    if tom.heading()==0:
        break
tom.end_fill()










s1.exitonclick()