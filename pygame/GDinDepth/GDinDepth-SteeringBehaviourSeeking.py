import pygame, sys, math
from random import randint, uniform

pygame.init()
pygame.mixer.init()

# Variables
WIDTH = 800
HEIGHT = 800
FPS = 60

clock = pygame.time.Clock()
keyState = pygame.key.get_pressed()
vector = pygame.math.Vector2

WHITE = (255, 255, 255)
BLACK = (0,0,0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
DARKGREY = (40, 40, 40)

MOB_SIZE = 32
MAX_SPEED = 5
SEEK_FORCE = 0.1
APPROACH_RADIUS = 150

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Steering Behaviour')

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((MOB_SIZE, MOB_SIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.pos = vector(randint(0, WIDTH),
                          randint(0, HEIGHT))
        self.velocity = vector(MAX_SPEED, 0).rotate(uniform(0, 360))
        self.acceleration = vector(0, 0)
        self.rect.center = self.pos
        
    def follow_mouse(self):
        mouse_position = pygame.mouse.get_pos()
        self.acceleration = (mouse_position - self.pos).normalize() * 0.5
        
    def seek_with_approach(self, target):
        self.desired = (target - self.pos)
        dist = self.desired.length()
        self.desired.normalize_ip() # normalize in place
        if dist < APPROACH_RADIUS:
            self.desired *= dist / APPROACH_RADIUS * MAX_SPEED
        else:
            self.desired *= MAX_SPEED
        steer = (self.desired - self.velocity)
        if steer.length() > SEEK_FORCE:
            steer.scale_to_length(SEEK_FORCE)
        return steer
    
    def seek(self, target):
        self.desired = (target - self.pos).normalize() * MAX_SPEED
        steer = (self.desired - self.velocity)
        if steer.length() > SEEK_FORCE:
            steer.scale_to_length(SEEK_FORCE)
        return steer
    
    def update(self):
        self.acceleration = self.seek_with_approach(pygame.mouse.get_pos())
        self.velocity += self.acceleration
        
        if self.velocity.length() > MAX_SPEED:
            self.velocity.scale_to_length(MAX_SPEED)
            
        self.pos += self.velocity
        
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        if self.pos.y > HEIGHT:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = HEIGHT
        
        self.rect.center = self.pos
        
        self.draw_vector()
    
    def draw_vector(self):
        scale = 25
        keyState = pygame.key.get_pressed()
        if keyState[pygame.K_v]:
            pygame.draw.line(screen, GREEN, self.pos, (self.pos + self.velocity * scale), 5)
            pygame.draw.line(screen, RED, self.pos, (self.pos + self.desired * scale), 5)
            pygame.draw.circle(screen, WHITE, pygame.mouse.get_pos(), APPROACH_RADIUS, 1)

mob = Mob()

all_sprites = pygame.sprite.Group()
all_sprites.add(mob)

gameRunning = True
while gameRunning:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False
    
    screen.fill(DARKGREY)
    all_sprites.draw(screen)
    all_sprites.update()
    # Always Last update/flip
    pygame.display.flip()

pygame.quit()
quit()