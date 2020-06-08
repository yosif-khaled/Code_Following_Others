# Imports
import pygame
import sys
import random

# Constants
WIDTH = 800
HEIGHT = 600

BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

FPS = 30


# Player
player_size = 50
player_pos = [WIDTH/2, HEIGHT - 2*player_size*(3/4)]
score = 0

# Enemy
enemy_size = 50
enemy_pos = [random.randint(enemy_size, WIDTH-enemy_size), 0]
print(enemy_pos)
enemy_list = [enemy_pos]
SPEED = 10

# Pygame Initalization
pygame.init()

# Screen Initialization
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Game Title

# Functions
def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]
    
    e_x = enemy_pos[0]
    e_y = enemy_pos[1]
    
    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
            return True
    return False

def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.1:
        x_pos = random.randint(enemy_size, WIDTH-enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])
        
def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
            pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
        
def update_enemy_position(enemy_list):
    # Update Enemy Position
    global score
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
            enemy_pos[1] += SPEED
        else:
            enemy_list.pop(idx)
            score += 1
            print(score)
            
def collision_check(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(enemy_pos, player_pos):
            return True
    return False

def set_level(score):
    global SPEED
    if score < 20:
        SPEED = 5
    elif score < 50 and score >= 20:
        SPEED = 20
    elif score < 60 and score >= 50:
        SPEED = 50
    else:
        SPEED = 100
    print(SPEED)
    # dividing the score a number and make the speed equal that number will make the speed proportion
    # SPEED = score/5 + 1

clock = pygame.time.Clock()
game_over = False
while not game_over:
    clock.tick(FPS)
    for event in pygame.event.get():
        #print(event) # extremly useful prints events on screen
        if event.type == pygame.QUIT:
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]
            if event.key == pygame.K_LEFT:
                x -= player_size
            elif event.key == pygame.K_RIGHT:
                x += player_size
            player_pos = [x,y]
    
    screen.fill(BLACK)
    
    drop_enemies(enemy_list)
    font = pygame.font.SysFont('monospace', 35)
    text = 'Score: ' + str(score)
    label = font.render(text, 1, (255, 255, 255))
    screen.blit(label, (WIDTH-200, HEIGHT-40))
    update_enemy_position(enemy_list)
    set_level(score)
    draw_enemies(enemy_list)
    
    if collision_check(enemy_list, player_pos):
        game_over = True
        
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.display.update()