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
    def __init__(self, color, width, height, player_x, player_y,player_health,player_lives, player_score):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = 0
        self.climb_speed = 0
        self.score = player_score
        self.health = player_health
        self.lives = player_lives
    def add_points(self,points):
        self.score = self.score + points
    def player_set_speed(self,val):
        self.speed = val
    def player_climb_speed(self,val):
        self.climb_speed = val
    def update(self):
        if self.rect.x >= 20 :
            self.rect.x = self.rect.x + self.speed
        elif self.rect.x < 20:
            self.rect.x = 20
        if self.rect.x <= 650 :
            self.rect.x = self.rect.x + self.speed
        elif self.rect.x > 650:
            self.rect.x = 650
        self.rect.y = self.rect.y + self.climb_speed
    def player_hit(self):
        self.health = self.health - 1
    def player_lose_life(self,val):
        self.lives = self.lives - 1
        self.health = val
        
class ladder(pygame.sprite.Sprite):
    def __init__(self, color, width, height, ladder_x, ladder_y):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = ladder_x
        self.rect.y = ladder_y

class enemy(pygame.sprite.Sprite):
    def __init__(self,color,width,height,enemy_x, enemy_y, health):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = enemy_x
        self.rect.y = enemy_y
        self.health = health
        self.speed = 0
    def set_direction(self,speed):
        self.speed = speed
    def enemy_take_damage(self):
        self.health = self.health - 1
        return self.health
    def update(self):
        self.rect.x = self.rect.x + self.speed
    def enemy_get_x(self):
        return self.rect.x
    def enemy_get_y(self):
        return self.rect.y
    def enemy_get_health(self):
        return self.health
        
class bullet(pygame.sprite.Sprite):
    def __init__(self,color,width,height,bullet_x, bullet_y,direction):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = bullet_x
        self.rect.y = bullet_y
        self.direction = direction
        if self.direction == "left":
            self.speed = -6
        elif self.direction == "right":
            self.speed = 6
    def update(self):
        self.rect.x = self.rect.x + self.speed
        
        
        
