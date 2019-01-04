##importing libraries, including sprite library
import pygame
import sprites
import math
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
ORANGE = (255, 150, 0)
PURPLE = (255,0,255)
PINK = (255, 200, 200)

#initialising pygame and the font functionality
pygame.init()
pygame.font.init()

#defines fonts for pause screen and score screen
my_pause_font = pygame.font.SysFont('Calibri', 50, True, False)
score_font = pygame.font.SysFont('Calibri', 15, True, False)

#sets screen width and height
screen_width = 700
screen_height = 500

# Set the width and height of the screen [width, height]
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

#setting the window name for the game
pygame.display.set_caption("dexter coursework")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

## creates counter event for enemy spawns
pygame.event.Event(pygame.USEREVENT)
pygame.time.set_timer(pygame.USEREVENT, 3000)

##creates paused screen text
paused_text = my_pause_font.render("GAME PAUSED", True, GREEN)

##sets new game variable
first_game = True

## initialises player variable
my_player = sprites.player(GREEN, (screen_width/70)*3, (screen_height/20)*3,(screen_width/2)-((screen_width/70)*3)/2,screen_height-(screen_height/5)*4, 0,0, 0)


##initialisation function
def initialise_variables():
    #player direction initiation variable
    global player_direction
    player_direction = "left"

    #level initiation variable
    global level
    level = 1

    ##variables for checking to make sure player rest on ground after climbing
    global touching_ground
    touching_ground = True

    ##initailising variable for telling if new level is needed
    global new_level
    new_level = True

    ##initialising variable for can climb
    global can_climb
    can_climb = False

    # Loop until the user clicks the close button.
    global done
    done = False

    #set paused variable to false
    global paused
    paused = False

    ## game over initialised
    global game_over
    game_over = False
    
    #variables for going up onto the laddres in level 3
    global ladders_1
    ladders_1 = pygame.sprite.Group()

    #initiate all sprites group
    global all_sprites_group
    all_sprites_group = pygame.sprite.Group()

    ##creating list of all wall sprites
    global wall_group
    wall_group = pygame.sprite.Group()

    ##creating list of all ladder sprites
    global ladder_group
    ladder_group = pygame.sprite.Group()

    ##creating group of bullets
    global bullet_group
    bullet_group = pygame.sprite.Group()

    ##creates group for enemies
    global enemy_group
    enemy_group = pygame.sprite.Group()

    ##creating door group for the one door
    global door_group
    door_group = pygame.sprite.GroupSingle()

    ##creates list for bullets
    global my_bullet
    global bullet_list_counter
    my_bullet = []
    bullet_list_counter = 0

    ##creates spawn for first enemy
    global my_enemy
    my_enemy =  []

    ##creates varaible for enemy hit checker
    global enemy_hit
    enemy_hit = False

    ##sets health max for player
    global max_health
    max_health = 10

    ##sets a counter for how many enemies has spawned
    global enemy_counter
    enemy_counter = 0

    ##sets variable so lives stay the same when going up a level but reset when restarting the game
    global current_lives
    current_lives = 3

    ##game started variable
    global game_started
    game_started = False
    
    ##current score variable
    global current_score
    current_score = 0

    ##start new game
    global start_new_game
    start_new_game = True

    ##coin group
    global coin_group
    coin_group = pygame.sprite.Group()

    ##power up group
    global power_up_group
    power_up_group = pygame.sprite.Group()

    ##speed powered up varaible
    global speed_powered_up
    speed_powered_up = False

    ##speed timer on
    global speed_timer_on
    speed_timer_on = False

    ##player speed
    global player_speed
    player_speed = 2

    ##bullet color
    global bullet_color
    bullet_color = RED

    ##bullet damage
    global bullet_damage
    bullet_damage = 1

    ##bullet powered up
    global bullet_powered_up
    bullet_powered_up = False

    ## power timer on
    global power_timer_on
    power_timer_on = False

    ##speed_up on
    global speed_up
    speed_up = False
    
    ##initialises playerr attributes
    my_player.health = max_health
    my_player.score = current_score
    my_player.lives = current_lives

##calls the initialising function
initialise_variables()

##level maker subroutine
def level_maker(level):
    ##if statement for checking what level to create
    if level == 1:
        ##creating a list of wall sprites
        temp_wall = [sprites.wall(WHITE, screen_width, (screen_height/25), 0, (screen_height-(screen_height/25))), sprites.wall(WHITE, screen_width/35, screen_height,0,0), sprites.wall(WHITE, screen_width/35, screen_height,(screen_width - screen_width/35),0), sprites.wall(WHITE, screen_width, (screen_height/25),0,(screen_height/25)*11)]
        ##adding each of the wall sprites a wall group and the all sprites group
        for i in range (0,4):
            wall_group.add(temp_wall[i])
            all_sprites_group.add(temp_wall[i])
        ##creating a list of ladder sprites
        temp_ladder = [sprites.ladder(RED, (screen_width/70)*4, (screen_height/25)*13 + 1,((screen_width/7)*2),(screen_height/25)*11 - 1),sprites.ladder(RED, (screen_width/70)*4, (screen_height/25)*13 + 1,((screen_width/35)*23),(screen_height/25)*11 - 1)]
        ##adding each ladder to a ladder group and the all sprites group
        for i in range(0,2):
            ladder_group.add(temp_ladder[i])
            all_sprites_group.add(temp_ladder[i])
    elif level == 2:
        temp_wall = [sprites.wall(WHITE, screen_width, (screen_height/25), 0, (screen_height-(screen_height/25))), sprites.wall(WHITE, screen_width/35, screen_height,0,0),sprites.wall(WHITE, screen_width/35, screen_height,(screen_width - screen_width/35),0), sprites.wall(WHITE, screen_width, (screen_height/25),0,(screen_height/25)*11)]
        for i in range (0,4):
            wall_group.add(temp_wall[i])
            all_sprites_group.add(temp_wall[i])
        temp_ladder = [sprites.ladder(RED, (screen_width/70)*4, (screen_height/25)*13 + 1,((screen_width/140)*67),(screen_height/25)*11 - 1)]
        for i in range(0,1):
            ladder_group.add(temp_ladder[i])
            all_sprites_group.add(temp_ladder[i])
    elif level == 3:
        temp_wall = [sprites.wall(WHITE, screen_width, (screen_height/25), 0, (screen_height-(screen_height/25))), sprites.wall(WHITE, screen_width/35, screen_height,0,0),sprites.wall(WHITE, screen_width/35, screen_height,(screen_width - screen_width/35),0), sprites.wall(WHITE, screen_width, (screen_height/25),0,(screen_height/25)*16),sprites.wall(WHITE,screen_width,screen_height/25,0,(screen_height/25)*8)]
        for i in range (0,5):
            wall_group.add(temp_wall[i])
            all_sprites_group.add(temp_wall[i])
        temp_ladder = [sprites.ladder(RED, (screen_width/70)*4, (screen_height/25)*8 + 1,((screen_width/7)*2),(screen_height/25)*16-1),sprites.ladder(RED, (screen_width/70)*4, (screen_height/25)*8+1,((screen_width/35)*23),(screen_height/25)*16-1),sprites.ladder(RED, (screen_width/70)*4, (screen_height/25)*8+1,(screen_width/70)*33,(screen_height/25)*8-1)]
        for i in range(0,3):
            ladder_group.add(temp_ladder[i])
            all_sprites_group.add(temp_ladder[i])
        ladders_1.add(temp_ladder[0])
        ladders_1.add(temp_ladder[1])
    ##putting the player into the starting position
    my_player.rect.x = (screen_width/2)-((screen_width/70)*3)/2
    my_player.rect.y = screen_height-(screen_height/25)-((screen_height/20)*3)
    return wall_group, all_sprites_group

##making a function for the ai to find out where the player is
def find_direction(player_pos_x, enemy_pos_x, player_pos_y, enemy_pos_y, temp_enemy):
    ##if statement checking whether the player is on the same vertical level as the enemy
    if player_pos_y == enemy_pos_y:
        ##setting the variable of direction to x, as the enemy is on the same y coordinate
        temp_direction = "x"
        ##checking if the enemy height is correct, so it does not go left or right while climbing
        if enemy_pos_y == (screen_height/100)*81 or enemy_pos_y == ((screen_height/500)*149):
            ##checking to see if player is to the left or right of the enemy, and setting the enemy's direction so that it will follow the player
            if player_pos_x > enemy_pos_x:
                enemy_speed = 1
            elif player_pos_x < enemy_pos_x:
                enemy_speed = -1
            else:
                enemy_speed = 0
        else:
            enemy_speed = 0
    ##checking to see if the enemy is higher or lower then the player
    elif player_pos_y > enemy_pos_y:
        ##checking to see if the enemy can climb up a ladder to get to the correct height
        if pygame.sprite.spritecollideany(temp_enemy, ladder_group):
            ##if it can, setting the enemy to climb upwards
            temp_direction = "y"
            enemy_speed = 1
        else:
            ##if it's not touching a ladder, it will move more on the x axis till it finds a ladder to touch
            temp_direction = "x"
            if player_pos_x > enemy_pos_x:
                enemy_speed = 1
            elif player_pos_x < enemy_pos_x:
                enemy_speed = -1
            else:
                enemy_speed = 0
    elif player_pos_y < enemy_pos_y:
        if pygame.sprite.spritecollideany(temp_enemy, ladder_group):
            temp_direction = "y"
            enemy_speed = -1
        else:
            temp_direction = "x"
            if player_pos_x > enemy_pos_x:
                enemy_speed = 1
            elif player_pos_x < enemy_pos_x:
                enemy_speed = -1
            else:
                enemy_speed = 0
    else:
        enemy_speed = 0
    ##setting the enemy sprite with the correct speed and direction now found from this function
    temp_enemy.set_direction(enemy_speed,temp_direction)

##function that can be called upon to allow the player to shoot
def shoot(direction, player_x, player_y,bullet_color):
    ##checking to see if enough time has passed to let the player shoot again
    if my_player.bullet_timer <= (pygame.time.get_ticks() - 300):
        ##finding position where the bullet should spawn, which would be around the middle of the player
        player_y = player_y + (screen_width/40)*3
        ##using the player's direction to decide which side of the player the bullet should spawn on
        if direction == "left":
            player_x = player_x
        elif direction == "right":
            player_x = (screen_width/70)*3 + player_x
        ##creating a bullet sprite using these attributes
        temp_bullet = sprites.bullet(bullet_color, 3,3, player_x, player_y,direction)
        ##adding the bullet sprite to a list of bullets
        my_bullet.append(temp_bullet)
        ##adding the bullet sprite to a group of bullets and all sprites
        bullet_group.add(temp_bullet)
        all_sprites_group.add(temp_bullet)
        ##reseting the timer for shooting
        my_player.bullet_timer = pygame.time.get_ticks()

##function to spawn enemies
def enemy_spawn(enemy_counter):
    ##choosing a spawn point for the enemy
    spawn_point = random.randint(1,4)
    ##creating an x attribute depending on which point is chosen
    if spawn_point == 1 or spawn_point == 3:
        spawn_x = screen_width/35
    else:
        spawn_x = (screen_width/14)*13
    ##creating a y attribute depending on which point is chosen
    if spawn_point == 1 or spawn_point == 2:
        spawn_y = screen_height-(screen_height/25)-((screen_height/20)*3)
    else:
        spawn_y = (screen_height/100)*29
    ##deciding what the enemhy will drop on death
    type_chooser = random.randint(1,7)
    ##if it is a powerup
    if type_chooser >= 6:
        enemy_type = "powerup"
        enemy_color = YELLOW
    ##if it is a coin
    else:
        enemy_type = "coin"
        enemy_color = BLUE
    ##creating an enemy sprite using these attributes
    temp_spawn_enemy = sprites.enemy(enemy_color,screen_width/70*3, (screen_height/20)*3,spawn_x,spawn_y,5,enemy_type)
    ##adding this sprite to a list of enemies, a group of enemy sprites, and all sprites group
    my_enemy.append(temp_spawn_enemy)
    enemy_group.add(temp_spawn_enemy)
    all_sprites_group.add(temp_spawn_enemy)
    ##returning how many enemies have been spawned
    enemy_counter += 1
    return enemy_counter

##function to drop a coin
def coin_drop(enemy_x,enemy_y):
    ##choosing an x and y value based on where the enemy last was
    enemy_x = enemy_x + (screen_width/140)*3
    enemy_y = enemy_y + screen_height/10
    ##creating a coin sprite using these values
    my_coin = sprites.coin(YELLOW,enemy_x,enemy_y)
    ##adding it to a group of coins and all sprites
    coin_group.add(my_coin)
    all_sprites_group.add(my_coin)

##function for dropping powerups
def powerup_drop(enemy_x,enemy_y):
    ##getting an x and y value for where to spawn the powerup
    enemy_x = enemy_x + screen_width/35
    enemy_y = enemy_y + (screen_height/55)*2
    ##choosing which type of powerup to drop
    powerup_checker = random.randint(1,2)
    ##if it is a 'speed' powerup
    if powerup_checker == 1:
        powerup_type = "speed"
        powerup_color = PURPLE
    ##if it is a damage powerup
    elif powerup_checker == 2:
        powerup_type = "power"
        powerup_color = PINK
    ##creating powerup sprite
    my_powerup = sprites.power_up(powerup_color,enemy_x,enemy_y,powerup_type)
    ##adding it to a group of powerups and all sprites group
    power_up_group.add(my_powerup)
    all_sprites_group.add(my_powerup)

##writing starting screen text
instructions_1 = "use left and right keys to move left and right"
instructions_2 = "use up and down keys while touching a ladder to climb up or down"
instructions_3 = "use space bar to shoot"
instructions_4 = "use escape to pause"
instructions_5 = "press space to start game"
##making it into displayable text
main_text_1 = score_font.render(instructions_1, True, YELLOW)
main_text_2 = score_font.render(instructions_2, True, YELLOW)
main_text_3 = score_font.render(instructions_3, True, YELLOW)
main_text_4 = score_font.render(instructions_4, True, YELLOW)
main_text_5 = score_font.render(instructions_5, True, YELLOW)

##writing text for game over screen
over_1 = "GAME OVER"
over_2 = "press space to play again"
##making it into displayable text
over_text_1 = score_font.render(over_1, True, RED)
over_text_2 = score_font.render(over_2, True, RED)


# -------- Main Program Loop -----------
##checking to make sure the game should be kept open
while not done:
    ##if a new game needs to be started
    if start_new_game == True:
        ##calling the initialisation function
        initialise_variables()
        ##setting it so that a new game does not need to be started
        start_new_game = False
    ##checking to see if a new level needs to be created
    if new_level == True:
        ##removing all current ladder sprites
        for i in ladder_group:
            ladder_group.remove(i)
            all_sprites_group.remove(i)
        ##removing all current wall sprites
        for i in wall_group:
            wall_group.remove(i)
            all_sprites_group.remove(i)
        ##removing all enemy sprites
        for i in enemy_group:
            enemy_group.remove(i)
            all_sprites_group.remove(i)
        ##calls the level making function
        level_maker(level)
        ##setting it so that it won't create another level till it is needed
        new_level = False
        ##adding the player into all sprites group 
        all_sprites_group.add(my_player)
        ##creating a door sprite
        if level == 1 or level == 2:
            my_door = sprites.door(ORANGE, 325, 120)
    # --- Main event loop
    for event in pygame.event.get():
        ##checking to see if the game has been quit
        if event.type == pygame.QUIT:
            ##setting the quitting variable to true
            done = True
        ##checking to see if it is time for a new enemy to spawn
        elif event.type == pygame.USEREVENT:
            ##calling the enemy spawn function
            enemy_spawn(enemy_counter)
        ##checking for keyboard inputs
        elif event.type == pygame.KEYDOWN :
            ##checking to see if escape has been pressed
            if event.key == pygame.K_ESCAPE :
                ##toggling the pause checking variable
                if paused == True :
                    paused = False
                elif paused == False:
                    paused = True
            ##making sure the player doesn't move around while the game is paused
            if paused == False:
                ##checkign to see if player is inputting a direction and touching the ground
                if event.key == pygame.K_LEFT and touching_ground == True:
                    ##setting the player speed to go left
                    ##seeing if the speed is powered up
                    if speed_up == False:
                        my_player.player_set_speed(int(-player_speed))
                        player_direction = "left"
                    else:
                        my_player.player_set_speed(int(-player_speed)-1)
                        player_direction = "left"
                elif event.key == pygame.K_RIGHT and touching_ground == True:
                    if speed_up == False:
                        my_player.player_set_speed(int(player_speed))
                        player_direction = "right"
                    else:
                        my_player.player_set_speed(int(player_speed)+1)
                        player_direction = "right"
                ##checking to see if the player is shooting, or that they want to start the game
                elif event.key == pygame.K_SPACE:
                    ##calling the shooting function
                    shoot(player_direction, my_player.rect.x, my_player.rect.y,bullet_color)
                    ##setting the game starting varaibles to what they need to be
                    game_started = True
                    first_game = False
                ##testing for level advancement
                elif event.key ==pygame.K_MINUS:
                    door_group.add(my_door)
                    all_sprites_group.add(my_door)
                ##testing for powerups
                elif event.key == pygame.K_0:
                    my_powerup = sprites.power_up(PURPLE,50, 200, "speed")
                    power_up_group.add(my_powerup)
                    all_sprites_group.add(my_powerup)
                ##checking to see if player is allowed to go up and down because it is touching a ladder
                elif can_climb == True:
                    ##moving the player up or down, and setting it so that it cannot go left or right while climbing
                    if event.key == pygame.K_UP:
                        if speed_up == False:
                            my_player.player_climb_speed(int(-player_speed*2))
                            touching_ground = False
                        else:
                            my_player.player_climb_speed((int(-player_speed)-1)*2)
                            touching_ground = False
                    elif event.key == pygame.K_DOWN :
                        if speed_up == False:
                            my_player.player_climb_speed(int(player_speed*2))
                            touching_ground = False
                        else:
                            my_player.player_climb_speed((int(player_speed)+1)*2)
                            touching_ground = False
        ##checking if the player has released the keys
        elif event.type == pygame.KEYUP:
            ##making it so that the player doesn't keep moving a direction after letting go of the key
            if event.key == pygame.K_LEFT:
                if my_player.speed == -2 or my_player.speed  == -3 or my_player.speed == -player_speed:
                    my_player.player_set_speed(int(0))
            elif event.key == pygame.K_RIGHT:
                if my_player.speed == 2 or my_player.speed == 3:
                    my_player.player_set_speed(int(0))
            elif event.key == pygame.K_UP:
                if my_player.climb_speed == -4 or my_player.climb_speed == -6:
                    my_player.player_climb_speed(0)
            elif event.key == pygame.K_DOWN:
                if my_player.climb_speed == 4 or my_player.climb_speed == 6:
                    my_player.player_climb_speed(0)

    # --- Game logic should go here
    ##only runs the game logic while the game should be starting
    if game_started == True:
        if paused == False: #-- only plays game logic and draw loop if paused
            
            ##calling the function to find the direction to move in for each enemy in the enemy group
            for enemy_find_direction in enemy_group:
                find_direction(my_player.rect.x,enemy_find_direction.rect.x,my_player.rect.y, enemy_find_direction.rect.y, enemy_find_direction)
            
            ##climbing code
            ##checking to see if the player is touching a ladder
            ladder_check = pygame.sprite.spritecollideany(my_player, ladder_group, False)
            ##changing the can climb variable depending on whether or not the player is touching a ladder
            if ladder_check:
                 can_climb = True
            else:
                can_climb = False
            ##checking to set the limits for climbing
            if ladder_check:
                ##if the level is 3
                if level == 3:
                    ##getting an extra ladder check for the higher ladder
                    ladder_1_check = pygame.sprite.spritecollideany(my_player, ladders_1, False)
                    if ladder_1_check:
                        ##checking the y axises for when the player is one movement above or below a ladder
                        if my_player.rect.y ==334 or my_player.rect.y ==336:
                            ##putting the player back at a height that means it will be able to climb back down
                            my_player.rect.y = 330
                            ##setting the touching ground variable to true so player can move left and right
                            touching_ground = True
                        elif my_player.rect.y == 166 or my_player.rect.y == 164:
                            my_player.rect.y = 170
                            touching_ground = True 
                    else:
                        if my_player.rect.y == 70 or my_player.rect.y == 68:
                            my_player.rect.y = 74
                            touching_ground = True
                        elif my_player.rect.y == 174 or my_player.rect.y == 176:
                            my_player.rect.y = 170
                            touching_ground = True 
                else:
                    if my_player.rect.y == 145:
                        my_player.rect.y = 149                        
                        touching_ground = True
                    elif my_player.rect.y == 409 or my_player.rect.y >= 411:
                        my_player.rect.y = 405
                        touching_ground = True
            print(my_player.rect.y)
            ##checking for if player is lifted off ground because of speed power up
            if my_player.rect.y == 141 or my_player.rect.y == 143:
                my_player.rect.y = 149
                touching_ground = True
                       
            ##making sure the player can only climb when touching a ladder
            if can_climb == False:
                ##setting climb speed to 0
                my_player.player_climb_speed(0)

            ##code for player colliding with a coin
            for i in coin_group:
                ##checking if the coin is touching the player sprite
                if pygame.sprite.collide_rect(my_player,i):
                    ##add one coin to the current coin count
                    my_player.coins = my_player.coins + 1
                    ##remove the sprites from the coin group and all sprites group
                    coin_group.remove(i)
                    all_sprites_group.remove(i)
            
            ##code for level door
            if new_level == False:
                ##if the door is not meant to be hidden anymore, it will be added to the all sprites group if it isn't already
                ##this will mean it will be drawn
                if my_door.in_group == False and my_door.hidden == False:
                    all_sprites_group.add(my_door)
                    my_door.in_group = True
            
            ##code for getting rid of bullets that have hit enemies
            for test_bullet in bullet_group:
                ##checks to see if any bulelts are colliding with any enemies
                bullet_hit_check_1 = pygame.sprite.spritecollideany(test_bullet, enemy_group)
                if bullet_hit_check_1:
                    bullet_hit_check_2 = True
                else:
                    bullet_hit_check_2 = False
                if bullet_hit_check_2 == True:
                    ##checking for enemy damaged
                    for test_enemy in enemy_group:
                        #checks each enemy to see if it has been hit by the bullet
                        enemy_hit = pygame.sprite.collide_rect(test_bullet,test_enemy)
                        if enemy_hit == True:
                            ##calls the damage taking function in the enemy sprite class
                            test_enemy.enemy_take_damage(bullet_damage)
                            ##checking to see if that enemy's health is 0 or below and therefore dead
                            if test_enemy.health <= 0:
                                ##checks for what type of drop the enemy will leave
                                if test_enemy.type == "coin":
                                    ##calls the coin drop function
                                    coin_drop(test_enemy.rect.x, test_enemy.rect.y)
                                    ##adds points
                                    my_player.add_points(10)
                                elif test_enemy.type == "powerup":
                                    ##calls the powerup drop function
                                    powerup_drop(test_enemy.rect.x,test_enemy.rect.y)
                                    ##adds points
                                    my_player.add_points(30)
                                ##removes the enemy sprite from the game
                                enemy_group.remove(test_enemy)
                                all_sprites_group.remove(test_enemy)
                                ##add to score
                                current_score = current_score + 10
                            ##removes the bullet sprite
                            bullet_group.remove(test_bullet)
                            all_sprites_group.remove(test_bullet)
                    bullet_hit_check_2 = False

            ##code for checking if enemies hit player
            for test_enemy in enemy_group:
                ##checks for collissions between the player sprite and any enemy sprite
                player_hit = pygame.sprite.spritecollide(my_player,enemy_group,False)
                ##for each enemy that is hitting the player
                for i in player_hit:
                    ##remove the enemy from the enemy group and sprites group
                    enemy_group.remove(player_hit)
                    all_sprites_group.remove(player_hit)
                    ##call the player hit function
                    my_player.player_hit()
                    ##checking to see if player is dead
                    if my_player.health == 0:
                        ##call the lose life function
                        my_player.player_lose_life(max_health)
                        ##reset player location
                        my_player.rect.x =(screen_width/2)-((screen_width/70)*3)/2
                        my_player.rect.y = screen_height-(screen_height/25)-((screen_height/10)*3)
                        ##checking to see if there is a game over
                        if my_player.lives < 0:
                            ##trigger game over
                            game_over = True
                            game_started = False

            ##for player touching power up
            for test_powerup in power_up_group:
                ##check to see if the player touches the powerup
                if pygame.sprite.spritecollide(my_player,power_up_group,False):
                    temp_type = test_powerup.type
                    ##checking what the powerup type is
                    if temp_type == "speed":
                        ##increasing the player speed
                        ##player_speed = 3.5
                        speed_powered_up = True
                        speed_up = True
                    elif temp_type == "power":
                        ##changing the damage of the bullets
                        bullet_color = YELLOW
                        bullet_damage = 2
                        bullet_powered_up = True
                    ##removing the powerup from the powerup group and the sprites group
                    power_up_group.remove(test_powerup)
                    all_sprites_group.remove(test_powerup)

            ##code for speed powering down
            ##check to see if the speed power up is active
            if speed_powered_up == True:
                ##check the time
                speed_timer_start = pygame.time.get_ticks()
                ##set an end timer
                speed_timer_end = speed_timer_start + 10000
                ##set poweruped up to false and timer on
                speed_timer_on = True
                speed_powered_up = False
            ##checking to see if the timer is on
            elif speed_timer_on == True:
                ##checking current time
                speed_timer = pygame.time.get_ticks()
                ##checking to see if it has reached the end
                if speed_timer >= speed_timer_end:
                    ##reseting speed
                    speed_up = False
                    speed_timer_on = False

            ##code for bullet powering down
            ##checking for powerup timer
            if bullet_powered_up == True:
                ##checking time
                power_timer_start = pygame.time.get_ticks()
                ##setting endtimer
                power_timer_end = power_timer_start + 7000
                ##setting poweredup and timer on
                power_timer_on = True
                bullet_powered_up = False
            ##checkign to see if the timer is on 
            elif power_timer_on == True:
                ##getting current time
                power_timer = pygame.time.get_ticks()
                ##checking to see if the time has reached the end
                if power_timer >= power_timer_end:
                    ##resetting damage
                    bullet_damage = 1
                    power_timer_on = False
                    bullet_color = RED
                        
            ##code for advancing level if door is touched
            ##checking for player collisions with level door
            if pygame.sprite.spritecollide(my_player, door_group, False):
                ##setting level start to new
                new_level = True
                ##removing door sprite
                all_sprites_group.remove(my_door)
                door_group.remove(my_door)
                ##advancing level by one
                level = level + 1
                
            ##creates score text
            score_text_string = "Score: {}".format(my_player.score)
            score_text = score_font.render(score_text_string, True, YELLOW)
            ##creates health text
            health_text_string = "health: {}".format(my_player.health)
            health_text = score_font.render(health_text_string, True, YELLOW)

            ##creates lives text
            lives_text_string = "lives: {}".format(my_player.lives)
            lives_text = score_font.render(lives_text_string,True,YELLOW)

            ##coins text
            coins_text_string = "coins: {}".format(my_player.coins)
            coins_text = score_font.render(coins_text_string, True, YELLOW)
            
            screen.fill(BLACK)
                    # --- Drawing code should go here
            ##calls the update function for all sprites
            all_sprites_group.update()
            ##draws all sprites in the sprites group
            all_sprites_group.draw(screen)
            ##draws score
            screen.blit(score_text, [30,0])
            ##draws health
            screen.blit(health_text, [150,0])
            ##draws lives
            screen.blit(lives_text, [300,0])
            ##draws coins
            screen.blit(coins_text, [400,0])
        else :
            #clears screen
            screen.fill(BLACK)
            #draws pause screen
            screen.blit(paused_text, [200,0])
            #draws score
            screen.blit(score_text, [30,0])
    ##checking to see if game has started yet
    elif game_started == False:
        ##checking to see whether or not to bring up the starting screen with instructions
        if first_game == True:
            ##drawing all the instruction text
            screen.blit(main_text_1, [0,50])
            screen.blit(main_text_2, [0,100])
            screen.blit(main_text_3, [0,150])
            screen.blit(main_text_4, [0,200])
            screen.blit(main_text_5, [0,250])
            first_game == False
        ##checking to see if it is game over
        elif game_over == True:
            ##drawing the game over screen
            screen.fill(BLACK)
            end_score = current_score
            ##drawing final score
            over_score = "your score was: {}".format(current_score)
            over_score_text = score_font.render(over_score, True, RED)
            ##drawing all the text
            screen.blit(over_text_1, [200,200])
            screen.blit(over_score_text, [200,300])
            screen.blit(over_text_2, [200,400])
            ##setting it to check for if the game is restarted
            start_new_game = True
            
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
