import pygame

class wall(pygame.sprite.Sprite):
    #defines constructor for walls
    def __init__(self, color, width, height, wall_x, wall_y):
        #calls sprite constructor
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
        
class player(pygame.sprite.Sprite):
    def __init__(self, color, width, height, player_x, player_y,):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = 0
    def player_set_speed(self,val):
        self.speed = val
    def update(self):
        self.rect.x = self.rect.x + self.speed
