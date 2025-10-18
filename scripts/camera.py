class Camera:
    def __init__(self, game, left_bound, right_bound):
        self.game = game
        self.left_bound = left_bound
        self.right_bound = right_bound
        self.pos = [0, 0]

    # Scroll the camera (background) according to player movement
    def scroll(self, surface, bg, player_pos = (0, 0)):
        if (player_pos[0] >= self.left_bound and player_pos[0] <= self.right_bound):
            surface.blit(bg, (-player_pos[0], 0))
            # print('in bounds: ' + str(player_pos[0]))
        elif (player_pos[0] < self.left_bound):
            surface.blit(bg, (self.left_bound, 0))
            # print('left bound: ' + str(player_pos[0]))
        elif (player_pos[0] > self.right_bound):
            surface.blit(bg, (-(self.right_bound), 0))
            # print('right bound: ' + str(player_pos[0]))