import pygame
import constants

pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
clock = pygame.time.Clock()

debug = True
running = True
move_right = False
move_left = False
dt = 0
scroll=0

vertical_pos = screen.get_height()/2
vertical_v = 0

game_window = pygame.Rect(screen.get_width()/2-150, 0/2, 300, screen.get_height())
bg = pygame.image.load("flappybird assets/flappy bird bg.png").convert()
fg = pygame.image.load("flappybird assets/foreground.png").convert()
pygame.display.set_caption("Minigame screen")



while running:
    #dt = time between frames, set screen frames per second
    dt = clock.tick(constants.FPS) / 1000
    dt = max(0.001,min(0.1,dt))

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    screen.fill("black")
    screen.blit(bg,(250,0))
    scroll-=dt*300
    screen.blit(fg,(scroll,400))
    if (scroll<-100):
        scroll+=200
    
    pygame.draw.rect(screen,"black",pygame.Rect(0,0,250,450))
    pygame.draw.rect(screen,"black",pygame.Rect(550,0,250,450))
    
    for event in pygame.event.get():
        #exit program
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            vertical_v=300
        #key pressed

    vertical_v-=dt*300
    vertical_pos-=vertical_v*dt
    pygame.draw.aacircle(screen,"red",(screen.get_width()/2,vertical_pos),20)

    if debug:
        print(str(vertical_pos) + ", " + str(vertical_v))
    
    # flip() the display to put your work on screen
    pygame.display.flip()

#clean up program
pygame.quit()
