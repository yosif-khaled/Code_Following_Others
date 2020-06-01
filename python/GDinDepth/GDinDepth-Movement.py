import pygame
from math import sqrt

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()


TITLE = '4 way vs 8 way movement'
FPS = 30
WIDTH = 500
HEIGHT = 500
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

rect_x = WIDTH//2
rect_y = HEIGHT//2
rect_size = 50


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64, 64))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        
    def update(self):
        self.vx = 0
        self.vy = 0
        keystate = pygame.key.get_pressed()
        '''
        # 4-Way Movement
        if keystate[pygame.K_UP]:
            self.vy += -5
        elif keystate[pygame.K_DOWN]:
            self.vy += 5
        elif keystate[pygame.K_LEFT]:
            self.vx += -5
        elif keystate[pygame.K_RIGHT]:
            self.vx += 5
        self.rect.x += self.vx
        self.rect.y += self.vy
        '''
        # 8-Way Movement
        if keystate[pygame.K_UP]:
            self.vy += -5
        if keystate[pygame.K_DOWN]:
            self.vy += 5
        if keystate[pygame.K_LEFT]:
            self.vx += -5
        if keystate[pygame.K_RIGHT]:
            self.vx += 5
        if self.vx != 0 and self.vy != 0:
            self.vx /= sqrt(2)
            self.vy /= sqrt(2)
        self.rect.x += self.vx
        self.rect.y += self.vy
        print(self.rect)
player = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)


running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()
    
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.update()
    
pygame.quit()
quit()