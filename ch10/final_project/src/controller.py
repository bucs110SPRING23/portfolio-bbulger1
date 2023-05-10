import pygame
import sys
import src.view as view
import src.api_proxys.coffee as coffee
import src.api_proxys.colormind_proxy as colormind_proxy
import src.models.image_processor as image_processor
import src.utility as utility

class Controller:
    def __init__(self):
        '''
        init function for controller
        args: self
        return: none
        '''
        #module objects
        self.util = utility.Utility()
        self.coffee = coffee.Coffee()
        self.colormind = colormind_proxy.ColormindAPI()
        self.colors = self.colormind.return_colors()
        self.img = image_processor.ImageProcessor()
        self.frame = 0
        self.view = view.View()
        self.accept_input = True

        #setup 
        self.view.text_display()
        self.display_image = False

    def mainloop(self):
        '''
        mainloop function
        args: self
        return: none
        '''
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if self.accept_input:
                        #self.accept_input = False
                        self.view.loading_display()
                        self.colors = self.colormind.return_colors()
                        self.coffee.image()
                        self.img.coffee_resize()
                        self.img.image_processor(self.colors)
                        self.display_image = True
            self.frame += 1
            #self.view.generate_background(self.colors, self.frame)
            #self.view.generate_color(self.colors, self.frame)
            if self.display_image: self.view.draw_coffee()
            #self.accept_input = True
            pygame.display.flip()