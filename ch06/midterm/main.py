import turtle
import random
import math

def uservalues():
    '''
    accepts user inputs for drawing settings
    args: None
    return: (list) inputvars - list containing (string) file, (int) speed, (int) resolution, (int) angle, (string) mode
    '''
    uservalues = [["Enter filename. (File must be in midterm folder. (Defaults to img_sunset.txt)", "Filename: ", "img_sunset.txt"],
                  ["Select drawing speed. (Specifically the number of movements that occur each frame. Very high speeds may cause lag.) (Default: 100)", "Speed: ", 100],
                  ["Select a resolution. Greater resolution creates less detail but will render faster. (Default: 1)", "Resolution: ", 1],
                  ["Select angle for pen rotation (1-179). Greater angles will generate tighter lines but draw slower. (Only applies to chaotic mode) (Default: 135)", "Angle: ", 135],
                  ["Select either chaotic or simple. (Enter number)\n 1. Chaotic - Unpredictable motion! o_0\n 2. Simple - Simple pixel layout.", "Mode: ", "1"]]
    inputvars = []
    for description, inputmsg, default in uservalues:
        print(description)
        inputvar = input(inputmsg)
        if inputvar == "": inputvar = default
        inputvars.append(inputvar)
    inputvars = [inputvars[0], int(inputvars[1]), int(inputvars[2]), int(inputvars[3]), inputvars[4]]
    return inputvars

def fileprocessor(filename):
    '''
    opens file and generates list of values
    args: None
    return: (list) imgdata - list containing color data needed to draw image
    '''
    filepath = "ch06/midterm/" + filename
    file = open(filepath, "r")
    imgdata = file.read()
    imgdata = imgdata.split()
    imgdata = tuple(imgdata)
    file.close()
    return imgdata

def turtlesetup(speed, resolution, mode):
    '''
    sets up turtle screen and pen
    args: (int) speed - number of pen movements that will occur per second, (int) resolution - size of pen lines
    return: (turtle.Turtle) pen - pen that will be used to draw image
    '''
    screen = turtle.Screen()
    turtle.colormode(255)
    turtle.tracer(speed, 0)
    pen = turtle.RawTurtle(screen)
    pen.speed(0)
    pen.color("white")
    pen.width(resolution)
    if mode != "1" and mode != "2": 
        print("Invalid input.") 
        exit()
    if mode == "2": 
        pen.penup()
        pen.goto(-300, -300)
        pen.pendown()
    return pen

def motion_chaotic(pen, angle):
    '''
    controls the motion of the pen, causing it to move forward and then rotate randomly each step
    args: (turtle.Turtle) pen - pen to move, (int or float) angle - angle to rotate after each movement
    return: None
    '''
    choice = random.choice([0, 1])
    if choice == 1:
        pen.right(angle)
    else: pen.left(angle)
    pen.forward(50)
    if abs(pen.xcor()) > 300 or abs(pen.ycor()) > 300:
        pen.penup()
        pen.goto(random.randrange(-250, 250), random.randrange(-300, 300))
        pen.pendown()

def motion_simple(pen, resolution):
    '''
    alternate motion that causes the pen to draw straight across each line 
    args: (turtle) pen - pen to move, (int) resolution - thickness of turtle/spacing between each line
    return: None
    '''
    if pen.xcor() >= 300:
        pen.penup()
        pen.goto(-300, pen.ycor() + resolution)
        pen.pendown()
    else: pen.forward(resolution)

def color(pen, imgdata):
    '''
    controls color of pen based on location using data from external file
    args: (turtle) pen - pen to control, (list) imgdata - color data for image, should be created by fileprocessor function from a .txt file
    return: None
    '''
    x = int(pen.xcor())
    y = int(pen.ycor())
    for n in range(0, len(imgdata), 14):
        shape = imgdata[n]
        if shape == "rect":
            x1 = int(imgdata[n+1])
            x2 = int(imgdata[n+2])
            y1 = int(imgdata[n+3])
            y2 = int(imgdata[n+4])
            rgbvalue = [int(imgdata[n+5]), int(imgdata[n+8]), int(imgdata[n+11])]
            rgbxshift = [int(imgdata[n+6]), int(imgdata[n+9]), int(imgdata[n+12])]
            rgbyshift = [int(imgdata[n+7]), int(imgdata[n+10]), int(imgdata[n+13])]
            if x >= x1 and x <= x2 and y >= y1 and y <= y2:
                rgbresult = []
                for c in range(3):
                    xshift = (x - x1)/(x2 - x1)
                    yshift = (y - y1)/(y2 - y1)
                    rgbresult.append(round(min(255, max(0, rgbvalue[c] + (xshift * rgbxshift[c]) + (yshift * rgbyshift[c])))))
                pen.color(rgbresult[0], rgbresult[1], rgbresult[2])
        if shape == "circ":
            x1 = int(imgdata[n+1])
            y1 = int(imgdata[n+2])
            r = int(imgdata[n+3])
            t1 = int(imgdata[n+4])
            t2 = int(imgdata[n+5])
            rgbvalue = [int(imgdata[n+6]), int(imgdata[n+8]), int(imgdata[n+10])]
            rgbrshift = [int(imgdata[n+7]), int(imgdata[n+9]), int(imgdata[n+11])]
            dist = math.hypot(x - x1, y - y1)
            angle = math.degrees(math.atan2(y - y1, x - x1))
            if angle < 0: angle += 360
            if dist <= r and angle >= t1 and angle <= t2:
                rgbresult = []
                for c in range(3):
                    rshift = dist/r
                    rgbresult.append(round(min(255, max(0, rgbvalue[c] + (rshift * rgbrshift[c])))))
                pen.color(rgbresult[0], rgbresult[1], rgbresult[2])
        if y > 300: pen.color("white")


def main():
    
    filename, speed, resolution, angle, mode = uservalues()
    imgdata = fileprocessor(filename)
    pen = turtlesetup(speed, resolution, mode)
    
    while 1:
        color(pen, imgdata)
        if mode == "1":
            motion_chaotic(pen, angle)
        if mode == "2":
            motion_simple(pen, resolution)

main()