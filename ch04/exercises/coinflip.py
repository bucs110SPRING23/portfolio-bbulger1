import turtle
import random

screen = turtle.Screen()
turtle1 = turtle.RawTurtle(screen)
turtle.colormode(255)
newrgb = (100, 100, 100)
rchange = 10
gchange = -10
bchange = 0

yea = True
while yea:   
    sides = ["heads", "tails"]
    flip = random.choice(sides)
    if flip == "heads":
        turtle1.left(80)
    else:
        turtle1.right(80)
    turtle1.forward(50)
    if abs(turtle1.xcor()) > 325 or abs(turtle1.ycor()) > 325:
        break
    newrgb = (min(newrgb[0] + rchange, 255), max(newrgb[1] + gchange, 0), min(newrgb[2] + bchange, 255))
    turtle1.color(newrgb)
    if newrgb[0] == 255:
        rchange = -10
        gchange = 0
        bchange = 10
    if newrgb[2] == 255:
        rchange = 0
        gchange = 10
        bchange = -10
    if newrgb[1] == 255:
        rchange = 10
        gchange = -10
        bchange = 0
