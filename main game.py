"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
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
 
pygame.init()
pygame.font.init()

#defines fonts
my_pause_font = pygame.font.SysFont('Calibri', 50, True, False)
score_font = pygame.font.SysFont('Calibri', 15, True, False)

#sets screen width and height
screen_width = 700
screen_height = 500

# Set the width and height of the screen [width, height]
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("dexter coursework")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

## creates counter for enemy spawns
pygame.event.Event(pygame.USEREVENT)
pygame.time.set_timer(pygame.USEREVENT, 3000)

##creates paused screen text
paused_text = my_pause_font.render("GAME PAUSED", True, GREEN)

##sets new game variable
first_game = True

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

    ##initialises playerr attributes
    my_player.health = max_health
    my_player.score = current_score
    my_player.lives = current_lives
    
initialise_variables()



##level maker subroutine
def level_maker(level):
    if level == 1:
        temp_wall = [sprites.wall(WHITE, screen_width, (screen_height/25), 0, (screen_height-(screen_height/25))), sprites.wall(WHITE, screen_width/35, screen_height,0,0), sprites.wall(WHITE, screen_width/35, screen_height,(screen_width - screen_width/35),0), sprites.wall(WHITE, screen_width, (screen_height/25),0,(screen_height/25)*11)]
        for i in range (0,4):
            wall_group.add(temp_wall[i])
            all_sprites_group.add(temp_wall[i])
        temp_ladder = [sprites.ladder(RED, (screen_width/70)*4, (screen_height/25)*13 + 1,((screen_width/7)*2),(screen_height/25)*11 - 1),sprites.ladder(RED, (screen_width/70)*4, (screen_height/25)*13 + 1,((screen_width/35)*23),(screen_height/25)*11 - 1)]
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
    my_player.rect.x = (screen_width/2)-((screen_width/70)*3)/2
    my_player.rect.y = screen_height-(screen_height/25)-((screen_height/20)*3)
    return wall_group, all_sprites_group

def find_direction(player_pos_x, enemy_pos_x, player_pos_y, enemy_pos_y, temp_enemy):
    if player_pos_y == enemy_pos_y:
        temp_direction = "x"
        if enemy_pos_y == (screen_height/100)*81 or enemy_pos_y == ((screen_height/500)*149):
            if player_pos_x > enemy_pos_x:
                enemy_speed = 1
            elif player_pos_x < enemy_pos_x:
                enemy_speed = -1
            else:
                enemy_speed = 0
        else:
            enemy_speed = 0
    elif player_pos_y > enemy_pos_y:
        if pygame.sprite.spritecollideany(temp_enemy, ladder_group):
            temp_direction = "y"
            enemy_speed = 1
        else:
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
    temp_enemy.set_direction(enemy_speed,temp_direction)


def shoot(direction, player_x, player_y):
    if my_player.bullet_timer <= (pygame.time.get_ticks() - 300):
        player_y = player_y + (screen_width/40)*3
        if direction == "left":
            player_x = player_x
        elif direction == "right":
            player_x = (screen_width/70)*3 + player_x
        temp_bullet = sprites.bullet(RED, 3,3, player_x, player_y,direction)
        my_bullet.append(temp_bullet)
        bullet_group.add(temp_bullet)
        all_sprites_group.add(temp_bullet)
        my_player.bullet_timer = pygame.time.get_ticks()

def enemy_spawn(enemy_counter):
    spawn_point = random.randint(1,4)
    if spawn_point == 1 or spawn_point == 3:
        spawn_x = screen_width/35
    else:
        spawn_x = (screen_width/14)*13
    if spawn_point == 1 or spawn_point == 2:
        spawn_y = screen_height-(screen_height/25)-((screen_height/20)*3)
    else:
        spawn_y = (screen_height/100)*29
    temp_spawn_enemy = sprites.enemy(BLUE,screen_width/70*3, (screen_height/20)*3,spawn_x,spawn_y,5)
    my_enemy.append(temp_spawn_enemy)
    enemy_group.add(temp_spawn_enemy)
    all_sprites_group.add(temp_spawn_enemy)
    enemy_counter += 1
    return enemy_counter

def coin_drop(enemy_x,enemy_y):
    enemy_x = enemy_x + (screen_width/140)*3
    enemy_y = enemy_y + screen_height/10
    my_coin = sprites.coin(YELLOW,enemy_x,enemy_y)
    coin_group.add(my_coin)
    all_sprites_group.add(my_coin)
    

#creates main title screen
instructions_1 = "use left and right keys to move left and right"
instructions_2 = "use up and down keys while touching a ladder to climb up or down"
instructions_3 = "use space bar to shoot"
instructions_4 = "use escape to pause"
instructions_5 = "press space to start game"
main_text_1 = score_font.render(instructions_1, True, YELLOW)
main_text_2 = score_font.render(instructions_2, True, YELLOW)
main_text_3 = score_font.render(instructions_3, True, YELLOW)
main_text_4 = score_font.render(instructions_4, True, YELLOW)
main_text_5 = score_font.render(instructions_5, True, YELLOW)

#creates game over screen
over_1 = "GAME OVER"
over_2 = "press space to play again"
over_text_1 = score_font.render(over_1, True, RED)
over_text_2 = score_font.render(over_2, True, RED)


# -------- Main Program Loop -----------
while not done:
    if start_new_game == True:
        initialise_variables()
        start_new_game = False
    if new_level == True:
        for i in ladder_group:
            ladder_group.remove(i)
            all_sprites_group.remove(i)
        for i in wall_group:
            wall_group.remove(i)
            all_sprites_group.remove(i)
        level_maker(level)
        new_level = False
        all_sprites_group.add(my_player)
        if level == 1 or level == 2:
            my_door = sprites.door(ORANGE, 325, 120)
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.USEREVENT:
            enemy_spawn(enemy_counter)
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE : # changes paused status
                if paused == True :
                    paused = False
                elif paused == False:
                    paused = True
            if paused == False:
                if event.key == pygame.K_LEFT and touching_ground == True:
                    my_player.player_set_speed(int(-2))
                    player_direction = "left"
                elif event.key == pygame.K_RIGHT and touching_ground == True:
                    my_player.player_set_speed(int(2))
                    player_direction = "right"
                elif event.key == pygame.K_SPACE:
                    shoot(player_direction, my_player.rect.x, my_player.rect.y)
                    game_started = True
                    first_game = False
                elif event.key ==pygame.K_MINUS:
                    door_group.add(my_door)
                    all_sprites_group.add(my_door)
                elif can_climb == True:
                    if event.key == pygame.K_UP:
                        my_player.player_climb_speed(-4)
                        touching_ground = False
                    elif event.key == pygame.K_DOWN :
                        my_player.player_climb_speed(4)
                        touching_ground = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                if my_player.speed == -2:
                    my_player.player_set_speed(int(0))
            elif event.key == pygame.K_RIGHT:
                if my_player.speed == 2:
                    my_player.player_set_speed(int(0))
            elif event.key == pygame.K_UP:
                if my_player.climb_speed == -4:
                    my_player.player_climb_speed(0)
            elif event.key == pygame.K_DOWN:
                if my_player.climb_speed == 4:
                    my_player.player_climb_speed(0)
    # --- Game logic should go here
    if game_started == True:
        if paused == False: #-- only plays game logic and draw loop if paused 
        
            

            for enemy_find_direction in enemy_group:
                find_direction(my_player.rect.x,enemy_find_direction.rect.x,my_player.rect.y, enemy_find_direction.rect.y, enemy_find_direction)
                
            

            ##climbing code
            ladder_check = pygame.sprite.spritecollideany(my_player, ladder_group, False)
            if ladder_check:
                can_climb = True
            else:
                can_climb = False
            if ladder_check:
                if level == 3:
                    ladder_1_check = pygame.sprite.spritecollideany(my_player, ladders_1, False)
                    if ladder_1_check:
                        if my_player.rect.y ==334:
                            my_player.rect.y = 330
                            touching_ground = True
                        elif my_player.rect.y == 166:
                            my_player.rect.y = 170
                            touching_ground = True 
                    else:
                        if my_player.rect.y == 70:
                            my_player.rect.y = 74
                            touching_ground = True
                        elif my_player.rect.y == 174:
                            my_player.rect.y = 170
                            touching_ground = True 
                else:
                    if my_player.rect.y == 145:
                        my_player.rect.y = 149                        
                        touching_ground = True
                    elif my_player.rect.y == 409:
                        my_player.rect.y = 405
                        touching_ground = True
            
            if can_climb == False:
                my_player.player_climb_speed(0)

            ##code for player colliding with a coin
            for i in coin_group:
                if pygame.sprite.collide_rect(my_player,i):
                    my_player.coins = my_player.coins + 1
                    coin_group.remove(i)
                    all_sprites_group.remove(i)
            
            ##code for level door
            if new_level == False:
                if my_door.in_group == False and my_door.hidden == False:
                    all_sprites_group.add(my_door)
                    my_door.in_group = True
            
            ##code for getting rid of bullets that have hit enemies
            for test_bullet in bullet_group:
                bullet_hit_check_1 = pygame.sprite.spritecollideany(test_bullet, enemy_group)
                if bullet_hit_check_1:
                    bullet_hit_check_2 = True
                else:
                    bullet_hit_check_2 = False
                if bullet_hit_check_2 == True:
                    ##checking for enemy damaged
                    for test_enemy in enemy_group:
                        enemy_hit = pygame.sprite.collide_rect(test_bullet,test_enemy)
                        if enemy_hit == True:
                            test_enemy.enemy_take_damage()
                            if test_enemy.health == 0:
                                coin_drop(test_enemy.rect.x, test_enemy.rect.y)
                                enemy_group.remove(test_enemy)
                                all_sprites_group.remove(test_enemy)
                                my_player.add_points(10)
                                current_score = current_score + 10
                            bullet_group.remove(test_bullet)
                            all_sprites_group.remove(test_bullet)
                    bullet_hit_check_2 = False

            ##code for checking if enemies hit player
            for test_enemy in enemy_group:
                player_hit = pygame.sprite.spritecollide(my_player,enemy_group,False)
                for i in player_hit:
                    enemy_group.remove(player_hit)
                    all_sprites_group.remove(player_hit)
                    my_player.player_hit()
                    if my_player.health == 0:
                        my_player.player_lose_life(max_health)
                        my_player.rect.x =(screen_width/2)-((screen_width/70)*3)/2
                        my_player.rect.y = screen_height-(screen_height/25)-((screen_height/10)*3)
                        if my_player.lives < 0:
                            game_over = True
                            game_started = False
            ##code for advancing level if door is touched
            if pygame.sprite.spritecollide(my_player, door_group, False):
                new_level = True
                all_sprites_group.remove(my_door)
                door_group.remove(my_door)
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
            all_sprites_group.update()
            all_sprites_group.draw(screen)
            screen.blit(score_text, [30,0])
            screen.blit(health_text, [150,0])
            screen.blit(lives_text, [300,0])
            screen.blit(coins_text, [400,0])
        else :
            #clears screen
            screen.fill(BLACK)
            #draws pause screen
            screen.blit(paused_text, [200,0])
            screen.blit(score_text, [30,0])
    elif game_started == False:
        if first_game == True:
            screen.blit(main_text_1, [0,50])
            screen.blit(main_text_2, [0,100])
            screen.blit(main_text_3, [0,150])
            screen.blit(main_text_4, [0,200])
            screen.blit(main_text_5, [0,250])
            first_game == False
        elif game_over == True:
            screen.fill(BLACK)
            end_score = current_score
            over_score = "your score was: {}".format(current_score)
            over_score_text = score_font.render(over_score, True, RED)
            screen.blit(over_text_1, [200,200])
            screen.blit(over_score_text, [200,300])
            screen.blit(over_text_2, [200,400])
            start_new_game = True
            
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
