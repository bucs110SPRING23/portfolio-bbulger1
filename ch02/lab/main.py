#PART A
import random
import turtle

colorlist = ["red", "purple", "aqua", "orange", "green", "blue", "pink", "gray"]
shapelist = ["arrow", "turtle", "circle", "square", "triangle", "classic"]

screen = turtle.Screen()
turtle1 = turtle.RawPen(screen)
turtle2 = turtle.RawTurtle(screen)
turtles = [turtle1, turtle2]
for thisturtle in turtles:
    thisturtle.penup()
    thisturtle.shape(random.choice(shapelist))
    thisturtle.color(random.choice(colorlist))
    thisturtle.speed("slowest")

turtle1.goto(-100, 20)
turtle2.goto(-100, -20)

#race 1

for thisturtle in turtles:
    thisturtle.pendown()
    thisturtle.forward(random.randrange(1,100))

turtle1.goto(-100,20)
turtle2.goto(-100,-20)
for thisturtle in turtles:
    thisturtle.clear()
    thisturtle.penup()

#race 2
for thisturtle in turtles:
    thisturtle.pendown()

for _ in range(10):
    for thisturtle in turtles:
        thisturtle.forward(random.randrange(1,10))

turtle1.goto(-100,20)
turtle2.goto(-100,-20)

#PART B
import pygame
import math
pygame.init()

while 1:
    pygame.event.get()

    screen2 = pygame.display.set_mode()

    sidessequence = [3, 4, 6, 20, 100, 360]
    possiblethickness = [0, 1, 2]
    bgcolor = [random.randrange(0,100), random.randrange(0,100), random.randrange(0,100)]
    screen2.fill(bgcolor)
    for num_sides in sidessequence:
        points = []
        xpos = random.randrange(100, 1000)
        ypos = random.randrange(100, 200)
        color = [random.randrange(100,255), random.randrange(100,255), random.randrange(100,255)]
        side_length = random.randrange(500,1000) / num_sides
        thickness = random.choice(possiblethickness)
        intangle = 360/num_sides
        shiftangle = random.randrange(0, 45)
        for side in range(num_sides):
            angle = side * intangle + shiftangle
            print(angle)
            radians = math.radians(angle)
            print(radians)
            xpos += side_length * math.cos(radians)
            ypos += side_length * math.sin(radians)
            points.append([xpos,ypos])
        pygame.draw.polygon(screen2, color, points, thickness)
        print(points)
        pygame.display.flip()
        pygame.time.wait(2000)
        screen2.fill(bgcolor)
        pygame.display.flip()
        pygame.time.wait(2000)
    break