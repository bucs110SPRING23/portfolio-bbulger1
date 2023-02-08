import turtle

screen = turtle.Screen()
theturtle = turtle.RawTurtle(screen)
theturtle.shape("turtle")
theturtle.color("purple")

for _ in range(4):
   theturtle.forward(50)
   theturtle.right(90)

theturtle.color("red")
theturtle.penup()
theturtle.forward(100)
theturtle.left(10)

theturtle.pendown()
for _ in range(4):
   theturtle.forward(50)
   theturtle.left(90)