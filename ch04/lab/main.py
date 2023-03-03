import pygame
import random
import math

pygame.init()
frame = 1

while 1:
    pygame.event.get()
    end = False
    screen = pygame.display.set_mode([1000, 750])
    screensize = pygame.display.get_window_size()

    #Setup
    phase = 0
    screencolor = (0, 0, 0, 255)
    targetradius = (screensize[1]/2) * 0.75
    targetpos = [screensize[0]/2, screensize[1]/2 + 1000]
    
    while 1:
        #Draw
        #BG
        screen.fill(screencolor)
        #Target
        pygame.draw.circle(screen, "black", [targetpos[0] + 8,targetpos[1] + 8], targetradius)
        pygame.draw.circle(screen, "orange", targetpos, targetradius)
        pygame.draw.circle(screen, "black", targetpos, targetradius, 1)
        pygame.draw.line(screen, "black", [targetpos[0] - targetradius,targetpos[1]], [targetpos[0] + targetradius,targetpos[1]])
        pygame.draw.line(screen, "black", [targetpos[0],targetpos[1] - targetradius], [targetpos[0],targetpos[1] + targetradius])

        #Flip
        pygame.display.flip()

        #Gameplay/Anim
        if phase == 0:
            targetpos[1] -= (targetpos[1] - screensize[1]/2) * 0.02
            if screencolor[2] < 139:
                screencolor = (0, 0, screencolor[2] + 1)
            if targetpos[1] < (screensize[1]/2 + 1): 
                phase = 1
        if phase == 1: break
        frame += 1

    break
    