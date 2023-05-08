import pygame
import random
import src.utility as utility

class View:
    def __init__(self):
        self.util = utility.Utility()
        self.screen = pygame.display.set_mode([self.util.WINDOW_SIZE, self.util.WINDOW_SIZE])

    def generate_background(self, colors, frame):

        for n in range(int(self.util.PIXEL_COUNT)):
            y = n * self.util.PIXEL_SIZE
            for m in range(int(self.util.PIXEL_COUNT)):
                x = m * self.util.PIXEL_SIZE
                color = colors[(n+m+frame+random.randrange(-5, 5))%5]
                pygame.draw.rect(self.screen, color, [x, y, x + self.util.PIXEL_SIZE, y + self.util.PIXEL_SIZE])

    def generate_color(self, colors, frame):
        for color in colors:
            pygame.draw.rect(self.screen, color, [random.randrange(-500, 500), random.randrange(-500, 500), random.randrange(0, 500), random.randrange(0, 500)])
        
        # pygame.display.flip()

    def clear(self):
        self.screen.fill("black")