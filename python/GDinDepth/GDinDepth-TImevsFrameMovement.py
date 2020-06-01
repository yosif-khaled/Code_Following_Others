import pygame

# Pygame Initialization
pygame.init()
pygame.mixer.init()

# The Clock
clock = pygame.time.Clock()

# KEYSTATE
keyState = pygame.key.get_pressed()

# DISPLAY Variables
WIDTH = 800
HEIGHT = 800
FPS = 60 # Frame_Rate
    ## COLORS
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 255)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)

# Game Loop Conditions
gameOver = True
gameRunning = True

# Creating The Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))


# CLASSES
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64,64))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.centery = HEIGHT/2
        self.dx = 120

    def update(self, dt):
        # Motion
        global FPS
        self.rect.x += self.dx * dt
        if self.rect.left >= WIDTH:
            self.rect.left = 0
        print(FPS)
        keyState = pygame.key.get_pressed()
        if keyState[pygame.K_RIGHT]:
            FPS += 5
        if keyState[pygame.K_LEFT]:
            FPS -= 5
        ## Left
        
        ## Right
        
        ## Up
        
        ## Down
        
        ### Balancing Diagonal Motion
        
        # Applying Motion
        
    def function(self):
        pass

# Initializing Game Objects
player = Player()

# Game Groups Later On SHOULD BE ADDED IN THE CLASSES
all_sprites = pygame.sprite.Group()


# Adding Sprites to Their Specific Groups
all_sprites.add(player)

# GAME LOOP
while gameRunning:
    # Setting The Frame Rate / Delta Time is dt which is how much time the previous frame took
    dt = clock.tick(FPS) / 1000 # divide by thousand to convert to secounds
    # To Exit The Game
    for event in pygame.event.get():
        # print(event) # useful/prints actions in terminal
        if event.type == pygame.QUIT:
            gameRunning = False
    
    # Screen Fill / Temporary
    screen.fill(BLACK)
    
    # Draw/Render
    all_sprites.draw(screen)
    
    # Update
    all_sprites.update(dt) # passing the delta time to the update
    
    # Screen Constant Update/Flip
    pygame.display.flip() # should always be the last line
    
pygame.quit()
quit()