import pygame

pygame.init()
pygame.mixer.init()

WIDTH = 800
HEIGHT = 800
FPS = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0,0,0)
YELLOW = (255, 255, 0)

keyState = pygame.key.get_pressed()

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32, 32))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.centery = HEIGHT/2
        self.vel_x = 120
        self.pos_x = 0
    
    def update(self, dt):
        self.pos_x += self.vel_x * dt
        if self.pos_x > WIDTH:
            self.pos_x = 0
        self.rect.x = self.pos_x
        
player = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)

gameRunning = True

while gameRunning:
    dt = clock.tick(FPS) / 1000
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False
    
    screen.fill(BLACK)
    all_sprites.draw(screen)
    all_sprites.update(dt)
    
    pygame.display.flip()

pygame.quit()
quit()