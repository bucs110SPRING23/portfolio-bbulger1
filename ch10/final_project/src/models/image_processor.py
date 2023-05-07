import pygame
import sys

class ImageProcessor():
    def do():
        sprite = pygame.sprite.Sprite("assets/random.jpeg")
        pygame.init()
        pygame.display.set_mode(500, 500)

        while 1:
            pygame.sprite.RenderPlain(sprite)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

ImageProcessor.do()