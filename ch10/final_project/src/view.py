import pygame
import random
import src.utility as utility

class View:
    def __init__(self):
        self.util = utility.Utility()
        pygame.init()
        self.screen = pygame.display.set_mode([self.util.WINDOW_SIZE, self.util.WINDOW_SIZE])

    def background(self, colors):
        for n in range(int(self.util.PIXEL_COUNT)):
            y = n * self.util.PIXEL_SIZE
            for m in range(int(self.util.PIXEL_COUNT)):
                x = m * self.util.PIXEL_SIZE
                color = colors[(n+m)%5]
                pygame.draw.rect(self.screen, color, [x, y, x + self.util.PIXEL_SIZE, y + self.util.PIXEL_SIZE])