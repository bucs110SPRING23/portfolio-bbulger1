import pygame
import sys
import src.view as view
import src.api_proxys.colormind_proxy as colormind_proxy
import src.utility as util

class Controller:
    def __init__(self):
        self.util = util.Utility()
        self.colormind = colormind_proxy.ColormindAPI()
        self.colors = self.colormind.return_colors()
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
                    #self.view.clear()
            self.frame += 1
            #self.view.generate_background(self.colors, self.frame)
            self.view.generate_color(self.colors, self.frame)
            pygame.display.flip()
            pygame.time.delay(self.util.FRAME_DELAY)