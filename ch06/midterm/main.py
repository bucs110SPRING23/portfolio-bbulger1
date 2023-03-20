import turtle
import random
import math

def uservalues():
    '''
    accepts user inputs for drawing settings
    args: None
    return: (int) speed, (int) resolution, (int) angle, (string) mode
    '''
    print("Select drawing speed. (Specifically the number of movements that occur each frame. Very high speeds may cause lag.) (Default: 100)")
    speed = input("Speed: ")
    if speed == "": speed = 100
    print("Select a resolution. Greater resolution creates less detail but will render faster. (Default: 1)")
    resolution = input("Resolution: ")
    if resolution == "": resolution = 1
    else: resolution = int(resolution)
    print("Select angle from 1 - 179. Default angle is 135. Greater angles will generate tighter lines but draw slower. (Only applies to chaotic mode) (Default: 135)")
    angle = input("Angle: ")
    if angle == "": angle = 135
    else: angle = int(angle)
    print("Select either chaotic or simple. (Enter number)")
    print("1. Simple - Simple pixel layout.")
    print("2. Chaotic - Less predictable, will likely be slower but produce more interesting results.")
    mode = input("Mode: ")
    if mode == "": mode = "2"
    return speed, resolution, angle, mode

def fileprocessor():
    '''
    opens file and generates list of values
    args: None
    return: (list) imgdata
    '''
    filepath = "ch06/midterm/img_simplegradient.txt"
    file = open(filepath, "r")
    imgdata = file.read()
    imgdata = imgdata.split()
    imgdata = tuple(imgdata)
    file.close()
    return imgdata

def motion(pen, resolution, angle):
    '''
    controls the motion of the pen, causing it to move forward and then rotate randomly each step
    args: (turtle) pen to move, (int) thickness of turtle, (int or float) angle to rotate after each movement
    return: None
    '''
    choice = random.choice([0, 1])
    if choice == 1:
        pen.right(angle)
    else: pen.left(angle)
    pen.forward(50)
    if abs(pen.xcor()) > 300 or abs(pen.ycor()) > 300:
        pen.penup()
        pen.goto(random.randrange(-300, 300), random.randrange(-300, 300))
        pen.pendown()

def altmotion(pen, resolution):
    '''
    alternate motion that causes the pen to draw straight across each line 
    args: (turtle) pen to move, (int) thickness of turtle/spacing between each line
    return: None
    '''
    if pen.xcor() >= 300 and pen.ycor() < 300:
        pen.penup()
        pen.goto(-300, pen.ycor() + resolution)
        pen.pendown()
    elif pen.ycor() < 300: pen.forward(resolution)

def color(pen):
    '''
    controls color of pen based on location
    args: (turtle) pen to control
    return: None
    '''
    x = int(pen.xcor())
    y = int(pen.ycor())
    if y <= -5:
        pen.color(max(0, round(255 + (y/4))), max(0, round(233 + (y/3))), max(0, round(208 + (y/2))))
    elif y <= 5 and y > -5:
        pen.color([255, 255, 255])
    elif y <= 100 and y > 5:
        pen.color(max(0, round(128 - (y))), max(0, round(252 - (y*2))), 255)
    elif y > 100:
        distancefromcenter = math.hypot(x, y - 100)
        if distancefromcenter < 100:
            pen.color([255, 240, 100])
        else: pen.color([max(0, round(280 - y/4 - abs(x)/4)), min(255, round(y * 0.8 + abs(x * 0.1))), min(255, round(2*y))])

def advcolor(pen, imgdata):
    '''
    controls color of pen based on location using data from external file
    args: (turtle) pen to control, (list) image data, should be created by fileprocessor function
    return: None
    '''
    x = int(pen.xcor())
    y = int(pen.ycor())
    for x in range(0, len(imgdata), 14):
        shape = imgdata[x]
        if shape == "rect":
            x1 = int(imgdata[x+1])
            x2 = int(imgdata[x+2])
            y1 = int(imgdata[x+3])
            y2 = int(imgdata[x+4])
            Rvalue = int(imgdata[x+5])
            Rxshift = float(imgdata[x+6])
            Ryshift = float(imgdata[x+7])
            Gvalue = int(imgdata[x+8])
            Gxshift = float(imgdata[x+9])
            Gyshift = float(imgdata[x+10])
            Bvalue = int(imgdata[x+11])
            Bxshift = float(imgdata[x+12])
            Byshift = float(imgdata[x+13])
            if x >= x1 and x < x2 and y >= y1 and y < y2:
                pen.color([round(min(255, max(0, Rvalue + (abs(x) * Rxshift) + (abs(y) * Ryshift)))), round(min(255, max(0, Gvalue + (abs(x) * Gxshift) + (abs(y) * Gyshift)))), round(min(255, max(0, Bvalue + (abs(x) * Bxshift) + (abs(y) * Byshift))))])
            else:
                pen.color([255,255,255])

def main():
    
    speed, resolution, angle, mode = uservalues()
    imgdata = fileprocessor()

    screen = turtle.Screen()
    turtle.colormode(255)
    turtle.tracer(speed, 0)
    pen = turtle.RawTurtle(screen)
    pen.speed(3)
    pen.width(resolution)
    if mode != "2" and mode != "1": 
        print("Invalid input.") 
        exit()
    if mode == "1": 
        pen.penup()
        pen.goto(-300, -300)
        pen.pendown()
    while 1:
        advcolor(pen, imgdata)
        #color(pen)
        if mode == "2":
            motion(pen, resolution, angle)
        if mode == "1":
            altmotion(pen, resolution)

main()