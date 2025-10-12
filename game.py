import pygame
import sys
import constants
from pygame.locals import *

class Game:
    def __init__(self):

        # Init pygame
        pygame.init()

        # Set title
        title = 'October Game Jam'
        pygame.display.set_caption(title)

        # Change game icon
        icon = pygame.image.load('test.png')
        pygame.display.set_icon(icon)

        #import and scale background image
        self.bg = pygame.image.load("bg.png").convert()
        self.bg = pygame.transform.scale(bg, (bg.get_width()*constants.SCREEN_HEIGHT/bg.get_height(), constants.SCREEN_HEIGHT))

        # Init screen and clock
        self.screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        # Init movement
        self.mvmt = [False, False, False, False]
        
        # Init variables
        self.running = True # Is game still running
        self.dt = 0  # Time between frames in seconds, unset
        self.debug = True # Variable for debug
    
    def run(self):
        while self.running:
            # Set dt
            self.dt = self.clock.tick(constants.FPS) / 1000
            self.dt = max(0.001,min(0.1, self.dt))

            # Fill screen with 