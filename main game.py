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


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
pygame.font.init()

#defines fonts
my_pause_font = pygame.font.SysFont('Calibri', 50, True, False)

#sets screen width and height
screen_width = 700
screen_height = 500

#level initiation variable
level = 2

# Set the width and height of the screen [width, height]
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("dexter coursework")

# Loop until the user clicks the close button.
done = False

#initiate all sprites group
all_sprites_group = pygame.sprite.Group()

#set paused variable to false
paused = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

##creating list of all wall sprites
wall_group = pygame.sprite.Group

##creating list of all ladder sprites
ladder_group = pygame.sprite.Group

##level maker subroutine
def level_maker(level):
    if level == 1:
        temp_wall = [sprites.wall(WHITE, screen_width, (screen_height/25), 0, (screen_height-(screen_height/25))), sprites.wall(WHITE, screen_width/35, screen_height,0,0), sprites.wall(WHITE, screen_width/35, screen_height,(screen_width - screen_width/35),0), sprites.wall(WHITE, (screen_width/7)*3, (screen_height/25),(screen_width/7)*2,(screen_height/25)*11)]
        for i in range (0,4):
            wall_group.add(temp_wall[i])
            all_sprites_group.add(temp_wall[i])
        temp_ladder = [sprites.ladder(RED, (screen_width/70)*4, (screen_height/25)*13,((screen_width/7)*2),(screen_height/25)*11),sprites.ladder(RED, (screen_width/70)*4, (screen_height/25)*13,((screen_width/35)*23),(screen_height/25)*11)]
        for i in range(0,2):
            ladder_group.add(temp_ladder[i])
            all_sprites_group.add(temp_ladder[i])
    elif level == 2:
        temp_wall = [sprites.wall(WHITE, screen_width, (screen_height/25), 0, (screen_height-(screen_height/25))), sprites.wall(WHITE, screen_width/35, screen_height,0,0),sprites.wall(WHITE, screen_width/35, screen_height,(screen_width - screen_width/35),0), sprites.wall(WHITE, screen_width, (screen_height/25),0,(screen_height/25)*11)]
        for i in range (0,4):
            wall_group.add(temp_wall[i])
            all_sprites_group.add(temp_wall[i])
        temp_ladder = [sprites.ladder(RED, (screen_width/70)*4, (screen_height/25)*13,((screen_width/7)*2),(screen_height/25)*11),sprites.ladder(RED, (screen_width/70)*4, (screen_height/25)*13,((screen_width/35)*23),(screen_height/25)*11)]
        for i in range(0,2):
            ladder_group.add(temp_ladder[i])
            all_sprites_group.add(temp_ladder[i])
    elif level == 3:
        temp_wall = [sprites.wall(WHITE, screen_width, (screen_height/25), 0, (screen_height-(screen_height/25))), sprites.wall(WHITE, screen_width/35, screen_height,0,0),sprites.wall(WHITE, screen_width/35, screen_height,(screen_width - screen_width/35),0), sprites.wall(WHITE, screen_width, (screen_height/25),0,(screen_height/25)*16),sprites.wall(WHITE,(screen_width/7)*2,screen_height/25,0,(screen_height/25)*8), sprites.wall(WHITE,(screen_width/7)*2,screen_height/25, screen_width - ((screen_width/7)*2),(screen_height/25)*8)]
        for i in range (0,6):
            wall_group.add(temp_wall[i])
            all_sprites_group.add(temp_wall[i])
    return wall_group, all_sprites_group

 ## adds player to sprites group
my_player = sprites.player(GREEN, (screen_width/70)*3, (screen_height/10)*3,(screen_width/2)-((screen_width/70)*3)/2,screen_height-(screen_height/25)-((screen_height/10)*3))
all_sprites_group.add(my_player)
# -------- Main Program Loop -----------
while not done:
    level_maker(level)
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE : # changes paused status
                if paused == True :
                    paused = False
                elif paused == False:
                    paused = True
            elif event.key == pygame.K_LEFT and paused == False:
                my_player.player_set_speed(int(-2))
            elif event.key == pygame.K_RIGHT and paused == False:
                my_player.player_set_speed(int(2))
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                my_player.player_set_speed(int(0))
            elif event.key == pygame.K_RIGHT:
                my_player.player_set_speed(int(0))
    # --- Game logic should go here
    if paused == False: #-- only plays game logic and draw loop if paused 
		# --- Screen-clearing code goes here

		# Here, we clear the screen to black. Don't put other drawing commands
		# above this, or they will be erased with this command.
 
		# If you want a background image, replace this clear with blit'ing the
		# background image.
        screen.fill(BLACK)
		# --- Drawing code should go here
        all_sprites_group.update()
        all_sprites_group.draw(screen)
    else :
        #clears screen
        screen.fill(BLACK)
        #draws pause screen
        paused_text = my_pause_font.render("GAME PAUSED", True, GREEN)
        screen.blit(paused_text, [0,0])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
