# Imports
import pygame
import os
import sys
import random

# Initializing Pygame
pygame.init()

# Constants
window_width = 800
window_height = 600
TITLE = 'Pong'
FPS = 120
clock = pygame.time.Clock()

# Screen
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption(TITLE)
# Global Variables
color_white = (255, 255, 255)


# Classes
class Player1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10 , 80))
        self.image.fill(color_white)
        self.rect = self.image.get_rect()
        self.rect.left = 25
        self.rect.centery = window_height/2
        self.dy = 0 # Velocity
        
    def update(self):
        self.dy = 0
        
        # Movement
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.dy = -3
        elif keystate[pygame.K_s]:
            self.dy = 3
            
        if keystate[pygame.K_r]:
            ball.__init__()
            
        self.rect.y += self.dy
        
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > window_height:
            self.rect.bottom = window_height
        
class Player2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10 , 80))
        self.image.fill(color_white)
        self.rect = self.image.get_rect()
        self.rect.right = window_width - 25
        self.rect.centery = window_height/2
        
    def update(self):
        self.dy = 0
        
        # Movement
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.dy = -3
        elif keystate[pygame.K_DOWN]:
            self.dy = 3
            
        self.rect.y += self.dy
        
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > window_height:
            self.rect.bottom = window_height
    
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (window_width/2, window_height/2)
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-2, -1, 1, 2])
        
    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        # Wall Collision
        if self.rect.top < 0:
            self.dy *= -1
        elif self.rect.bottom > window_height:
            self.dy *= -1
        
        # Paddle Collision
        collision = pygame.sprite.spritecollideany(ball, all_sprites)
        if collision:
            if collision == player1:
                self.rect.x -= self.dx
                self.dx *= -1
                self.dx += random.choice([0, 1])
            if collision == player2:
                self.rect.x -= self.dx
                self.dx *= -1
                self.dx += random.choice([0, 1])
            if self.dy == 0:
                self.dy += random.choice([-1, 1])
            if self.dy <= 0:
                self.dy += -random.choice([-1, 0, 1])
            if self.dy >= 0:
                self.dy += random.choice([-1, 0, 1])
    
class Score():
    def __init__(self):
        self.score1 = 0
        self.score2 = 0
        self.score_font = pygame.font.SysFont(None, 100)
        self.win_font = pygame.font.SysFont(None, 70)
        self.player1_win = self.win_font.render('Player 1 WINS', True, (255, 255, 255), (0,0,0))
        self.player2_win = self.win_font.render('Player 2 WINS', True, (255, 255, 255), (0,0,0))
        
    def update(self):
        if ball.rect.right < 0:
            self.score2 += 1
            ball.__init__()
        if ball.rect.left > window_width:
            self.score1 += 1
            ball.__init__()
        self.player1_score = self.score_font.render(str(self.score1), True, (255, 255, 255), (0, 0, 0))
        self.player2_score = self.score_font.render(str(self.score2), True, (255, 255, 255), (0, 0, 0))
        
    def draw(self):
        game_window.blit(self.player1_score, (window_width/4, window_height/4))
        game_window.blit(self.player2_score, (window_width*(3/4), window_height/4))
        if self.score1 == 5:
            ball.__init__()
            ball.dy = 0
            ball.dx = 0
            game_window.blit(self.player1_win, (window_width/4, window_height/2))
            
        if self.score2 == 5:
            ball.__init__()
            ball.dy = 0
            ball.dx = 0
            game_window.blit(self.player2_win, (window_width/4, window_height/2))
# Sprite Group
all_sprites = pygame.sprite.Group()
ball_sprite = pygame.sprite.GroupSingle()

# Object Initialization
player1 = Player1()
all_sprites.add(player1)
player2 = Player2()
all_sprites.add(player2)
ball = Ball()
ball_sprite.add(ball)

score = Score()
score.__init__()


while True:
    # Set Frame Rate
    clock.tick(FPS)
    
    # Process Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # Update
    all_sprites.update()
    ball_sprite.update()
    score.update()
    # Draw
        # Fill
    game_window.fill((0, 0, 0))
        #Field
    pygame.draw.line(game_window, (255, 255, 255), (window_width/2, 0), (window_width/2, window_height))
    pygame.draw.circle(game_window, (255, 255, 255), (window_width//2, window_height//2), 80, 1)
        # Sprites
    score.draw()
    all_sprites.draw(game_window)
    ball_sprite.draw(game_window)
    
    # Flip Rendering
    pygame.display.flip()

pygame.quit()