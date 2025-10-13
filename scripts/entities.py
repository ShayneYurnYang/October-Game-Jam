import pygame
import constants

class entities:
    def __init__(self, game, type, pos, size):
        # Initialization
        self.game = game
        self.type = type
        self.pos = list(pos)
        self.size = size
        self.vel = [0,0]

    # Update position 
    def update(self, mvmt = (0, 0)):
        # Movement per frame
        frame_mvmt = (mvmt[0] + self.vel[0], mvmt[1] + self.vel[1])

        # Change position
        self.pos[0] += frame_mvmt[0]
        self.pos[1] += frame_mvmt[1]

    def render(self, surface):
        surface.blit(pygame.transform.scale(self.game.assets['player'], self.size), self.pos)