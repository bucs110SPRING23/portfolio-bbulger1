import pygame
import src.utility as utility

class View:
    def __init__(self):
        '''
        init function for view
        args: self
        return: none
        '''
        self.util = utility.Utility()
        self.screen = pygame.display.set_mode([self.util.WINDOW_SIZE, self.util.WINDOW_SIZE])
        pygame.font.init()
        self.main_font = pygame.font.Font(pygame.font.get_default_font(), 16)

    def text_display(self, msg):
        '''
        displays text for program start
        args: self
        return: none
        '''
        message = self.main_font.render(msg, False, "white")
        self.screen.blit(message, [16, 16])

    def loading_display(self, msg):
        '''
        displays text for loading
        args: none
        return: none
        '''
        message = self.main_font.render(msg, False, "yellow", "black")
        self.screen.blit(message, [16, self.util.WINDOW_SIZE - 32])
        pygame.display.flip()

    def draw_coffee(self, image):
        '''
        draws coffee image on screen
        args: self, image (filepath) filepath to image to display
        return: none
        '''
        to_draw = pygame.image.load(image)
        self.screen.blit(to_draw, [0, 0])