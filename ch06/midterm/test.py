import turtle

def main():
    screen = turtle.Screen()
    newturtle = turtle.RawTurtle(screen)
    execution(newturtle)

def execution(newturtle):
    newturtle.forward(100)
    newturtle.left(90)
    newturtle.forward(100)

main()
turtle.done()