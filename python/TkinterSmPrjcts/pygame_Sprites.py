import pygame
import random


# constants
WIDTH = 800
HEIGHT = 600
FPS = 30

# defining colors (r, g, b)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# player class
class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((50, 50))
		self.image.fill(GREEN)
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH / 2, HEIGHT / 2)
	
	def update(self):
		self.rect.x += 5
		if self.rect.left > WIDTH:
			self.rect.right = 0

# window and sound initialization
pygame.init() # intialize pygame
pygame.mixer.init() # initialize sounds
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # initialize screen size notice the double bracket
pygame.display.set_caption("pygame_skeleton") # the screen title
clock = pygame.time.Clock() # responsible for speed and how fast things are going

# grouping sprites
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# game loop
running = True
while running:
    # keep loop running at the right speed
	clock.tick(FPS)
	# process input (events)
	for event in pygame.event.get():
    	 if event.type == pygame.QUIT:
        	running = False
         
         
	# update
	all_sprites.update()

	# draw / render
	screen.fill(BLACK)
	all_sprites.draw(screen)
	# after drawing everything flip display
	pygame.display.flip() #initialize double buffering


pygame.quit()
