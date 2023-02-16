# 프렉탈
import turtle # 그림그려주는 거북이

t = turtle.setup(width=600, height=600)

import turtle  
# Creating turtle  
t = turtle.Turtle()  
  
turtle.bgcolor("black")  
turtle.pensize(2)  
turtle.speed(0)  
  
while (True):  
    for i in range(6):  
        for colors in ["red", "blue", "magenta", "green", "yellow", "white"]:  
            turtle.color(colors)  
            turtle.circle(100)  
            turtle.left(10)  
  

turtle.hideturtle()  
turtle.mainloop() 