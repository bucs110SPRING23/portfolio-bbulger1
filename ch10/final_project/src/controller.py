import pygame
import sys
import src.view as view
import src.api_proxys.colormind_proxy as colormind_proxy
import src.utility as utility

class Controller:
    def __init__(self):
        self.view = view.View()
        self.colormind = colormind_proxy.ColormindAPI()
        self.colors = self.colormind.return_colors()

    def mainloop(self):
        while 1:

            self.view.background(self.colors)
            utility = utility.Utility()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()