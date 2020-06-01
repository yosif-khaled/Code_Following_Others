import pygame
import random


# constants
WIDTH = 360
HEIGHT = 480
FPS = 30

# defining colors (r, g, b)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# window and sound initialization
pygame.init() # intialize pygame
pygame.mixer.init() # initialize sounds
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # initialize screen size notice the double bracket
pygame.display.set_caption("pygame_skeleton") # the screen title
clock = pygame.time.Clock() # responsible for speed and how fast things are going


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


	# draw / render
	screen.fill(BLACK)
	# after drawing everything flip display
	pygame.display.flip() #initialize double buffering


pygame.quit()