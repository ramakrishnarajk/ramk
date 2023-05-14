from turtle import *
def square():
    fd(100)
    left(90)
    fd(100)
    left(90)
    fd(100)
    left(90)
    fd(100)
def print():
    square()   
    left(45)
    fd(50)
    left(45)
    square()
    pattern()
def pattern():
    left(180)
    fd(100)
    left(45)
    fd(50)
    right(45+90)
    fd(100)
    right(45)
    fd(50)
    right(45)
    fd(100)
    right(180-45)
    fd(50)


