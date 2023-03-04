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
    phase = "intro"
    screencolor = (0, 0, 0, 255)
    targetradius = (screensize[1]/2) * 0.75
    targetpos = [screensize[0]/2, screensize[1]/2 + 1000]
    titlefont = pygame.font.Font(pygame.font.get_default_font(), 256) 
    gamefont = pygame.font.Font(pygame.font.get_default_font(), 32)
    titlefont.set_italic(True)
    messages = []
    targetframe = 0
    
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
        #Dart
        #Text
        for currentfont, currentfontcolor, currentfontbg, fontcoords, message in messages:
            fontsurface = currentfont.render(message, False, currentfontcolor, currentfontbg)
            screen.blit(fontsurface, fontcoords)

        #Flip
        pygame.display.flip()

        #Gameplay/Anim
        if phase == "intro":
            targetpos[1] -= (targetpos[1] - screensize[1]/2) * 0.02
            if screencolor[2] < 139:
                screencolor = (0, 0, screencolor[2] + 1)
            if targetpos[1] < (screensize[1]/2 + 0.5): 
                phase = "title"
                phasestart = True
        elif phase == "title":
            if phasestart == True:
                targetpos[1] = screensize[1]/2
                for x in range(16):
                    msg = [titlefont, "black", None, (8 + x, 8 + x), "DARTS"]
                    messages.append(msg)
                msg = [titlefont, "white", None, (8,8), "DARTS"]
                messages.append(msg)
                if targetframe == 0: targetframe = frame
                phasestart = False
            if frame > (targetframe + 180):
                    adjustsize = gamefont.size("Press SPACE to start.")
                    msg = [gamefont, "white", "black", (screensize[0]/2 - adjustsize[0]/2, screensize[1]/2 - adjustsize[1]/2), "Press SPACE to start."]
                    messages.append(msg)
                    targetframe = 0
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                phase = "player 1 turn intro"
            
        elif phase == "player 1 turn intro": 
            messages = []
            adjustsize = gamefont.size("Player 1's turn.")
            msg = [gamefont, "white", "black", (screensize[0]/2 - adjustsize[0]/2, screensize[1]/2 - adjustsize[1]/2), "Player 1's turn."]
            messages.append(msg)
            if targetframe == 0: targetframe = frame
            if frame > (targetframe + 300):
                phase = "player 1 turn"
                targetframe = 0
        elif phase == "player 1 turn":
            msg = False
            drawdart = True
            phase = "game end"
        elif phase == "game end":
            break

        frame += 1

    break
