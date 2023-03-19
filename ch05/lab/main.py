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
    max_so_far = 0
    for n in range(2, upper_limit + 1):
        count = threenp1(n)
        if count > max_so_far: 
            max_so_far = count
            max_at_n = n
        objs_in_sequence.update({n : count})
    return objs_in_sequence, max_so_far, max_at_n

def graph_coordinates(threenplus1_iters_dict, max, display, n, max_at_n):
    coordinates = list(threenplus1_iters_dict.items())
    pygame.draw.lines(display, "blue", False, coordinates)
    width, height = display.get_size()
    new_display = pygame.transform.scale(display, (width * min(10, 1000/n), height * min(10, 500/max)))
    display.blit(new_display, (0,0))
    new_display = pygame.transform.flip(display, False, True)
    display.blit(new_display, (0,0))
    font = pygame.font.Font(None, 64)
    msg = font.render("Max Count: " + str(max) + " (at n = " + str(max_at_n) + ")", False, "white", "black")
    display.blit(msg, (8, 8))
    msg = font.render("Calculated up to n = " + str(n), False, "white", "black")
    display.blit(msg, (8, 72))
    pygame.display.flip()

def main():
    try: n = int(input("Max n value: "))
    except ValueError: n = 1000
    objs_in_sequence, max, max_at_n = threenp1range(n)
    pygame.init()
    display = pygame.display.set_mode([1000, 750])
    while 1:
        display.fill("black")
        graph_coordinates(objs_in_sequence, max, display, n, max_at_n)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

main()