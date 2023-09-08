import pygame
import sys
import os
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
        #module objects + other things that get referenced later
        self.util = utility.Utility()
        self.coffee = coffee.Coffee()
        self.colormind = colormind_proxy.ColormindAPI()
        self.colors = self.colormind.return_colors()
        self.img = image_processor.ImageProcessor()
        self.view = view.View()
        self.accept_input = True

        #setup 
        self.view.text_display(self.util.MSG)
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
                    try: os.remove("ch10/final_project/assets/final_image.jpg")
                    except: pass
                    try: os.remove("ch10/final_project/assets/image_b.jpg")
                    except: pass
                    try: os.remove("ch10/final_project/assets/image_g.jpg")
                    except: pass
                    try: os.remove("ch10/final_project/assets/image_r.jpg")
                    except: pass
                    try: os.remove("ch10/final_project/assets/image.jpg")
                    except: pass
                    try: os.remove("ch10/final_project/assets/new_image.jpg")
                    except: pass
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if self.accept_input:
                        self.view.loading_display(self.util.MSG2)
                        self.colors = self.colormind.return_colors()
                        self.coffee.image()
                        new_image = self.img.coffee_resize("ch10/final_project/assets/image.jpg", "ch10/final_project/assets/")
                        final_image = self.img.image_processor(self.colors, new_image, "ch10/final_project/assets/")
                        self.display_image = True
            if self.display_image: self.view.draw_coffee(final_image)
            pygame.display.flip()