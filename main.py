import pygame
import random
import math
import constants
from pygame.locals import *
from game import Game
# #initalize objects
# pygame.init()
# screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
# clock = pygame.time.Clock()

# #initalize variables
# debug = True
running = True
# move_right = False
# move_left = False
# dt = 0
# player_pos = pygame.Vector2(0, 0)
game = Game()

game.run()

# #set window name
# pygame.display.set_caption("October game jam")

# #import and scale background image
# bg = pygame.image.load("bg.png").convert()
# bg = pygame.transform.scale(bg,(bg.get_width()*constants.SCREEN_HEIGHT/bg.get_height(),constants.SCREEN_HEIGHT))

#main game loop
# while running:
    # #dt = time between frames, set screen frames per second
    # dt = clock.tick(constants.FPS) / 1000
    # dt = max(0.001,min(0.1,dt))

    # # poll for events
    # # pygame.QUIT event means the user clicked X to close your window
    # screen.fill("black")
    # for event in pygame.event.get():
    #     #exit program
    #     if event.type == pygame.QUIT:
    #         running = False
        
        # #key pressed
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_a:
        #         move_left=True
        #     if event.key == pygame.K_d:
        #         move_right=True
        
        # #key released
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_a:
        #         move_left=False
        #     if event.key == pygame.K_d:
        #         move_right=False
    
    # #set left bounds
    # if move_left:
    #     if ((player_pos.x-(constants.PLAYER_VELOCITY*dt))>-constants.SCREEN_WIDTH/2+constants.PLAYER_WIDTH/2):
    #         player_pos.x-=constants.PLAYER_VELOCITY*dt
    
    # #set right bounds
    # if move_right:
    #     if ((player_pos.x+constants.PLAYER_VELOCITY*dt)<(bg.get_width()-constants.SCREEN_WIDTH/2-constants.PLAYER_WIDTH/2)):
    #         player_pos.x+=constants.PLAYER_VELOCITY*dt
    
    # #allow player to move to edge of background sides
    # if (player_pos.x>=0 and player_pos.x<=bg.get_width()-constants.SCREEN_WIDTH):
    #     screen.blit(bg,(-player_pos.x,0))
    #     pygame.draw.circle(screen, "red",(screen.get_width()/2,screen.get_height()/2),constants.PLAYER_WIDTH/2)
    # elif (player_pos.x<0):
    #     screen.blit(bg,(0,0))
    #     pygame.draw.circle(screen, "red",(screen.get_width()/2+player_pos.x,screen.get_height()/2),constants.PLAYER_WIDTH/2)
    # elif (player_pos.x>bg.get_width()-constants.SCREEN_WIDTH):
    #     screen.blit(bg,(-(bg.get_width()-constants.SCREEN_WIDTH),0))
    #     pygame.draw.circle(screen, "red",(screen.get_width()/2+player_pos.x-(bg.get_width()-constants.SCREEN_WIDTH),screen.get_height()/2),constants.PLAYER_WIDTH/2)

    # #debug
    # if debug:
    #     print(str(player_pos.x)+", "+str((bg.get_width()-constants.SCREEN_WIDTH/2)))
    
    # # flip() the display to put your work on screen
    # pygame.display.flip()

# #clean up program
# pygame.quit()


