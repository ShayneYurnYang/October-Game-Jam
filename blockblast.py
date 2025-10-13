import pygame
import constants

pygame.init()
arr = [[0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0]]

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
clock = pygame.time.Clock()

debug = True
running = True
move_right = False
move_left = False
dt = 0

smallest_side = min(screen.get_height(),screen.get_width())
window_size = smallest_side-constants.MINIGAME_GAP*2
game_window = pygame.Rect(screen.get_width()/2-window_size/2, screen.get_height()/2-window_size/2, window_size, window_size)

pygame.display.set_caption("Minigame screen")

def draw_grid(arr):
    x_size = len(arr)
    y_size = len(arr[0])
    x = 0
    y = 0
    tile_size = window_size/x_size
    for i in arr:
        y=0
        for r in i:
            tile = pygame.Rect(screen.get_width()/2-window_size/2+tile_size*x+5, screen.get_height()/2-window_size/2+tile_size*y+5, tile_size-10,tile_size-10)
            if arr[x][y]==1:
                pygame.draw.rect(screen,"green",tile)
            elif arr[x][y]==0:
                pygame.draw.rect(screen,"red",tile)
            #print(str(x)+","+str(y)+" | value of tile ="+str(arr[x][y]))
            y+=1
        x+=1

def reverse_tile(arr,x,y):
    if (arr[x][y]==1):
        arr[x][y]=0
    else:
        arr[x][y]=1



tile_x,tile_y=(0,0)
while running:
    #dt = time between frames, set screen frames per second
    dt = clock.tick(constants.FPS) / 1000
    dt = max(0.001,min(0.1,dt))

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    screen.fill("black")
    pygame.draw.rect(screen,"white",game_window)
    draw_grid(arr)
    for event in pygame.event.get():
        #exit program
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (mouse_x>screen.get_width()/2-window_size/2 and mouse_x<screen.get_width()/2+window_size/2 and mouse_y>screen.get_height()/2-window_size/2 and mouse_y<screen.get_height()/2+window_size/2):
                tile_x=int((mouse_x-(390/10)) // (390/5)-2)
                tile_y=int((mouse_y-(390/10)) / (390/5))
                if (0<=tile_x and tile_x<=4 and 0<=tile_y and tile_y<=4):
                    if (1<=tile_x and tile_x<=3 and 1<=tile_y and tile_y<=3):
                        reverse_tile(arr,tile_x+1,tile_y)
                        reverse_tile(arr,tile_x,tile_y+1)
                        reverse_tile(arr,tile_x-1,tile_y)
                        reverse_tile(arr,tile_x,tile_y-1)
                        reverse_tile(arr,tile_x,tile_y)
                    else:
                        reverse_tile(arr,tile_x,tile_y)
                        if (tile_x+1>4):
                            reverse_tile(arr,0,tile_y)
                        else:
                            reverse_tile(arr,tile_x+1,tile_y)
                        if (tile_y+1>4):
                            reverse_tile(arr,tile_x,0)
                        else:
                            reverse_tile(arr,tile_x,tile_y+1)
                        reverse_tile(arr,tile_x-1,tile_y)
                        reverse_tile(arr,tile_x,tile_y-1)





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
    if debug:
        print(str(screen.get_width()/2-smallest_side/2+constants.MINIGAME_GAP)+", "+str(screen.get_height()/2-smallest_side/2+constants.MINIGAME_GAP)+" | "+str(tile_x)+", "+str(tile_y))
    
    # flip() the display to put your work on screen
    pygame.display.flip()

#clean up program
pygame.quit()
