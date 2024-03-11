import random
import turtle
from turtle import Turtle,Screen
WIDTH,HEIGHT=400,400
color_list=["red","green","pink","orange","blue","navy blue","brown","purple","burlywood","sky blue"]
def no_of_turtle():
    count=0
    while True:
        count=input("how many turtles you want to participate in the race(2-10):")
        if count.isdigit():
            count=int(count)
        else:
            print("please enter a numeric value between 2 to 10")
            continue
        if 2<=count<=10:
            return count
        else:
            print("input is not in given range..... try again!!!")
turtles=no_of_turtle()
print(turtles)

s1=Screen()
s1.setup(400,400)

x_spacing = WIDTH//(turtles+1)
turtle_list=[]
for i in range(1,turtles+1):
    new_turtle=Turtle()
    new_turtle.shape("turtle")
    new_turtle.left(90)
    new_turtle.color(color_list[i-1])
    new_turtle.penup()
    new_turtle.goto(-WIDTH//2+(i*x_spacing),-HEIGHT//2+10)   # *********** (-400//2+(1+100),-200//2+10)
    turtle_list.append(new_turtle)

def race():
    is_race_on=True
    while is_race_on:
        for t in turtle_list:
            distance=random.randrange(1,10)
            t.forward(distance)

            x,y=t.pos()
            if y>=HEIGHT//2:
                print(f"the winner is {t.pencolor()} turtle")
                is_race_on=False

race()

s1.exitonclick()