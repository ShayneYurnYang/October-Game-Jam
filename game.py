import pygame
import sys
import constants
from scripts.entities import Entities
from scripts.entities import NPC
from scripts.camera import Camera
from scripts.text import Text
from scripts.utils import load_img


class Game:
    def __init__(self):

        # Init pygame
        pygame.init()

        # Set title
        title = 'October Game Jam'
        pygame.display.set_caption(title)

        # Init screen and clock
        self.screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        # Change game icon
        icon = pygame.image.load('data/images/test.png').convert()
        pygame.display.set_icon(icon)

        #import and scale background image
        self.bg = pygame.image.load("data/images/bg.png").convert()
        self.bg = pygame.transform.scale(self.bg, (self.bg.get_width()*constants.SCREEN_HEIGHT/self.bg.get_height(), constants.SCREEN_HEIGHT))
        
        # Init voicefont
        self.vf = pygame.mixer.Sound("sfx/tempvoicefont.wav")

        # Init camera
        self.cam = Camera(self, 0, self.bg.get_width()-constants.SCREEN_WIDTH)

        # Init movement
        self.mvmt = [False, False]

        # Init player
        self.player = Entities(self, 'player', 0, self.bg.get_width()-constants.SCREEN_WIDTH, (0, constants.SCREEN_HEIGHT/2), (50, 75))
        self.assets = {
            'player': load_img('entities/player/player.png'),
            'playerStep': load_img('entities/player/playerStep.png')
        }        

        # Init text
        self.text = Text(self.vf)
        
        # Init variables
        self.dt = 0  # Time between frames in seconds, unset
        self.debug = True # Variable for debug
    
    def run(self):
        while True:
            # Check for inputs
            

            # Set dt
            self.dt = self.clock.tick(constants.FPS) / 1000
            self.dt = max(0.001,min(0.1, self.dt))
            keys = pygame.key.get_pressed()

            # Flip to display new screen
            pygame.display.flip()

            # Reset screen after every frame
            self.screen.fill((30, 182, 248))

            # Update player position
            self.player.update([((self.mvmt[1] - self.mvmt[0])*constants.PLAYER_VELOCITY*self.dt), 0])

            # Put background
            self.cam.scroll(self.screen, self.bg, self.player.get_pos())

            # Render player model
            self.player.render(self.screen)

            # Update text
            self.text.update(keys, self.dt)

            # Render text
            self.text.render(self.screen)

            # toggles movement 
            if keys[pygame.K_a]:
                self.mvmt[0] = True
            else:
                self.mvmt[0] = False

            if keys[pygame.K_d]:
                self.mvmt[1] = True
            else:
                self.mvmt[1] = False

            # text test
            if keys[pygame.K_l]:
                self.text.print("Hello bro")

            for event in pygame.event.get():
                
                # Check if exit (X) button pressed
                if (event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()
                # # Check keys pressed
                # if (event.type == pygame.KEYDOWN):
                #     # Check movement
                #     if (event.key == pygame.K_a):
                #         self.mvmt[0] = True
                #     if (event.key == pygame.K_d):
                #         self.mvmt[1] = True

                # # Check keys released
                # if event.type == pygame.KEYUP:
                #     # Check movement
                #     if (event.key == pygame.K_a):
                #         self.mvmt[0] = False
                #     if (event.key == pygame.K_d):
                #         self.mvmt[1] = False