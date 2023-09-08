import pygame
import pygame.draw
pygame.init()

while 1:
    pygame.event.get()

    dim561array = [(150, 50), (275, 100), (500, 200)]
    dim562array = [(650, 50), (525, 100), (300, 200)] 
    dim1234array = [(255, 0, 255, 325, dim561array), (0, 255, 255, 725, dim562array), (255, 255, 0, 1125, dim561array)]

    screen = pygame.display.set_mode()
    for dimR, dimG, dimB, dimx, dim56array in dim1234array:
        for dimy, dimrad in dim56array:
            pygame.time.wait(1000)
            pygame.draw.circle(screen, [dimR, dimG, dimB], [dimx, dimy], dimrad)
            pygame.display.flip()

    # following code is an unoptimized version of the same code, i made it before making the code above and am keeping it in the file as a note just so i can refer to it while editing the actual code, as what the program is "supposed" to be doing
    # id imagine the optimized version doesnt really effect any use of actual memory but it just looks nicer and was good practice for using lists/arrays/matrices :)
 
    # screen = pygame.display.set_mode()
    # pygame.time.wait(1000)
    # pygame.draw.circle(screen, [255, 0, 255], [325, 150], 50)
    # pygame.display.flip()
    # pygame.time.wait(250)
    # pygame.draw.circle(screen, [255, 0, 255], [325, 275], 100)
    # pygame.display.flip()
    # pygame.time.wait(250)
    # pygame.draw.circle(screen, [255, 0, 255], [325, 500], 200)
    # pygame.display.flip()
    # pygame.time.wait(250)
    # pygame.draw.circle(screen, [0, 225, 255], [725, 650], 50)
    # pygame.display.flip()
    # pygame.time.wait(250)
    # pygame.draw.circle(screen, [0, 225, 255], [725, 525], 100)
    # pygame.display.flip()
    # pygame.time.wait(250)
    # pygame.draw.circle(screen, [0, 225, 255], [725, 300], 200)
    # pygame.display.flip()
    # pygame.time.wait(250)
    # pygame.draw.circle(screen, [255, 225, 0], [1125, 150], 50)
    # pygame.display.flip()
    # pygame.time.wait(250)
    # pygame.draw.circle(screen, [255, 225, 0], [1125, 275], 100)
    # pygame.display.flip()
    # pygame.time.wait(250)
    # pygame.draw.circle(screen, [255, 225, 0], [1125, 500], 200)
    # pygame.display.flip()

    pygame.time.wait(2500)
    break