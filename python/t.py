import random
from turtle import *
shape("turtle")
speed(116)
pencolor("white")
pensize(6)
Screen().bgcolor("DarkOrange")
def vshape(size):
    right(25)
    forward(size)
    backward(size)
    left(50)
    forward(size)
    backward(size)
    right(25)
def snow_flake_arm(size):
    for x in range(0,4):
        forward(size)
        vshape(size)
    backward(size*4)
def snow_flake(size):
    for x in range(0,18):
        snow_flake_arm(size)
        right(20)
for i in range(0,10):
    size = random.randint(5,30)
    x = random.randint(-400,400)
    y = random.randint(-400,400)
    penup()
    goto(x,y)
    pendown()
    snow_flake(size)