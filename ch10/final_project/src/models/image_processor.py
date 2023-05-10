import pygame
import src.utility as utility

class ImageProcessor():
    def __init__(self):
        self.util = utility.Utility()
        

    def coffee_resize(self):
        image = pygame.image.load("ch10/final_project/assets/image.jpg")
        new_image = pygame.transform.scale(image, [self.util.WINDOW_SIZE, self.util.WINDOW_SIZE])
        return new_image

    def image_processor(self, new_image):
        x=1