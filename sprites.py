import pygame

class wall(pygame.sprite.Sprite):
    #defines constructor for walls
    def __init__(self, color, width, height, wall_x, wall_y):
        #calls sprite constructor
        super().__init__()
        ##creates the rectangle sprite
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        ##sets the x and y value
        self.rect.x = wall_x
        self.rect.y = wall_y

##player sprite class
class player(pygame.sprite.Sprite):
    #defines constructor for player
    def __init__(self, color, width, height, player_x, player_y,player_health,player_lives, player_score,player_image):
        #calls sprite constructor
        super().__init__()
        ##creates rectangle sprite
        self.image = player_image
        self.rect = self.image.get_rect()
        #sets x and y values
        self.rect.x = player_x
        self.rect.y = player_y
        #sets speed to 0
        self.speed = 0
        self.climb_speed = 0
        #sets score, health and lives
        self.score = player_score
        self.health = player_health
        self.lives = player_lives
        #sets bullet timer
        self.bullet_timer = 0
        ##sets coins
        self.coins = 0
    ##function to add points
    def add_points(self,points):
        self.score = self.score + points
    ##function to set speed
    def player_set_speed(self,val):
        self.speed = val
    ##function to set climbing speed
    def player_climb_speed(self,val):
        self.climb_speed = val
    ##function to update sprite position
    def update(self):
        #checks to make sure sprite is in game boundaries
        if self.rect.x >= 20 :
            #adds speed to current position
            self.rect.x = self.rect.x + self.speed
        elif self.rect.x < 20:
            self.rect.x = 20
        if self.rect.x <= 650 :
            self.rect.x = self.rect.x + self.speed
        elif self.rect.x > 650:
            self.rect.x = 650
        ##adds climbing speed to y
        self.rect.y = self.rect.y + self.climb_speed
    ##function to take away health from player
    def player_hit(self):
        self.health = self.health - 1
    ##function to take away lives from player
    def player_lose_life(self,val):
        self.lives = self.lives - 1
        self.health = val

##ladder sprite class
class ladder(pygame.sprite.Sprite):
    ##defines constructor for ladder
    def __init__(self, color, width, height, ladder_x, ladder_y):
        ##calls sprite constructor
        super().__init__()
        ##creates sprite rectangle
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        ##sets x and y values
        self.rect.x = ladder_x
        self.rect.y = ladder_y

##enemy sprite class
class enemy(pygame.sprite.Sprite):
    ##defines enemy sprite constructor
    def __init__(self,color,width,height,enemy_x, enemy_y, health,enemy_type,enemy_image):
        ##calls sprite constructor
        super().__init__()
        ##creates sprite rectangle
        self.image = enemy_image
        self.rect = self.image.get_rect()
        ##sets x and y and health values
        self.rect.x = enemy_x
        self.rect.y = enemy_y
        self.health = health
        ##sets speed to 0
        self.speed = 0
        self.touching_ground = True
        ##sets enemy drop type
        self.type = enemy_type
    ##function for setting the direction
    def set_direction(self,speed,direction):
        self.speed = speed
        self.direction = direction
    ##function for taking damage
    def enemy_take_damage(self,val):
        self.health = self.health - val
        return self.health
    ##function for updating sprite position
    def update(self):
        ##checks to see if it moving up or down or left or right
        if self.direction == "x":
            ##adds speed to x value to move left or right
            self.rect.x = self.rect.x + self.speed
        else:
            ##adds speed to y value to move up or down
            self.rect.y = self.rect.y + self.speed
    def enemy_get_x(self):
        return self.rect.x
    def enemy_get_y(self):
        return self.rect.y
    def enemy_get_health(self):
        return self.health

##bullet sprite class
class bullet(pygame.sprite.Sprite):
    ##constructor for bullet sprites
    def __init__(self,color,width,height,bullet_x, bullet_y,direction):
        ##calls sprite constructor
        super().__init__()
        ##creates sprite rectangle
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        ##sets x and y and direction values
        self.rect.x = bullet_x
        self.rect.y = bullet_y
        self.direction = direction
        ##checks the direction
        if self.direction == "left":
            ##sets speed in correct direction
            self.speed = -6
        elif self.direction == "right":
            self.speed = 6
    ##updates sprite position
    def update(self):
        ##add speed to x value
        self.rect.x = self.rect.x + self.speed

##door sprite class
class door(pygame.sprite.Sprite):
    ##constructor for door sprite
    def __init__(self,color,door_x, door_y):
        ##calls sprite constructor
        super().__init__()
        ##creates sprite rectangle
        self.image = pygame.Surface([50,100])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        ##sets x and y values
        self.rect.x = door_x
        self.rect.y = door_y
        ##initialises hidden and in_group variables
        self.hidden = True
        self.in_group = False
    ##function to cause door to be revealed
    def reveal_door(self):
        self.hidden = False

##coin sprite class
class coin(pygame.sprite.Sprite):
    ##constructor for coin sprites
    def __init__(self,color,coin_x, coin_y):
        ##calls sprite constructor
        super().__init__()
        ##creates sprite rectangle
        self.image = pygame.Surface([10,10])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        ##sets x and y values
        self.rect.x = coin_x
        self.rect.y = coin_y

##powerup sprite class
class power_up(pygame.sprite.Sprite):
    ##constructor for powerup sprites
    def __init__(self,color,power_x,power_y,power_type):
        ##calls sprite constructor
        super().__init__()
        ##creates sprite rectangle
        self.image = pygame.Surface([20,20])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        ##sets x and y values
        self.rect.x = power_x
        self.rect.y = power_y
        ##sets powerup type
        self.type = str(power_type)
        

