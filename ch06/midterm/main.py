import turtle
import random
import math

def motion(pen, resolution):
    choice = random.choice([0, 1])
    if choice == 1:
        pen.right(135)
    else: pen.left(135)
    pen.forward(50)
    if abs(pen.xcor()) > 300 or abs(pen.ycor()) > 300:
        pen.penup()
        pen.goto(random.randrange(-300, 300), random.randrange(-300, 300))
        pen.pendown()

def altmotion(pen, resolution):
    # if pen.xcor() >= 300:
    #     pen.penup()
    #     pen.goto(-300, pen.ycor() + 1)
    #     pen.pendown()
    # else: 
    if pen.xcor() < 300: pen.forward(resolution)


def color(pen):
    x = int(pen.xcor())
    y = int(pen.ycor())
    if y <= -5:
        pen.color(max(0, round(255 + (y/4))), max(0, round(233 + (y/3))), max(0, round(208 + (y/2))))
    elif y <= 5 and y > -5:
        pen.color([255, 255, 255])
    elif y <= 100 and y > 5:
        pen.color([128, 252, 255])
        pen.color(max(0, round(128 - (y))), max(0, round(252 - (y*2))), 255)
    elif y > 100:
        distancefromcenter = math.hypot(x, y - 100)
        if distancefromcenter < 100:
            pen.color([255, 255, 100])
        else: pen.color([max(0, round(280 - y/4)), min(255, round(y * 0.8)), min(255, round(2*y))])

def main():
    
    print("Select a resolution. Greater resolution creates less detail but will render faster.")
    resolution = int(input("Resolution: "))
    print("Select either chaotic or simple.")
    mode = input("Mode: ")
    print("Select render speed.")
    speed = input("Speed: ")

    screen = turtle.Screen()
    turtle.colormode(255)
    pens = []
    if mode == "simple":
        for x in range(-300, 300, resolution):
            newturtle = turtle.RawTurtle(screen)
            newturtle.speed(0)
            newturtle.width(resolution)
            newturtle.hideturtle()
            newturtle.penup()
            newturtle.goto (-300, x)
            newturtle.pendown()
            pens.append(newturtle)
    if mode == "chaotic":
        newturtle = turtle.RawTurtle(screen)
        newturtle.speed(0)
        newturtle.width(resolution)
        pens.append(newturtle)
    while 1:
        for _ in speed:
            for pen in pens:
                color(pen)
                if mode == "chaotic":
                    motion(pen, resolution)
                if mode == "simple":
                    altmotion(pen, resolution)

main()