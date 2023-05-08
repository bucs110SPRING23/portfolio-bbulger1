import pygame
import sys
import src.view as view
import src.api_proxys.coffee as coffee
import src.api_proxys.colormind_proxy as colormind_proxy
import src.models.image_processor as image_processor
import src.utility as utility

class Controller:
    def __init__(self):
        self.util = utility.Utility()
        self.coffee = coffee.Coffee()
        self.colormind = colormind_proxy.ColormindAPI()
        self.colors = self.colormind.return_colors()
        self.img = image_processor.ImageProcessor()
        self.frame = 0
        self.view = view.View()

    def mainloop(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.colors = self.colormind.return_colors()
                    self.image = self.coffee.image()
                    self.view.clear()
            self.frame += 1
            #self.view.generate_background(self.colors, self.frame)
            self.view.generate_color(self.colors, self.frame)
            pygame.display.flip()
            pygame.time.delay(self.util.FRAME_DELAY)