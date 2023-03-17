import turtle

def main():
    screen = turtle.Screen()
    newturtle = turtle.RawTurtle(screen)
    turtle.tracer(16, 0)
    for x in range(1000):
        execution(newturtle, x)
    screen.mainloop()

def execution(newturtle, x):
    newturtle.forward(x)
    newturtle.left(15)

main()