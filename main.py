from turtle import *

t = Turtle()
s = Screen()
s.title("etch a sketch")
def mov_forward():
    t.forward(50)

def mov_back():
    t.back(50)

def mov_right():
    t.right(10)

def mov_left():
    t.left(10)

def clear():
    t.clear()

s.listen()
s.onkey(fun=mov_forward, key="w")
s.onkey(fun=mov_back, key="s")
s.onkey(fun=mov_right, key="d")
s.onkey(fun=mov_left, key="a")
s.onkey(fun=clear,key="c")
s.exitonclick()
