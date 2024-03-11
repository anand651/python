import random
from turtle import Turtle
tom=Turtle()
colors=["red","green","pink","orange","blue","alice blue","aquamarine","brown","burlywood"]
for i in range(3,9):
    angle=360/i
    tom.pencolor(random.choice(colors))
    for _ in range(i):
        tom.forward(100)
        tom.right(angle)
tom.screen.mainloop()