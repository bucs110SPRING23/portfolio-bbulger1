import pygame
import random
import src.utility as utility

class View:
    def __init__(self, colors):
        pygame.init()
        self.util = utility.Utility()
        self.screen = pygame.display.set_mode([self.util.WINDOW_SIZE, self.util.WINDOW_SIZE])
        self.colors = colors
        self.target_colors = colors

    def background(self):

        # for n1 in range(5):
        #     for n2 in range(3):
        #         if abs(self.target_colors[n1][n2] - self.colors[n1][n2]) <= 0.1:
        #             self.target_colors[n1][n2] = self.colors[(n1+1)%5][n2]
        #         else:
        #             self.colors[n1][n2] += 0.01 * (self.target_colors[n1][n2] - self.colors[n1][n2])

        # for n in range(int(self.util.PIXEL_COUNT)):
        #     y = n * self.util.PIXEL_SIZE
        #     for m in range(int(self.util.PIXEL_COUNT)):
        #         x = m * self.util.PIXEL_SIZE
        #         color = self.colors[(n+m)%5]
        #         pygame.draw.rect(self.screen, color, [x, y, x + self.util.PIXEL_SIZE, y + self.util.PIXEL_SIZE])

        for color in self.colors:
            pygame.draw.rect(self.screen, color, [random.randrange(-10, 500), random.randrange(-10, 500), random.randrange(0, 510), random.randrange(0, 510)])
        
        # pygame.display.flip()