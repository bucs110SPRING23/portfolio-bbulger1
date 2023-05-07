import pygame
import sys
import src.view as view
import src.api_proxys.colormind_proxy as colormind_proxy
import src.utility as util

class Controller:
    def __init__(self):
        self.colormind = colormind_proxy.ColormindAPI()
        self.colors = self.colormind.return_colors()
        self.frame = 0
        self.view = view.View(self.colors)

    def mainloop(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.frame += 1
            self.view.background()
            pygame.display.flip()
            pygame.time.delay(10)