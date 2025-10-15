import pygame
import constants

class Entities:
    def __init__(self, game, type, left_bound, right_bound, pos, size):
        # Initialization
        self.game = game
        self.type = type
        self.left_bound = left_bound
        self.right_bound = right_bound
        self.pos = list(pos)
        self.size = size
        self.vel = [0,0]

    def get_pos(self):
        return self.pos

    # Update position 
    def update(self, mvmt = (0, 0)):
        # Movement per frame
        frame_mvmt = (mvmt[0] + self.vel[0], mvmt[1] + self.vel[1])

        # Change position
        self.pos[0] += frame_mvmt[0]
        self.pos[1] += frame_mvmt[1]

        if (self.pos[0] < (self.left_bound - constants.SCREEN_WIDTH/2)):
            self.pos[0] = (self.left_bound - constants.SCREEN_WIDTH/2)
        if (self.pos[0] > self.right_bound + constants.SCREEN_WIDTH/2 - self.size[0]):
            self.pos[0] = (self.right_bound + constants.SCREEN_WIDTH/2 - self.size[0])

    # Render entity sprite on surface
    def render(self, surface):
        if (self.get_pos()[0] >= self.left_bound and self.get_pos()[0] <= self.right_bound):
            surface.blit(pygame.transform.scale(self.game.assets['player'], self.size), (constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2))
        elif (self.get_pos()[0] > self.right_bound):
            surface.blit(pygame.transform.scale(self.game.assets['player'], self.size), (self.pos[0] - self.right_bound + constants.SCREEN_WIDTH/2, self.pos[1]))
        elif (self.get_pos()[0] < self.left_bound):
            surface.blit(pygame.transform.scale(self.game.assets['player'], self.size), (self.pos[0] + constants.SCREEN_WIDTH/2, self.pos[1]))