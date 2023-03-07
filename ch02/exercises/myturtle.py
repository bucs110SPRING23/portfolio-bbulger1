import turtle

screen = turtle.Screen()
theturtle = turtle.RawTurtle(screen)
theturtle.shape("turtle")

colors = ["purple", "red", "blue", "magenta", "gray", "cyan", "green", "black", "orange"]

for color in colors:
   theturtle.color(color)
   for _ in range(4):
      theturtle.forward(50)
      theturtle.right(90)
   theturtle.penup()
   theturtle.forward(100)
   theturtle.left(80)
   theturtle.pendown()