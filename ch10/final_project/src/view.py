import pygame
import random
import src.utility as utility

class View:
    def __init__(self):
        self.util = utility.Utility()
        self.screen = pygame.display.set_mode([self.util.WINDOW_SIZE, self.util.WINDOW_SIZE])
        pygame.font.init()
        self.main_font = pygame.font.Font(pygame.font.get_default_font(), 16)

    def text_display(self):
        message = self.main_font.render(self.util.MSG, False, "white")
        self.screen.blit(message, [16, 16])

    def loading_display(self):
        message = self.main_font.render(self.util.MSG2, False, "yellow", "black")
        self.screen.blit(message, [16, self.util.WINDOW_SIZE - 32])
        pygame.display.flip()

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

    def draw_coffee(self):
        to_draw = pygame.image.load("ch10/final_project/assets/final_image.jpg")
        self.screen.blit(to_draw, [0, 0])