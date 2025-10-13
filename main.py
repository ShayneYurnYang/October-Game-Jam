import pygame
import random
import math
import constants
from pygame.locals import *
#initalize objects
pygame.init()
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
clock = pygame.time.Clock()

#initalize variables
debug = True
running = True
move_right = False
move_left = False
dt = 0
player_pos = pygame.Vector2(0, 0)
keys = pygame.key.get_pressed()

#set window name
pygame.display.set_caption("October game jam")

#import and scale background image
bg = pygame.image.load("bg.png").convert()
bg = pygame.transform.scale(bg,(bg.get_width()*constants.SCREEN_HEIGHT/bg.get_height(),constants.SCREEN_HEIGHT))


class Text:
    def __init__(self):
        self.msg = []
        self.printmsg = []
        self.start = 0
        self.counter = 0
        self.row = 0
        self.lineHeight = 20
        self.keyPress = True
        
    def print(self, msg, time, name = ""):
        split = msg.split("\n")
        self.msg.append((split, time, name))
        self.printmsg=[" "]*len(self.msg[0][0])

            
    
    def update(self, keys):
        if len(self.msg) != 0:
            self.start += dt
            pygame.draw.polygon(screen, (255,255,255), [(constants.SCREEN_WIDTH/8, constants.SCREEN_HEIGHT/2),(constants.SCREEN_WIDTH/8*7, constants.SCREEN_HEIGHT/2),(constants.SCREEN_WIDTH/8*7, constants.SCREEN_HEIGHT),(constants.SCREEN_WIDTH/8, constants.SCREEN_HEIGHT)], width=0)
            pygame.draw.polygon(screen, (0,0,0), [(constants.SCREEN_WIDTH/8, constants.SCREEN_HEIGHT/2),(constants.SCREEN_WIDTH/8*7, constants.SCREEN_HEIGHT/2),(constants.SCREEN_WIDTH/8*7, constants.SCREEN_HEIGHT),(constants.SCREEN_WIDTH/8, constants.SCREEN_HEIGHT)], width=2)
            
            for index, msg in enumerate(self.printmsg, start=1):
                screen.blit(pygame.font.SysFont("arial", 20).render(msg, False, (0, 0, 0)), (constants.SCREEN_WIDTH/8+100, constants.SCREEN_HEIGHT/2+10+self.lineHeight*index))

            screen.blit(pygame.font.SysFont("arial", 20).render(self.msg[0][2], False, (0, 0, 0)), (constants.SCREEN_WIDTH/8+8, constants.SCREEN_HEIGHT/2+2))
            

            if self.start >= self.msg[0][1] and self.printmsg != self.msg[0][0]:
                    self.printmsg[self.row]=(self.msg[0][0][self.row][:self.counter])
                    if self.counter != len(self.msg[0][0][self.row]):
                        self.counter += 1
                    else:
                        self.row += 1
                        self.counter = 0
                    self.start = 0
                
            if keys[pygame.K_RETURN] and self.keyPress:
                if self.printmsg != self.msg[0][0]:
                    self.printmsg = self.msg[0][0].copy()
                else:
                    self.msg.pop(0)
                    if len(self.msg) != 0:
                        self.printmsg=[" "]*len(self.msg[0][0])
                    self.counter = 0
                    self.row = 0
                self.keyPress = False
            if not keys[pygame.K_RETURN] and self.keyPress == False:
                self.keyPress = True
gg = True

text = Text()

#main game loop
while running:
    #dt = time between frames, set screen frames per second
    dt = clock.tick(constants.FPS) / 1000
    dt = max(0.001,min(0.1,dt))

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    screen.fill("black")
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        #exit program
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        
        #key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                move_left=True
            if event.key == pygame.K_d:
                move_right=True
        
        #key released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                move_left=False
            if event.key == pygame.K_d:
                move_right=False
    
    #set left bounds
    if move_left:
        if ((player_pos.x-(constants.PLAYER_VELOCITY*dt))>-constants.SCREEN_WIDTH/2+constants.PLAYER_WIDTH/2):
            player_pos.x-=constants.PLAYER_VELOCITY*dt
    
    #set right bounds
    if move_right:
        if ((player_pos.x+constants.PLAYER_VELOCITY*dt)<(bg.get_width()-constants.SCREEN_WIDTH/2-constants.PLAYER_WIDTH/2)):
            player_pos.x+=constants.PLAYER_VELOCITY*dt
    
    #allow player to move to edge of background sides
    if (player_pos.x>=0 and player_pos.x<=bg.get_width()-constants.SCREEN_WIDTH):
        screen.blit(bg,(-player_pos.x,0))
        pygame.draw.circle(screen, "red",(screen.get_width()/2,screen.get_height()/2),constants.PLAYER_WIDTH/2)
    elif (player_pos.x<0):
        screen.blit(bg,(0,0))
        pygame.draw.circle(screen, "red",(screen.get_width()/2+player_pos.x,screen.get_height()/2),constants.PLAYER_WIDTH/2)
    elif (player_pos.x>bg.get_width()-constants.SCREEN_WIDTH):
        screen.blit(bg,(-(bg.get_width()-constants.SCREEN_WIDTH),0))
        pygame.draw.circle(screen, "red",(screen.get_width()/2+player_pos.x-(bg.get_width()-constants.SCREEN_WIDTH),screen.get_height()/2),constants.PLAYER_WIDTH/2)



    #debug
    if debug:
        # print(str(player_pos.x)+", "+str((bg.get_width()-constants.SCREEN_WIDTH/2)))
        # print(dt)
        if gg:
            text.print("hello guys made some very minor updates", .05, "person 1")
            text.print("but it can support multiple lines now", .05, "person 2")
            text.print("which it could not do before \n \nfor some reason", .05, "person 1")
            text.print("still ugly though", .05, "person 2")
            text.print("what else should i change apart from the font", .05)
            gg=False
        # print(dt)
    
    # flip() the display to put your work on screen
    text.update(keys)
    pygame.display.flip()

#clean up program
pygame.quit()