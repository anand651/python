from turtle import Turtle,Screen
s1=Screen()
abc=Turtle()
abc.speed(10)

'''draw a circle'''
abc.penup()
abc.goto(-200,100)
abc.pendown()
abc.color("red","yellow")
abc.begin_fill()
abc.circle(50)
abc.end_fill()

'''draw a square'''
abc.penup()
abc.goto(200,100)
abc.pendown()
abc.color("green","pink")
abc.begin_fill()
abc.forward(100)
abc.left(90)
abc.forward(100)
abc.left(90)
abc.forward(100)
abc.left(90)
abc.forward(100)
abc.end_fill()

'''draw a pantogone'''
abc.penup()
abc.goto(200,-100)
abc.pendown()
abc.color("orange","blue")
abc.begin_fill()
abc.rt(60)
abc.forward(100)
abc.lt(90)
abc.forward(100)
abc.lt(60)
abc.forward(100)
abc.lt(75)
abc.forward(100)
abc.lt(80)
abc.forward(100)
abc.end_fill()


'''draw a triangle'''
abc.penup()
abc.goto(-200,-100)
abc.begin_fill()
abc.pendown()
abc.color("black","brown")
abc.lt(90)
abc.forward(100)
abc.lt(120)
abc.forward(100)
abc.lt(120)
abc.forward(100)
abc.end_fill()


s1.exitonclick()