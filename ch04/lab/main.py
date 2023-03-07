import pygame
import sys
import random
import math

pygame.init()
frame = 1

while 1:
    pygame.event.pump()

    end = False
    screen = pygame.display.set_mode([1000, 750])
    screensize = pygame.display.get_window_size()

    #Setup - these are just a bunch of random variables that become important later but need to be set from the start
    phase = "intro"
    screencolor = (0, 0, 0, 255)
    targetradius = (screensize[1]/2) * 0.75
    targetpos = [screensize[0]/2, screensize[1]/2 + 1000]
    titlefont = pygame.font.Font(pygame.font.get_default_font(), 256) 
    gamefont = pygame.font.Font(pygame.font.get_default_font(), 32)
    hitfont = pygame.font.Font(pygame.font.get_default_font(), 128)
    titlefont.set_italic(True)
    hitfont.set_italic(True)
    messages = []
    targetframe = 0
    ready2start = False
    drawdart = False
    dartpos = [-10, -10]
    dartpos1 = [-10, -10]
    pygame.mouse.set_visible(False)
    hits = []
    drawcursor = False
    rounds = 0
    player1score = 0
    player2score = 0
    buttons = []
    selection = 0
    drawselectcursor = False
    
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
        #Hits
        for pos, playercolor in hits:
            pygame.draw.circle(screen, playercolor, pos, 2, 1)
            pygame.draw.circle(screen, playercolor, pos, 4, 1)
        #Buttons
        for buttoncolor, buttonrect in buttons:
            pygame.draw.rect(screen, buttoncolor, buttonrect)
        #Cursor
        if drawcursor:
            pygame.draw.circle(screen, dartcolor, cursorpos, 8, 1)
            pygame.draw.line(screen, dartcolor, [cursorpos[0] - 8,cursorpos[1]], [cursorpos[0] + 8,cursorpos[1]])
            pygame.draw.line(screen, dartcolor, [cursorpos[0],cursorpos[1] - 8], [cursorpos[0],cursorpos[1] + 8])
        if drawselectcursor:
            pygame.draw.circle(screen, "white", cursorpos, 4, 1)
        #Dart
        if drawdart:
            #calc stuff
            if dartpos1[0] - screensize[0]/2 == 0: adjustanglex = 0.00001
            else: adjustanglex = 0
            angle = math.atan((dartpos1[1] - screensize[1]/2)/(dartpos1[0] - screensize[0]/2 + adjustanglex)) + 90
            dartpos1 = [screensize[0]/2 + offset * (dartpos[0] - screensize[0]/2), screensize[1]/2 + offset * (dartpos[1] - screensize[1]/2)]
            dartpos2 = [screensize[0]/2 + (offset + 0.2) * (dartpos[0] - screensize[0]/2), screensize[1]/2 + (offset + 0.2) * (dartpos[1] - screensize[1]/2)]
            dartpos3 = [screensize[0]/2 + (offset + 0.5) * (dartpos[0] - screensize[0]/2), screensize[1]/2 + (offset + 0.5) * (dartpos[1] - screensize[1]/2)]
            pygame.draw.line(screen, "black", dartpos1, dartpos2, 1)
            pygame.draw.circle(screen, dartcolor, dartpos2, 6)
            pygame.draw.circle(screen, "black", dartpos2, 6, 1)
            for x in range(24):
                dartpos4 = [dartpos2[0] + (x/4) * math.cos(angle), dartpos2[1] + (x/4) * math.sin(angle)]
                dartpos5 = [dartpos2[0] - (x/4) * math.cos(angle), dartpos2[1] - (x/4) * math.sin(angle)]
                dartpos6 = [dartpos3[0] + (x/2) * math.cos(angle), dartpos3[1] + (x/2) * math.sin(angle)]
                dartpos7 = [dartpos3[0] - (x/2) * math.cos(angle), dartpos3[1] - (x/2) * math.sin(angle)]
                pygame.draw.line(screen, dartcolor, dartpos4, dartpos6, 2)
                pygame.draw.line(screen, dartcolor, dartpos5, dartpos7, 2)
            dartpos4 = [dartpos2[0] + 6 * math.cos(angle), dartpos2[1] + 6 * math.sin(angle)]
            dartpos5 = [dartpos2[0] - 6 * math.cos(angle), dartpos2[1] - 6 * math.sin(angle)]
            dartpos6 = [dartpos3[0] + 12 * math.cos(angle), dartpos3[1] + 12 * math.sin(angle)]
            dartpos7 = [dartpos3[0] - 12 * math.cos(angle), dartpos3[1] - 12 * math.sin(angle)]
            pygame.draw.line(screen, "black", dartpos4, dartpos6, 1)
            pygame.draw.line(screen, "black", dartpos5, dartpos7, 1)
            pygame.draw.circle(screen, dartcolor, dartpos3, 12)
            pygame.draw.circle(screen, "black", dartpos3, 12, 1)
        #Text
        for currentfont, currentfontcolor, currentfontbg, fontcoords, message in messages:
            fontsurface = currentfont.render(message, False, currentfontcolor, currentfontbg)
            screen.blit(fontsurface, fontcoords)

        #Flip
        pygame.display.flip()

        #Gameplay/Anim
        if phase == "intro":
            targetpos[1] -= (targetpos[1] - screensize[1]/2) * 0.02
            if screencolor[2] < 200:
                screencolor = (0, 0, screencolor[2] + 1)
            if targetpos[1] < (screensize[1]/2 + 0.5): 
                phase = "title"
                phasestart = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        phase = "title"
                        phasestart = True
        elif phase == "title":
            if phasestart == True:
                targetpos[1] = screensize[1]/2
                screencolor = (0, 0, 200, 255)
                for x in range(16):
                    msg = [titlefont, "black", None, (8 + x, 8 + x), "DARTS"]
                    messages.append(msg)
                msg = [titlefont, "white", None, (8,8), "DARTS"]
                messages.append(msg)
                if targetframe == 0: targetframe = frame
                phasestart = False
            if frame > (targetframe + 180):
                adjustsize = gamefont.size("Press ENTER to begin.")
                msg = [gamefont, "white", "black", (screensize[0]/2 - adjustsize[0]/2, screensize[1]/2 - adjustsize[1]/2), "Press ENTER to begin."]
                messages.append(msg)
                ready2start = True
                targetframe = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if ready2start:
                            phase = "bet"
                        else:
                            frame = targetframe + 180
        elif phase == "bet":
            messages = []
            buttons = []
            drawselectcursor = True
            cursorpos = pygame.mouse.get_pos()
            if selection == 0:
                adjustsize = gamefont.size("Predict which player will win!")
                msg = [gamefont, "white", "black", [screensize[0]/2 - adjustsize[0]/2, 16], "Predict which player will win!"]
                messages.append(msg)
                for x in range(8):
                    button = ["black", [screensize[0]/4 - 128 + x, screensize[1]/2 - 128 + x, 256, 256]]
                    buttons.append(button)
                    button = ["black", [3 * (screensize[0]/4) - 128 + x, screensize[1]/2 - 128 + x, 256, 256]]
                    buttons.append(button)
                button = ["cyan", [screensize[0]/4 - 128, screensize[1]/2 - 128, 256, 256]]
                buttons.append(button)
                button = ["magenta", [3 * (screensize[0]/4) - 128, screensize[1]/2 - 128, 256, 256]]
                buttons.append(button)
            elif selection == 1:
                drawselectcursor = False
                for x in range(4):
                    button = ["black", [screensize[0]/4 - 124 + x, screensize[1]/2 - 124 + x, 256, 256]]
                    buttons.append(button)
                    button = ["black", [3 * (screensize[0]/4) - 128 + x, screensize[1]/2 - 128 + x, 256, 256]]
                    buttons.append(button)
                button = ["yellow", [screensize[0]/4 - 124, screensize[1]/2 - 124, 256, 256]]
                buttons.append(button)
                button = ["grey", [3 * (screensize[0]/4) - 128, screensize[1]/2 - 128, 256, 256]]
                buttons.append(button)
                if targetframe == 0: targetframe = frame
                if frame == targetframe + 180:
                    phase = "player turn intro"
                    player = 1
                    phasestart = True
            elif selection == 2:
                drawselectcursor = False
                for x in range(4):
                    button = ["black", [screensize[0]/4 - 128 + x, screensize[1]/2 - 128 + x, 256, 256]]
                    buttons.append(button)
                    button = ["black", [3 * (screensize[0]/4) - 124 + x, screensize[1]/2 - 124 + x, 256, 256]]
                    buttons.append(button)
                button = ["grey", [screensize[0]/4 - 128, screensize[1]/2 - 128, 256, 256]]
                buttons.append(button)
                button = ["yellow", [3 * (screensize[0]/4) - 124, screensize[1]/2 - 124, 256, 256]]
                buttons.append(button)
                if targetframe == 0: targetframe = frame
                if frame == targetframe + 180:
                    phase = "player turn intro"
                    player = 1
                    targetframe = 0
                    phasestart = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT and selection == 0:
                        if cursorpos[0] > screensize[0]/4 - 128 and cursorpos[0] < screensize[0]/4 + 128 and cursorpos[1] > screensize[1]/2 - 128 and screensize[1]/2 + 128:
                            selection = 1
                        elif cursorpos[0] > 3 * screensize[0]/4 - 128 and cursorpos[0] < 3 * screensize[0]/4 + 128 and cursorpos[1] > screensize[1]/2 - 128 and screensize[1]/2 + 128:
                            selection = 2
        elif phase == "player turn intro": 
            messages = []
            buttons = []
            if player == 1: 
                playermessage = "Player 1's turn."
                fontcolor = "cyan"
            else: 
                playermessage = "Player 2's turn"
                fontcolor = "magenta"
            adjustsize = gamefont.size(playermessage)
            msg = [gamefont, fontcolor, "black", (screensize[0]/2 - adjustsize[0]/2, screensize[1]/2 - adjustsize[1]/2), playermessage]
            messages.append(msg)
            if targetframe == 0: targetframe = frame
            if frame > (targetframe + 180):
                phase = "player turn"
                targetframe = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        elif phase == "player turn":
            messages = []
            drawdart = True
            drawcursor = True
            cursorpos = pygame.mouse.get_pos()
            dartpos = [dartpos[0] + 0.05 * (cursorpos[0] - dartpos[0]), dartpos[1] + 0.05 * (cursorpos[1] - dartpos[1])]
            offset = 2
            if player == 1: dartcolor = "cyan"
            else: dartcolor = "magenta"
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        phase = "player throw"
                        phasestart = True
        elif phase == "player throw":
            if phasestart:
                phasestart = False
                drawdart = True
                drawcursor = False
                dartpos = cursorpos
                offset = 1
                if player == 1: dartcolor = "cyan"
                else: dartcolor = "magenta"
                currenthit = [dartpos, dartcolor]
                hits.append(currenthit)
                distancefromcenter = math.hypot(dartpos[0] - (screensize[0]/2), dartpos[1] - (screensize[1]/2))
                isincircle = distancefromcenter <= (screensize[1]/2) * 0.75
                if isincircle: 
                    hittextcolor = [0, 255, 0, 255]
                    adjustsize = hitfont.size("HIT!")
                else: 
                    hittextcolor = [255, 0, 0, 255]
                    adjustsize = hitfont.size("MISS!")
                if dartpos[1] < 256:
                    hittextpos = [dartpos[0] - adjustsize[0]/2, dartpos[1]]
                    hittexttargetpos = [dartpos[0] - adjustsize[0]/2, dartpos[1] + 100]
                else:
                    hittextpos = [dartpos[0] - adjustsize[0]/2, dartpos[1] - 100]
                    hittexttargetpos = [dartpos[0] - adjustsize[0]/2, dartpos[1] - 200]
            messages = []
            if isincircle:
                msg = [hitfont, hittextcolor, None, hittextpos, "HIT!"]
                messages.append(msg)
            else:
                msg = [hitfont, hittextcolor, None, hittextpos, "MISS!"]
                messages.append(msg)
            hittextpos = [hittextpos[0], hittextpos[1] - 0.05 * (hittextpos[1] - hittexttargetpos[1])]
            if round(hittextpos[1]) == hittexttargetpos[1]:
                if player == 1:
                    if isincircle: player1score += 1
                elif isincircle: player2score += 1
                rounds += 1
                if rounds < 10:
                    if player == 1: player = 2
                    else: player = 1
                    phase = "player turn intro"
                else:
                    phase = "game over"
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        elif phase == "game over":
            messages = []
            adjustsize = gamefont.size("GAME OVER.")
            msg = [gamefont, "white", "black", [screensize[0]/2 - adjustsize[0]/2, screensize[1]/2 - adjustsize[1]/2], "GAME OVER."]
            messages.append(msg)
            if targetframe == 0: targetframe = frame
            if frame == targetframe + 180:
                phase = "show score"
                targetframe = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        elif phase == "show score":
            messages = []
            player1scoremessage = "Player 1: " + str(player1score)
            player2scoremessage = "Player 2: " + str(player2score)
            adjustsize = gamefont.size(player1scoremessage)
            msg = [gamefont, "cyan", "black", [screensize[0]/2 - adjustsize[0]/2, screensize[1]/2 - adjustsize[1]], player1scoremessage]
            messages.append(msg)
            adjustsize = gamefont.size(player2scoremessage)
            msg = [gamefont, "magenta", "black", [screensize[0]/2 - adjustsize[0]/2, screensize[1]/2], player2scoremessage]
            messages.append(msg)
            if targetframe == 0: targetframe = frame
            if frame == targetframe + 300:
                phase = "show winner"
                targetframe = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        elif phase == "show winner":
            if player1score > player2score: 
                winner = "Player 1 wins!"
                winnercolor = "cyan"
                winnerselection = 1
            elif player2score > player1score: 
                winner = "Player 2 wins!"
                winnercolor = "magenta"
                winnerselection = 1
            else: 
                winner = "It was a tie..."
                winnercolor = "white"
            messages = []
            adjustsize = hitfont.size(winner)
            msg = [hitfont, winnercolor, "black", [screensize[0]/2 - adjustsize[0]/2, screensize[1]/2 - adjustsize[1]/2], winner]
            messages.append(msg)
            if winnerselection == selection:
                adjustsize = gamefont.size("Your prediction was correct! :D")
                msg = [gamefont, winnercolor, "black", [screensize[0]/2 - adjustsize[0]/2, screensize[1]/2 + 128], "Your prediction was correct! :D"]
                messages.append(msg)
            else:
                adjustsize = gamefont.size("Your prediction was wrong! :(")
                msg = [gamefont, winnercolor, "black", [screensize[0]/2 - adjustsize[0]/2, screensize[1]/2 + 128], "Your prediction was wrong! :("]
                messages.append(msg)
            if targetframe == 0: targetframe = frame
            if frame == targetframe + 300:
                phase = "game end"
                targetframe = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        elif phase == "game end":
            break

        frame += 1

    break
