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