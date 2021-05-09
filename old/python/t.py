import random
from turtle import *

number = input("how many snowflakes do you want")

shape("turtle")
speed(116)
pensize(6)
colours = ['blue', 'green', 'yellow', 'red', 'indigo']
Screen().bgcolor("DarkOrange")


def vshape(size):
    random_num = random.randint(0, 4)
    pencolor(colours[random_num])
    right(25)
    forward(size)
    backward(size)
    left(50)
    forward(size)
    backward(size)
    right(25)


def snow_flake_arm(size):
    for x in range(0, 4):
        forward(size)
        vshape(size)
    backward(size * 4)


def snow_flake(size):
    for x in range(0, 18):
        snow_flake_arm(size)
        right(20)


for i in range(0, int(number)):
    size = random.randint(5, 30)
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    penup()
    goto(x, y)
    pendown()
    snow_flake(size)