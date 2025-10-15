import pygame
import constants

class Text:
    def __init__(self):
        self.msg = []
        self.printmsg = []
        self.start = 0
        self.counter = 0
        self.row = 0
        self.lineHeight = 20
        self.keyPress = True

        
    def print(self, msg, time=0.1, name = ""):
        split = msg.split("\n")
        self.msg.append((split, time, name))
        self.printmsg=[" "]*len(self.msg[0][0])
        self.start = 0
        self.counter = 0
        self.row = 0
    
    def update(self, keys, dt):
        if len(self.msg) != 0:
            self.start += dt
            
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

    def render(self, surface):
        if len(self.msg) != 0:
            pygame.draw.polygon(surface, (255,255,255), [(constants.SCREEN_WIDTH/8, constants.SCREEN_HEIGHT/2),(constants.SCREEN_WIDTH/8*7, constants.SCREEN_HEIGHT/2),(constants.SCREEN_WIDTH/8*7, constants.SCREEN_HEIGHT),(constants.SCREEN_WIDTH/8, constants.SCREEN_HEIGHT)], width=0)
            pygame.draw.polygon(surface, (0,0,0), [(constants.SCREEN_WIDTH/8, constants.SCREEN_HEIGHT/2),(constants.SCREEN_WIDTH/8*7, constants.SCREEN_HEIGHT/2),(constants.SCREEN_WIDTH/8*7, constants.SCREEN_HEIGHT),(constants.SCREEN_WIDTH/8, constants.SCREEN_HEIGHT)], width=2)
            
            for index, msg in enumerate(self.printmsg, start=1):
                surface.blit(pygame.font.SysFont("arial", 20).render(msg, False, (0, 0, 0)), (constants.SCREEN_WIDTH/8+100, constants.SCREEN_HEIGHT/2+10+self.lineHeight*index))

            surface.blit(pygame.font.SysFont("arial", 20).render(self.msg[0][2], False, (0, 0, 0)), (constants.SCREEN_WIDTH/8+8, constants.SCREEN_HEIGHT/2+2))
