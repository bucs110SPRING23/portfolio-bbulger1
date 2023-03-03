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
    gamefont = pygame.font.Font(pygame.font.get_default_font(), 64)
    gamefont.set_italic(True)
    istext = False
    
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
        #Text
        if istext:
            fontsurface = currentfont.render(message, False, currentfontcolor, currentfontbg)
            screen.blit(fontsurface, fontcoords)

        #Flip
        pygame.display.flip()

        #Gameplay/Anim
        if phase == 0:
            targetpos[1] -= (targetpos[1] - screensize[1]/2) * 0.02
            if screencolor[2] < 139:
                screencolor = (0, 0, screencolor[2] + 1)
            if targetpos[1] < (screensize[1]/2 + 1): 
                phase = 1
        if phase == 1:
            targetpos[1] = screensize[1]/2
            istext = True
            currentfont = gamefont
            currentfontcolor = "white"
            currentfontbg = False
            fontcoords = (targetpos[0] - 128, targetpos[1] - 32)
            message = "DARTS"
            currentframe = frame
            if frame == currentframe + 2000:
                phase = 2
        if phase == 2: 
            break

        frame += 1

    break
