# from turtle import Turtle
# abc=Turtle()
# xyz=Turtle()
# abc.forward(100)
# xyz.forward(200)
'''another way to import turtle'''

# import turtle as t
# abc=t.Turtle()
# xyz=t.Turtle()

# import turtle
# abc=turtle.Turtle()
# xyz=turtle.Turtle()
# abc.screen.mainloop()

from turtle import Turtle,Screen
s1=Screen()
tom=Turtle()
tom.shape("turtle")
tom.forward(100)
# tom.pencolor("red")
# tom.fillcolor("yellow")
tom.color("red","yellow")
tom.forward(100)

tom.begin_fill()
tom.circle(100)
tom.end_fill()

tom.rt(90)
tom.penup()
tom.forward(100)
tom.pendown()
tom.color("green","pink")
tom.pensize(2)
tom.begin_fill()
tom.circle(60)
tom.end_fill()
print(tom.pos())

tom.hideturtle()
print(tom.isvisible())
tom.goto(-100,100)
tom.showturtle()
s1.exitonclick()