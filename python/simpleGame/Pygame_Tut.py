# import the pygame module
import pygame
from os import path
# initialize the pygame module
pygame.init()
# creating pygame window and title
window = pygame.display.set_mode((500, 480))
pygame.display.set_caption('game')
clock = pygame.time.Clock()
# works on linux and mac
game_folder = path.dirname(__file__)
bullet_sound = pygame.mixer.Sound(path.join(game_folder, 'bullet.wav'))
hit_sound = pygame.mixer.Sound(path.join(game_folder, 'hit.wav'))
music = pygame.mixer.music.load(path.join(game_folder, 'music.mp3'))
pygame.mixer.music.play(-1)

walkRight = [pygame.image.load(path.join(game_folder, 'R1.png')),
            pygame.image.load(path.join(game_folder, 'R2.png')),
            pygame.image.load(path.join(game_folder, 'R3.png')),
            pygame.image.load(path.join(game_folder, 'R4.png')),
            pygame.image.load(path.join(game_folder, 'R5.png')),
            pygame.image.load(path.join(game_folder, 'R6.png')),
            pygame.image.load(path.join(game_folder, 'R7.png')),
            pygame.image.load(path.join(game_folder, 'R8.png')),
            pygame.image.load(path.join(game_folder, 'R9.png'))]

walkLeft = [pygame.image.load(path.join(game_folder, 'L1.png')),
            pygame.image.load(path.join(game_folder, 'L2.png')), 
            pygame.image.load(path.join(game_folder, 'L3.png')), 
            pygame.image.load(path.join(game_folder, 'L4.png')), 
            pygame.image.load(path.join(game_folder, 'L5.png')), 
            pygame.image.load(path.join(game_folder, 'L6.png')), 
            pygame.image.load(path.join(game_folder, 'L7.png')), 
            pygame.image.load(path.join(game_folder, 'L8.png')), 
            pygame.image.load(path.join(game_folder, 'L9.png'))]

bg = pygame.image.load(path.join(game_folder, 'bg.jpg'))
char = pygame.image.load(path.join(game_folder, 'standing.png'))
score = 0

class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = True
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 20, 52)
        
    def draw(self, window):
        
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        
        if not self.standing:
            if self.left:
                window.blit(walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                window.blit(walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.left:
                window.blit(walkLeft[0], (self.x, self.y))
            elif self.right:
                window.blit(walkRight[0], (self.x, self.y))
        
        self.hitbox = (self.x + 17, self.y + 11, 20, 52)
        #pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)
        
    def hit(self):
        self.x = 60
        self.y = 410
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5', 1, (255, 0, 0))
        window.blit(text, (250 - (text.get_width()/2), 200))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()


class Projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.velocity = 8 * self.facing

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y),self.radius)

class Enemy(object):
    walkRight = [pygame.image.load(path.join(game_folder, 'R1E.png')),
                pygame.image.load(path.join(game_folder, 'R2E.png')),
                pygame.image.load(path.join(game_folder, 'R3E.png')),
                pygame.image.load(path.join(game_folder, 'R4E.png')),
                pygame.image.load(path.join(game_folder, 'R5E.png')),
                pygame.image.load(path.join(game_folder, 'R6E.png')),
                pygame.image.load(path.join(game_folder, 'R7E.png')),
                pygame.image.load(path.join(game_folder, 'R8E.png')),
                pygame.image.load(path.join(game_folder, 'R9E.png')),
                pygame.image.load(path.join(game_folder, 'R10E.png')),
                pygame.image.load(path.join(game_folder, 'R11E.png'))]

    walkLeft = [pygame.image.load(path.join(game_folder, 'L1E.png')),
                pygame.image.load(path.join(game_folder, 'L2E.png')),
                pygame.image.load(path.join(game_folder, 'L3E.png')),
                pygame.image.load(path.join(game_folder, 'L4E.png')),
                pygame.image.load(path.join(game_folder, 'L5E.png')),
                pygame.image.load(path.join(game_folder, 'L6E.png')),
                pygame.image.load(path.join(game_folder, 'L7E.png')),
                pygame.image.load(path.join(game_folder, 'L8E.png')),
                pygame.image.load(path.join(game_folder, 'L9E.png')),
                pygame.image.load(path.join(game_folder, 'L10E.png')),
                pygame.image.load(path.join(game_folder, 'L11E.png'))]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.velocity = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    def draw(self, window):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0
                
            if self.velocity > 0:
                window.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
                
            elif self.velocity < 0:
                window.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            
            pygame.draw.rect(window, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(window, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, (50 - (50/10)*(10-self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            #pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)
    
    def move(self):
        if self.velocity > 0:
            if self.x + self.velocity < self.path[1]:
                self.x += self.velocity
            else:
                self.velocity = self.velocity * -1
                self.walkCount = 0
        else:
            if self.x - self.velocity > self.path[0]:
                self.x += self.velocity
            else:
                self.velocity = self.velocity * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
            
        hit_sound.play()
        print('hit')
        

# functions
def redrawGameWindow():
    window.blit(bg, (0, 0))
    text = font.render('Score: '+ str(score), 1, (0, 0, 0))
    window.blit(text, (390, 10))
    man.draw(window)
    goblin.draw(window)
    for bullet in bullets:
        bullet.draw(window)
    pygame.display.update()


# mainloop
font = pygame.font.SysFont('comicsans', 30, True, True)
man = Player(300, 400, 64, 64)
goblin = Enemy(100, 400, 64, 64, 450)
bullets = []
shootLoop = 0
run = True

while run:
    # without this line the square willl fly around
    # the less the value the faster the square will move
    clock.tick(27)
    # checking for events
    if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
        if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
            man.hit()
            score -= 5
    
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                goblin.hit()
                bullets.pop(bullets.index(bullet))
                score += 1
                
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.velocity
        else:
            bullets.pop(bullets.index(bullet))

    # movement; keys is a variman.able that we create in order not to write
    # pygame.key.get_pressed()[desiredkey]
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and shootLoop == 0:
        bullet_sound.play()
        if man.left:
            facing = - 1
        elif man.right:
            facing = 1
        if len(bullets) < 5:
            bullets.append(Projectile(round(man.x + man.width//2), round(man.y + man.height//2), 6, (0, 0, 0), facing))
        shootLoop = 1
    
    if keys[pygame.K_LEFT] and man.x > man.velocity:
        man.x -= man.velocity
        man.left = True
        man.right = False
        man.standing = False

    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.velocity:
        man.x += man.velocity
        man.left = False
        man.right = True
        man.standing = False

    else:
        man.standing = True
        man.walkCount = 0

    if not (man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.left = False
            man.right = False
            man.walkCount = 0

    else:
        if man.jumpCount >= - 10:
            neg = 1
            if man.jumpCount < 0:
                neg = - 1
            man.y -= (man.jumpCount ** 2)* 0.5 * neg
            man.jumpCount -= 1

        else:
            man.isJump = False
            man.jumpCount = 10
    redrawGameWindow()


pygame.quit()
