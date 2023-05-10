import pygame
import random
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

    def text_display(self):
        '''
        displays text for program start
        args: self
        return: none
        '''
        message = self.main_font.render(self.util.MSG, False, "white")
        self.screen.blit(message, [16, 16])

    def loading_display(self):
        '''
        displays text for loading
        args: none
        return: none
        '''
        message = self.main_font.render(self.util.MSG2, False, "yellow", "black")
        self.screen.blit(message, [16, self.util.WINDOW_SIZE - 32])
        pygame.display.flip()

    def draw_coffee(self):
        '''
        draws coffee image on screen
        args: self
        return: none
        '''
        to_draw = pygame.image.load("ch10/final_project/assets/final_image.jpg")
        self.screen.blit(to_draw, [0, 0])