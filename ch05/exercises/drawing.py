import turtle

def draw_eq_shape(num_sides, side_length):
    screen = turtle.Screen()
    pen = turtle.RawTurtle(screen)
    angle = 360 / num_sides
    for side in range(num_sides):
        pen.left(angle)
        pen.forward(side_length)

def main():
    num_sides = int(input("Number of sides: "))
    side_length = int(input("Side length: "))
    
    draw_eq_shape(num_sides, side_length)

main()