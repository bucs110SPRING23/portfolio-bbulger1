from PIL import Image

class ImageProcessor():
    def __init__(self):
        x = 1

    def image_processor(self, image):
        pic = Image.open(image, "r")
        pic.save("ch10/final_project/assets", "JPEG")