import pygame
import constants
import random
import math

pygame.init()

#screen init
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
clock = pygame.time.Clock()

#variable init
debug = True
running = True
move_right = False
move_left = False
dt = 0

#global timer, never reset
game_timer=0

#position and velocity variables for the birb/circle
vertical_pos = screen.get_height()/2
vertical_v = 0

#screen height for obstacles
obs_height = 0

#importing background and foreground
game_window = pygame.Rect(screen.get_width()/2-150, 0/2, 300, screen.get_height())
bg = pygame.image.load("flappybird assets/flappy bird bg.png").convert()
fg = pygame.image.load("flappybird assets/foreground.png").convert()
pygame.display.set_caption("Minigame screen")

#import obstacle
up_obs = pygame.image.load("flappybird assets/flappy bird pipe.png").convert_alpha()

#obstacle location [game times][obs_height]
obs_location = []
for i in range(10):
    pair = []
    pair.append((i+2)*bg.get_width())
    pair.append(random.random()*150)
    obs_location.append(pair)


#main loop
while running:
    #dt = time between frames, set screen frames per second
    dt = clock.tick(constants.FPS) / 1000
    dt = max(0.001,min(0.1,dt))
    
    #++global timer
    game_timer+=1

    #draw background and foreground
    screen.fill("black")
    screen.blit(bg,(250,0))
    screen.blit(fg,(-(game_timer%(fg.get_width()-screen.get_width())),400))
    
    #draw character
    pygame.draw.aacircle(screen,"red",(screen.get_width()/2,vertical_pos),15)
    
    #player hitbox
    p_hitbox = pygame.Rect((screen.get_width()/2)-15,(vertical_pos-15),30,30)

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        #exit program
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            vertical_v=400
        #key pressed

    #effect of gravity on velocity
    vertical_v-=dt*800

    #effect of velocity on position
    vertical_pos-=vertical_v*dt
    
    #draw obstacles
    obs_x,obs_height = obs_location[0]
    screen.blit(up_obs,(obs_x-game_timer,300+obs_height))
    screen.blit(pygame.transform.flip(up_obs,False,True),(obs_x-game_timer,-200+obs_height))
    
    #checking for collision
    if(p_hitbox.colliderect(pygame.Rect(obs_x-game_timer,300+obs_height,100,300)) or p_hitbox.colliderect(pygame.Rect(obs_x-game_timer,-200+obs_height,100,300))):
        pygame.quit()

    #next set of obstacles
    obs_x,obs_height = obs_location[1]
    screen.blit(up_obs,(obs_x-game_timer,300+obs_height))
    screen.blit(pygame.transform.flip(up_obs,False,True),(obs_x-game_timer,-200+obs_height))

    #checking for collision
    if(p_hitbox.colliderect(pygame.Rect(obs_x-game_timer,300+obs_height,100,300)) or p_hitbox.colliderect(pygame.Rect(obs_x-game_timer,-200+obs_height,100,300))):
        pygame.quit()

    #check if second pipe passes the middle
    if (obs_x-game_timer<screen.get_width()/2):
        obs_location.pop(0)

    #cuttin off extra from main screen
    pygame.draw.rect(screen,"black",pygame.Rect(0,0,250,450))
    pygame.draw.rect(screen,"black",pygame.Rect(550,0,250,450))


    #debug
    if debug:
        print(str(vertical_pos) + ", " + str(vertical_v)+" | "+str(game_timer)+" | "+str(obs_x)+" | "+str(obs_x-game_timer))
    
    # flip() the display to put your work on screen
    pygame.display.flip()

#clean up program
pygame.quit()
