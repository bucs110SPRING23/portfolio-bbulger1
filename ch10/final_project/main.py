import pygame
import src.controller as controller

# import your controller

def main():
    pygame.init()
    main_controller = controller.Controller()
    # Create an instance on your controller object
    main_controller.mainloop()
    # Call your mainloop

    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == "__main__":
    main()
