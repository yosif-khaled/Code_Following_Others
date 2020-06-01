# We convert to an executable by using cx-Freeze
# you need to install a zlibg1 or something then pip3

import pygame
import time
import random
from os import path

pygame.init()
clock = pygame.time.Clock()
FPS = 15
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
blue = (0, 0, 255)
display_width = 800
display_height = 600
img_folder = path.dirname(__file__)
direction = 'right'
block_size = 20
appleThickness = 40

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Slither')
icon = pygame.image.load(path.join(img_folder, 'snakehead.png'))
icon = pygame.transform.scale(icon, (32, 32))
pygame.display.set_icon(icon)

smallfont = pygame.font.SysFont('comicsansms', 25)
medfont = pygame.font.SysFont('comicsansms', 50)
largefont = pygame.font.SysFont('comicsansms', 80)


img = pygame.image.load(path.join(img_folder, 'snakehead.png'))
appleimg = pygame.image.load(path.join(img_folder, 'apple.png'))
appleimg = pygame.transform.scale(appleimg, (32, 32))

def pause():
    
    paused = True
    message_to_screen('PAUSED',
                          black,
                          -100,
                          'large')
    message_to_screen('Press C to Play Again or Q to Quit',
                        black,
                        25)
    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        #gameDisplay.fill(white)
 
def score(score):
    text = smallfont.render('Score: '+str(score), True, black)
    gameDisplay.blit(text, [0,0])

def randAppleGen():
    randAppleX = round(random.randrange(0 + 10, display_width - appleThickness))#/10.0)*10.0
    randAppleY = round(random.randrange(0 + 10, display_height - appleThickness))#/10.0)*10.0
    return randAppleX, randAppleY

randAppleX, randAppleY = randAppleGen()

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.fill(white)
        message_to_screen('Welcome to Slither',
                          green,
                          -100,
                          'large')
        message_to_screen('The Objective of the game is to eat red apples',
                          black,
                          -30,
                          'small')
        message_to_screen('the more apples you eat the longer you will be',
                          black,
                          10,
                          'small')
        message_to_screen('if you run into yourself or the edges you will die',
                          black,
                          50,
                          'small')
        message_to_screen('Press c to play or q to quit',
                          black,
                          180,
                          size='small')
        pygame.display.update()
        clock.tick(15)

def snake(block_size, snakelist):
    
    if direction == 'right':
        head = pygame.transform.rotate(img, 180)
    if direction == 'left':
        head = pygame.transform.rotate(img, 0)
    if direction == 'up':
        head = pygame.transform.rotate(img, 270)
    if direction == 'down':
        head = pygame.transform.rotate(img, 90)
        
    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay,
                        green,
                        (XnY[0], XnY[1], block_size, block_size))

def text_objects(text, color, size):
    if size == 'small':
        textSurface = smallfont.render(text, True, color)
    if size == 'medium':
        textSurface = medfont.render(text, True, color)
    if size == 'large':
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color, y_displace=0, size = 'small'):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width/2), (display_height/2) + y_displace
    gameDisplay.blit(textSurf, textRect)

def gameLoop():
    global direction
    direction = 'right'
    lead_x = display_width//2
    lead_y = display_height//2
    lead_x_change = 10
    lead_y_change = 0
    snakelist = []
    snakelength = 1
    randAppleX, randAppleY = randAppleGen()
    
    gameExit = False
    gameOver = False
    
    while not gameExit:
        clock.tick(FPS)
        
        if gameOver == True:
            message_to_screen('Game Over',
                              red,
                              y_displace=-50,
                              size = 'large')
            message_to_screen('Press c to play again or q to quit',
                              black,
                              50,
                              size = 'medium')
            pygame.display.update()

        while gameOver:
            #gameDisplay.fill(white)
  
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = 'left'
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = 'right'
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = 'up'
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = 'down'
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_p:
                    pause()
            
        if lead_x >= display_width or lead_x <= 0 or lead_y <= 0 or lead_y >= display_height:
            gameOver = True
        
        
        lead_x += lead_x_change
        lead_y += lead_y_change
        
        gameDisplay.fill(white)
        gameDisplay.blit(appleimg, (randAppleX, randAppleY))

        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)
        
        if len(snakelist)>snakelength:
            del snakelist[0]
            
        for eachsegment in snakelist[:-1]:
            if eachsegment == snakehead:
                gameOver = True
        
        snake(block_size, snakelist)
        
        score(snakelength - 1)
        
        pygame.display.update()
        
        if lead_x > randAppleX and lead_x < randAppleX + appleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + appleThickness:
            if lead_y > randAppleY and lead_y < randAppleY + appleThickness or lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + appleThickness:
                randAppleX, randAppleY = randAppleGen()
                snakelength += 1
        
    pygame.quit()
    quit()
    
game_intro()
gameLoop()
