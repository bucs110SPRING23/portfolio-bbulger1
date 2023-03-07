import turtle

sides = input("How many sides do you want? ")
sides = int(sides)
length = input("How long should each side be? ")
length = int(length)

angle = 360 / sides
sidescounter = sides

screen = turtle.Screen()
pen1 = turtle.RawTurtle(screen)
while sidescounter > 0:
    pen1.forward(length)
    pen1.right(angle)
    sidescounter -= 1