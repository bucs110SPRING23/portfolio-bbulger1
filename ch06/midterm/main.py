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
    if pen.xcor() >= 300 and pen.ycor() < 300:
        pen.penup()
        pen.goto(-300, pen.ycor() + resolution)
        pen.pendown()
    elif pen.ycor() < 300: pen.forward(resolution)

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
    
    print("Select drawing speed. (Specifically the number of movements that occur each frame. Very high speeds may cause lag.)")
    speed = input("Speed: ")
    print("Select a resolution. Greater resolution creates less detail but will render faster. (Maximum: 35)")
    resolution = int(input("Resolution: "))
    # print("Select either chaotic or simple. (Enter number)")
    # print("1. Simple - Simple pixel layout.")
    # print("2. Chaotic - Less predictable, will likely be slower but produce more interesting results.")
    mode = "2"#input("Mode: ")

    screen = turtle.Screen()
    turtle.colormode(255)
    turtle.tracer(speed, 0)
    pen = turtle.RawTurtle(screen)
    pen.speed(0)
    pen.width(resolution)
    if mode != "2" and mode != "1": 
        print("Invalid input.") 
        exit()
    if mode == "1": 
        pen.penup()
        pen.goto(-300, -300)
        pen.pendown()
    while 1:
        color(pen)
        if mode == "2":
            motion(pen, resolution)
        if mode == "1":
            altmotion(pen, resolution)

main()