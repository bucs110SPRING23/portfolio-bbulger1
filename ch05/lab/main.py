import pygame
import sys

def threenp1(n):
    count = 0
    while n > 1.0:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(3 * n + 1)
        count += 1
    return count

def threenp1range(upper_limit):
    objs_in_sequence = {}
    for n in range(2, upper_limit + 1):
        count = threenp1(n)
        objs_in_sequence.update({n: count})
    return objs_in_sequence

def graph_coordinates(threenplus1_iters_dict, display):
    coordinates = list(threenplus1_iters_dict.items())
    pygame.draw.lines(display, "blue", False, coordinates)
    new_display = pygame.transform.flip(display, False, True)
    width, height = new_display.get_size()
    new_display = pygame.transform.scale(display, (width * 2, height * 2))
    display.blit(new_display, (0,0))
    pygame.display.flip()

def main():
    n = 500
    objs_in_sequence = threenp1range(n)
    pygame.init()
    display = pygame.display.set_mode([1000, 750])
    while 1:
        display.fill("black")
        graph_coordinates(objs_in_sequence, display)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

main()