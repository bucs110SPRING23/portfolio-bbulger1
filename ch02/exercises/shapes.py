import pygame
import pygame.draw
pygame.init()

while 1:
    pygame.event.get()
    # this code is an attempt at a more optimized version of the same code, but i cant test it yet ;-;
    # also another note i couldve sworn i had specific colors set in this somewhere but maybe im just dumb - actually nvm i realized the color is built into the draw function as rgb values
    # also also this is definitely not going to work right but its really not gonna be possible to fix it until i get pygame working lol

    # dim1range = [255, 0, 255]
    # dim2range = [0, 255, 255]
    # dim3range = [255, 255, 0]
    # dim4range = [325, 725, 1125]
    # dim5range = [150, 275, 500, 650, 525, 300, 150, 275, 500]
    # dim6range = [50, 100, 200]

    # screen = pygame.display.set_mode()
    # for dim1 in dim1range:
    #     for dim2 in dim2range:
    #         for dim3 in dim3range:
    #             for dim4 in dim4range:
    #                 for dim5 in dim5range:
    #                     for dim6 in dim6range:
    #                         pygame.time.wait(1000)
    #                         pygame.draw.circle(screen, [dim1, dim2, dim3], [dim4, dim5], dim6)
    #                         pygame.display.flip

    # an even more confusing and scuffed attempt at using matrices to make this work maybe,

    # dim1234array = [[255, 0, 255], [0, 255, 255], [255, 255, 0], [325, 725, 1125]]
    # dim561array = [[50, 100, 200], [150, 275, 500]]
    # dim562array = [[50, 100, 200], [650, 525, 300]]
    # dim56x = [dim561array, dim562array]

    # screen = pygame.display.set_mode()
    # for dim1, dim2, dim3, dim4 in dim1234array:
    #     for dim56array in dim56x:
    #         for dim5, dim6 in dim56array:
    #             pygame.time.wait(1000)
    #             pygame.draw.circle(screen, [dim1, dim2, dim3], [dim4, dim5], dim6)
    #             pygame.display.flip

    screen = pygame.display.set_mode()
    pygame.time.wait(1000)
    pygame.draw.circle(screen, [255, 0, 255], [325, 150], 50)
    pygame.display.flip()
    pygame.time.wait(250)
    pygame.draw.circle(screen, [255, 0, 255], [325, 275], 100)
    pygame.display.flip()
    pygame.time.wait(250)
    pygame.draw.circle(screen, [255, 0, 255], [325, 500], 200)
    pygame.display.flip()
    pygame.time.wait(250)
    pygame.draw.circle(screen, [0, 225, 255], [725, 650], 50)
    pygame.display.flip()
    pygame.time.wait(250)
    pygame.draw.circle(screen, [0, 225, 255], [725, 525], 100)
    pygame.display.flip()
    pygame.time.wait(250)
    pygame.draw.circle(screen, [0, 225, 255], [725, 300], 200)
    pygame.display.flip()
    pygame.time.wait(250)
    pygame.draw.circle(screen, [255, 225, 0], [1125, 150], 50)
    pygame.display.flip()
    pygame.time.wait(250)
    pygame.draw.circle(screen, [255, 225, 0], [1125, 275], 100)
    pygame.display.flip()
    pygame.time.wait(250)
    pygame.draw.circle(screen, [255, 225, 0], [1125, 500], 200)
    pygame.display.flip()

    pygame.time.wait(10000)
    break