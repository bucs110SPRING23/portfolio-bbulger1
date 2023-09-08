import pygame
from PIL import Image
import src.utility as utility

class ImageProcessor():
    def __init__(self):
        '''
        init function for image processor
        args: self
        return: none
        '''
        self.util = utility.Utility()
        #self.pil_color.init()

    def coffee_resize(self, filepath, output_location):
        '''
        resizes coffee image to fit windows size
        args: self, filepath (filepath) image source, output_location (output_location) filepath to save image output to
        return: (filepath) filepath for output image
        '''
        image = pygame.image.load(filepath)
        new_image = pygame.transform.scale(image, [self.util.WINDOW_SIZE, self.util.WINDOW_SIZE])
        pygame.image.save(new_image, output_location + "new_image.jpg")
        return output_location + "new_image.jpg"

    def image_processor(self, colors, filepath, output_location):
        '''
        generates new image with color pallete from base image
        args: self, colors (list) color pallete, filepath (filepath) image source, output_location (output_location) filepath to save images output to
        return: (filepath) filepath for final image output
        '''
        new_image = Image.open(filepath, "r")
        image_r = Image.new("L", [self.util.WINDOW_SIZE, self.util.WINDOW_SIZE], 0)
        image_g = Image.new("L", [self.util.WINDOW_SIZE, self.util.WINDOW_SIZE], 0)
        image_b = Image.new("L", [self.util.WINDOW_SIZE, self.util.WINDOW_SIZE], 0)
        for x in range(self.util.WINDOW_SIZE):
            for y in range(self.util.WINDOW_SIZE):
                pixel = new_image.getpixel((x,y))
                color_compare = []
                for color in colors:
                    val_r = pixel[0] - color[0]
                    val_g = pixel[1] - color[1]
                    val_b = pixel[2] - color[2]
                    dif = abs(val_r + val_g + val_b)
                    color_compare.append(dif)
                m = min(color_compare)
                i = color_compare.index(m)
                new_pixel = colors[i]
                image_r.putpixel([x, y], new_pixel[0])
                image_g.putpixel([x, y], new_pixel[1])
                image_b.putpixel([x, y], new_pixel[2])
        image_r.save(output_location + "image_r.jpg")
        image_b.save(output_location + "image_g.jpg")
        image_g.save(output_location + "image_b.jpg")
        final_image = Image.merge("RGB", [image_r, image_b, image_g])
        final_image.save(output_location + "final_image.jpg")
        return output_location + "final_image.jpg"