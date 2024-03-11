from turtle import Turtle,Screen
s1=Screen()
abc=Turtle()
abc.speed(10)
abc.shape("turtle")

'''draw a arrow'''
# abc.forward(10)
# abc.penup()
# abc.forward(10)
# abc.pendown()
# abc.forward(10)
# abc.penup()
# abc.forward(10)
# abc.pendown()
# abc.forward(10)
# abc.penup()
# abc.forward(10)
# abc.pendown()
# abc.forward(10)
# abc.penup()
# abc.forward(10)
# abc.pendown()
# abc.forward(10)
# abc.penup()
# abc.forward(10)
# abc.pendown()
# abc.forward(10)
# abc.penup()
# abc.forward(10)
# abc.pendown()
# abc.forward(10)
# abc.penup()
# abc.forward(10)
# abc.pendown()
# abc.forward(10)
# abc.penup()
# abc.forward(10)
# abc.pendown()
'''    or      '''

# for _ in range(10):
for i in range(10):
     abc.forward(10)
     abc.penup()
     abc.forward(10)
     abc.pendown()
'''   or    '''

# we can used pencolor to draw the arrow ("black","white")

s1.exitonclick()