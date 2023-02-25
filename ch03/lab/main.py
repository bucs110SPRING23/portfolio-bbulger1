#PART A
import pygame
import random
import math

pygame.init()

while 1:
    pygame.event.get()

    screen = pygame.display.set_mode()
    screensizevariable = pygame.display.get_window_size()
    screenwidth = screensizevariable[0]
    screenheight = screensizevariable[1]
    screen.fill("dark blue")

    pygame.draw.circle(screen, "orange", [(screenwidth/2),(screenheight/2)], screenheight/2)
    pygame.draw.circle(screen, "black", [(screenwidth/2),(screenheight/2)], screenheight/2, 1)
    pygame.draw.line(screen, "black", [screenwidth/2, 0], [screenwidth/2, screenheight], 1)
    pygame.draw.line(screen, "black", [(screenwidth/2) - (screenheight/2),(screenheight/2)], [(screenwidth/2) + (screenheight/2),(screenheight/2)], 1)
    pygame.display.flip()
    pygame.time.wait(1000)

    score = 0
    
#PART B
    for _ in range(10):
        dartx = random.randrange(0,screenwidth)
        darty = random.randrange(0,screenheight)
        distancefromcenter = math.hypot(dartx - (screenwidth/2), darty - (screenheight/2))
        isincircle = distancefromcenter <= (screenheight/2)
        if isincircle:
            for _ in range(3):
                pygame.draw.circle(screen, "dark green", [dartx, darty], 4, 1)
                pygame.display.flip()
                pygame.time.wait(100)
                pygame.draw.circle(screen, "black", [dartx, darty], 4, 1)
                pygame.display.flip()
                pygame.time.wait(100)
                score += 1
        else:
            for _ in range(3):
                pygame.draw.circle(screen, "red", [dartx, darty], 4, 1)
                pygame.display.flip()
                pygame.time.wait(100)
                pygame.draw.circle(screen, "white", [dartx, darty], 4, 1)
                pygame.display.flip()
                pygame.time.wait(100)
        pygame.time.wait(500)

    # pygame.font.init
    # text = pygame.font.SysFont("Helvetica", 32)
    # message = "Final score: " + str(score) + " / 10"
    # rendersurface = text.render(message, False, "white", "black")
    # screen.blit(rendersurface, [64, 64])
    # pygame.time.wait(4000)

    break