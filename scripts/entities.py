import pygame
import constants
import random

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
        self.mvmt = [False,0,'player']

    def get_pos(self):
        return self.pos  

    # Update position 
    def update(self, mvmt = [0, 0]):
        # Movement per frame
        frame_mvmt = (mvmt[0] + self.vel[0], mvmt[1] + self.vel[1])
        self.mvmt[0] = True if mvmt[0] < 0 else False if mvmt[0] > 0 else self.mvmt[0]
        if mvmt[0] != 0:
            self.mvmt[1] += abs(mvmt[0])
            if self.mvmt[1] > 75:
                self.mvmt[1] = 0
                self.mvmt[2] = 'playerStep' if self.mvmt[2] == 'player' else 'player'
                print(self.game.assets)
        else:
            self.mvmt[1] = 0
            self.mvmt[2] = 'player'
        # Change position
        self.pos[0] += frame_mvmt[0]
        self.pos[1] += frame_mvmt[1]

        if (self.pos[0] < (self.left_bound - constants.SCREEN_WIDTH/2)):
            self.pos[0] = (self.left_bound - constants.SCREEN_WIDTH/2)
        if (self.pos[0] > self.right_bound + constants.SCREEN_WIDTH/2 - self.size[0]):
            self.pos[0] = (self.right_bound + constants.SCREEN_WIDTH/2 - self.size[0])

    # Render entity sprite on surface
    # this is player specific!!!!! im gonna try to find another way to get this to work.... agh
    def render(self, surface):
        if (self.get_pos()[0] >= self.left_bound and self.get_pos()[0] <= self.right_bound):
            surface.blit(pygame.transform.scale(pygame.transform.flip(self.game.assets[self.mvmt[2]], self.mvmt[0], 0), self.size), (constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2))
        elif (self.get_pos()[0] > self.right_bound):
            surface.blit(pygame.transform.scale(pygame.transform.flip(self.game.assets[self.mvmt[2]], self.mvmt[0], 0), self.size), (self.pos[0] - self.right_bound + constants.SCREEN_WIDTH/2, self.pos[1]))
        elif (self.get_pos()[0] < self.left_bound):
            surface.blit(pygame.transform.scale(pygame.transform.flip(self.game.assets[self.mvmt[2]], self.mvmt[0], 0), self.size), (self.pos[0] + constants.SCREEN_WIDTH/2, self.pos[1]))
            
            
class NPC(Entities):
    def __init__(self, game, type, left_bound, right_bound, pos, size):
        super().__init__(game, type, left_bound, right_bound, pos, size)
        self.distance = 0
        self.moving = False
        
    def wander(self):
        chance = random.randint(0,100)
        if chance == 0:
            self.moving = True
            self.distance = random.randint(100,200)
            mvmt = random.randint(0,1)
        
        if self.moving:
            self.distance -= self.vel[mvmt]
            if mvmt:
                return (False, True)
            else:
                return (True, False)
            
        
    def interact(self):
        pass
        # wip