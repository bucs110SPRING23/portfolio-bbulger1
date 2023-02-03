import turtle

screen = turtle.Screen()
theturtle = turtle.RawTurtle(screen)
theturtle.shape("turtle")
theturtle.color("purple")
sidecounter = 4

while sidecounter > 0:
   theturtle.forward(50)
   theturtle.right(90)
   sidecounter -= 1

theturtle.color("red")
theturtle.penup()
theturtle.forward(100)
theturtle.left(10)

theturtle.pendown()
sidecounter = 4
while sidecounter > 0:
   theturtle.forward(50)
   theturtle.left(90)
   sidecounter -= 1