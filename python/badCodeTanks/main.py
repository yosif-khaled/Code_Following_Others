## the code is ugly
## the cleanliness of the code impacts its functionality really hard
## so always write clean code
## I didn't follow tut 83 because adding sounds is not really a big deal
## I also started to appreciate OOP more than Functional or procedural
## in OOP I don't have to write bits of code tons of times over and over

import random
import pygame

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Tanks')

#icon = pygame.image.load('SlitherWindowIcon.png')
#pygame.display.set_icon(icon)

white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)
yellow = (200, 200, 0)
light_green = (0, 255, 0)
light_yellow = (255, 255, 0)
light_red = (255, 0, 0)

clock = pygame.time.Clock()

mainTankX = display_width * 0.9
mainTankY = display_height * 0.9

tankWidth = 40
tankHeight = 20

turretWidth = 5
wheelWidth = 5

ground_height = 35

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

#img = pygame.image.load('SlitherSnakeHead.png')
#appleimg = pygame.image.load('PerfectRedApple.png')

def score(score):
    text = smallfont.render("Score: " + str(score), True, black)
    gameDisplay.blit(text, [0, 0])

def text_objects(text, color, size):

    if size == "small":
        textSurface = smallfont.render(text, True, color)

    elif size == "medium":
        textSurface = medfont.render(text, True, color)

    elif size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()


def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size='small'):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (buttonx+(buttonwidth/2)), (buttony+(buttonheight/2))
    gameDisplay.blit(textSurf, textRect)




def message_to_screen(msg, color, y_displace=0, size="small"):

    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width / 2), (display_height / 2) + y_displace
    gameDisplay.blit(textSurf, textRect)


def tank(x, y, turPos):

    x = int(x)
    y = int(y)

    possibleTurrets = [(x-27, y-2), (x-26, y-5), (x-25, y-8), (x-23, y-12), (x-20, y-14), (x-18, y-15), (x-15, y-17), (x-13, y-19), (x-11, y-21)] # A List of Tuples


    pygame.draw.circle(gameDisplay, black, (x, y), int(tankHeight/2))


    pygame.draw.rect(gameDisplay, black, (x-tankHeight, y, tankWidth, tankHeight))


    pygame.draw.line(gameDisplay, black, (x, y), possibleTurrets[turPos], turretWidth)

    startX = 15

    for i in range(7):
        pygame.draw.circle(gameDisplay, black, (x-startX, y+20), wheelWidth)
        startX -= 5

    return possibleTurrets[turPos]


def enemy_tank(x, y, turPos):

    x = int(x)
    y = int(y)

    possibleTurrets = [(x+27, y-2), (x+26, y-5), (x+25, y-8), (x+23, y-12), (x+20, y-14), (x+18, y-15), (x+15, y-17), (x+13, y-19), (x+11, y-21)] # A List of Tuples


    pygame.draw.circle(gameDisplay, black, (x, y), int(tankHeight/2))


    pygame.draw.rect(gameDisplay, black, (x-tankHeight, y, tankWidth, tankHeight))


    pygame.draw.line(gameDisplay, black, (x, y), possibleTurrets[turPos], turretWidth)

    startX = 15

    for i in range(7):
        pygame.draw.circle(gameDisplay, black, (x-startX, y+20), wheelWidth)
        startX -= 5

    return possibleTurrets[turPos]


def game_controls():
    gcont = True

    while gcont:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        message_to_screen("Controls", green, y_displace=-100, size="large")
        message_to_screen("Fire : Spacebar", black, y_displace=-30)
        message_to_screen("Move Turret : Up and Down Arrows", black, y_displace=10)
        message_to_screen("Move Tank : Left and Right Arrows", black, y_displace=50)
        message_to_screen("Press P to Puase", black, y_displace=90)

        button('PLAY', 150, 500, 100, 50, green, light_green, action= 'play')
        #button('Main', 350, 500, 100, 50, yellow, light_yellow, action= 'main')
        button('QUIT', 550, 500, 100, 50, red, light_red, action= 'quit')

        pygame.display.update()
        clock.tick(15)


def button(text, x, y, width, height, inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click) basicly a tuple (first bottun state, middle button state, right button state)

    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == 'quit':
                pygame.quit()
                quit()
            if action == 'controls':
                game_controls()

            if action == 'play':
                gameLoop()

            if action == 'main':
                game_intro()
            #print('Action', x)
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))

    text_to_button(text, black, x, y, width, height)

def pause():

    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()



        gameDisplay.fill(white)
        message_to_screen("Paused", black, -100, size="large")
        message_to_screen("Press C to continue or Q to quit.", black, 25)
        pygame.display.update()
        clock.tick(5)


def barrier(xlocation, randomHeight, barrier_width):

    pygame.draw.rect(gameDisplay, black, [xlocation, display_height-randomHeight, barrier_width, randomHeight])


def explosion(x, y, size=50):

    explode = True

    while explode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        startPoint = x, y

        colorChoices = [red, light_red, yellow, light_yellow]

        magnitude = 1

        while magnitude < size:

            exploding_bit_x = x + random.randrange(-1*magnitude, magnitude)
            exploding_bit_y = y + random.randrange(-1*magnitude, magnitude)

            pygame.draw.circle(gameDisplay, random.choice(colorChoices), (exploding_bit_x, exploding_bit_y), random.randrange(1, 5))
            magnitude += 1

            pygame.display.update()
            clock.tick(100)

        explode = False


def fireShell(xy, tankx, tanky, turPos, gun_power, xlocation, barrier_width, randomHeight, enemyTankX, enemyTankY):

    damage = 0

    fire = True
    startingShell = list(xy)

    print('Fire!!', xy)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.draw.circle(gameDisplay, red, (startingShell[0], startingShell[1]), 5)
        startingShell[0] -= (12 - turPos)*2
        startingShell[1] += int((((startingShell[0]-xy[0])*0.01/(gun_power/50))**2) - (turPos+turPos/(12-turPos)))

        if startingShell[1] > display_height - ground_height:
            hit_x = int((startingShell[0]*display_height- ground_height)/ startingShell[1])
            hit_y = int(display_height - ground_height)
            print("Impact : ", hit_x, hit_y)
            if enemyTankX + 10 > hit_x > enemyTankX - 10:
                damage = 25
                print('Critical Hit')
            elif enemyTankX + 15 > hit_x > enemyTankX - 15:
                damage = 20
                print('Hard Hit')
            elif enemyTankX + 20 > hit_x > enemyTankX - 20:
                damage = 15
                print('Medium Hit')
            elif enemyTankX + 30 > hit_x > enemyTankX - 30:
                damage = 10
                print('Light Hit')
            explosion(hit_x, hit_y)
            fire = False

        check_x_1 = startingShell[0] <= xlocation + barrier_width
        check_x_2 = startingShell[0] >= xlocation
        check_y_1 = startingShell[1] <= display_height
        check_y_2 = startingShell[1] >= display_height - randomHeight

        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            print('Last Shell: ', startingShell[0], startingShell[1])
            hit_x = int(startingShell[0])
            hit_y = int(startingShell[1])
            print("Impact : ", hit_x, hit_y)
            explosion(hit_x, hit_y)
            fire = False

        pygame.display.update()
        clock.tick(60)
    return damage


def e_fireShell(xy, tankx, tanky, turPos, gun_power, xlocation, barrier_width, randomHeight, ptankx, ptanky):

    damage = 0
    currentPower = 1
    power_found = False

    while not power_found:
        currentPower += 1
        if currentPower > 100:
            power_found = True
            print(currentPower)

        fire = True
        startingShell = list(xy)


        while fire:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            startingShell[0] += (12 - turPos)*2

            gun_power = random.randrange(int(currentPower*0.8), int(currentPower*1.2))

            startingShell[1] += int((((startingShell[0]-xy[0])*0.01/(gun_power/50))**2) - (turPos+turPos/(12-turPos)))

            if startingShell[1] > display_height - ground_height:
                hit_x = int((startingShell[0]*display_height- ground_height)/ startingShell[1])
                hit_y = int(display_height - ground_height)
                if ptankx + 15 > hit_x > ptankx - 15:
                    print('Target Acquired')
                    power_found = True
                fire = False

            check_x_1 = startingShell[0] <= xlocation + barrier_width
            check_x_2 = startingShell[0] >= xlocation
            check_y_1 = startingShell[1] <= display_height
            check_y_2 = startingShell[1] >= display_height - randomHeight

            if check_x_1 and check_x_2 and check_y_1 and check_y_2:
                hit_x = int(startingShell[0])
                hit_y = int(startingShell[1])
                fire = False



    fire = True
    startingShell = list(xy)

    print('Fire!!', xy)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.draw.circle(gameDisplay, red, (startingShell[0], startingShell[1]), 5)
        startingShell[0] += (12 - turPos)*2
        startingShell[1] += int((((startingShell[0]-xy[0])*0.01/(currentPower/50))**2) - (turPos+turPos/(12-turPos)))

        if startingShell[1] > display_height - ground_height:
            print('Last Shell: ', startingShell[0], startingShell[1])
            hit_x = int((startingShell[0]*display_height- ground_height)/ startingShell[1])
            hit_y = int(display_height - ground_height)
            print("Impact : ", hit_x, hit_y)
            if ptankx + 10 > hit_x > ptankx - 10:
                damage = 25
                print('Critical Hit')
            elif ptankx + 15 > hit_x > ptankx - 15:
                damage = 20
                print('Hard Hit')
            elif ptankx + 20 > hit_x > ptankx - 20:
                damage = 15
                print('Medium Hit')
            elif ptankx + 30 > hit_x > ptankx - 30:
                damage = 10
                print('Light Hit')
            explosion(hit_x, hit_y)
            fire = False

        check_x_1 = startingShell[0] <= xlocation + barrier_width
        check_x_2 = startingShell[0] >= xlocation
        check_y_1 = startingShell[1] <= display_height
        check_y_2 = startingShell[1] >= display_height - randomHeight

        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            print('Last Shell: ', startingShell[0], startingShell[1])
            hit_x = int(startingShell[0])
            hit_y = int(startingShell[1])
            print("Impact : ", hit_x, hit_y)
            explosion(hit_x, hit_y)
            fire = False

        pygame.display.update()
        clock.tick(60)
    return damage

def power(level):
    text = smallfont.render("Power: "+ str(level)+'%', True, black)
    gameDisplay.blit(text, (display_width/2, 0))


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
        message_to_screen("Welcome to Tanks!", green, y_displace=-100, size="large")
        message_to_screen("The objective of the game is to shoot and destroy", black, y_displace=-30)
        message_to_screen("the enemy tank before they destroy you.", black, y_displace=10)
        message_to_screen("The more enemies you destroy, the harder they get!", black, y_displace=50)
        #message_to_screen("Press C to play, P to pause or Q to quit.", black, y_displace=180)


        button('PLAY', 150, 500, 100, 50, green, light_green, action= 'play')
        button('Controls', 350, 500, 100, 50, yellow, light_yellow, action= 'controls')
        button('QUIT', 550, 500, 100, 50, red, light_red, action= 'quit')

        pygame.display.update()
        clock.tick(15)


def game_over():
    game_over = True

    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    game_over = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("Game Over!", green, y_displace=-100, size="large")
        message_to_screen("YOU DIED", black, y_displace=-30)
        #message_to_screen("the enemy tank before they destroy you.", black, y_displace=10)
        #message_to_screen("The more enemies you destroy, the harder they get!", black, y_displace=50)
        #message_to_screen("Press C to play, P to pause or Q to quit.", black, y_displace=180)


        button('PLAY AGAIN', 150, 500, 150, 50, green, light_green, action= 'play')
        button('Controls', 350, 500, 100, 50, yellow, light_yellow, action= 'controls')
        button('QUIT', 550, 500, 100, 50, red, light_red, action= 'quit')

        pygame.display.update()
        clock.tick(15)

def you_win():
    win = True

    while win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    win = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("You Win!", green, y_displace=-100, size="large")
        #message_to_screen("YOU DIED", black, y_displace=-30)
        #message_to_screen("the enemy tank before they destroy you.", black, y_displace=10)
        #message_to_screen("The more enemies you destroy, the harder they get!", black, y_displace=50)
        #message_to_screen("Press C to play, P to pause or Q to quit.", black, y_displace=180)


        button('PLAY', 150, 500, 100, 50, green, light_green, action= 'play')
        button('Controls', 350, 500, 100, 50, yellow, light_yellow, action= 'controls')
        button('QUIT', 550, 500, 100, 50, red, light_red, action= 'quit')

        pygame.display.update()
        clock.tick(15)

def health_bars(player_health, enemy_health):

    if player_health > 75:
        player_health_color = green
    elif player_health > 50:
        player_health_color = yellow
    else:
        player_health_color = red

    if enemy_health > 75:
        enemy_health_color = green
    elif enemy_health > 50:
       enemy_health_color = yellow
    else:
        enemy_health_color = red

    pygame.draw.rect(gameDisplay, player_health_color, (680, 25, player_health, 25))
    pygame.draw.rect(gameDisplay, enemy_health_color, (20, 25, enemy_health, 25))


def gameLoop():

    gameExit = False
    gameOver = False
    FPS = 15

    global enemy_health_color
    global player_health_color

    player_health = 100
    enemy_health = 100

    global mainTankX
    global mainTankY

    tankMove = 0

    currentTurPos = 0
    changeTur = 0


    enemyTankX = display_width * 0.1
    enemyTankY = display_height * 0.9


    fire_power = 50
    power_change = 0

    xlocation = (display_width/2) + random.randint(-0.2 * display_width, 0.2 * display_width)
    randomHeight = random.randrange(display_height*0.3, display_height*0.5)

    barrier_width = 50

    while not gameExit:
        while gameOver == True:
            #gameDisplay.fill(white)
            message_to_screen("Game over!", red, y_displace=-50, size="large")
            message_to_screen("Press C to play again or Q to quit", black, y_displace=50, size="medium")
            pygame.display.update()

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
                    tankMove = -5

                elif event.key == pygame.K_RIGHT:
                    tankMove = 5

                elif event.key == pygame.K_UP:
                    changeTur = 1

                elif event.key == pygame.K_DOWN:
                    changeTur = -1

                elif event.key == pygame.K_p:
                    pause()

                elif event.key == pygame.K_SPACE:
                    damage = fireShell(gun, mainTankX, mainTankY, currentTurPos, fire_power, xlocation, barrier_width, randomHeight, enemyTankX, enemyTankY)
                    enemy_health -= damage
                    print(damage, "to enemy")


                    possibleMovement = ['f', 'r']
                    moveIndex = random.randrange(0,2)

                    for x in range(random.randrange(0, 2)):
                        if display_width * 0.1 > enemyTankX > display_width * 0.4:
                            if possibleMovement[moveIndex] == 'f':
                                enemyTankX += 5
                            elif possibleMovement[moveIndex] == 'r':
                                enemyTankX -= 5
                            gameDisplay.fill(white)
                            health_bars(player_health, enemy_health)
                            gun = tank(mainTankX, mainTankY, currentTurPos)
                            enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
                            
                            power(fire_power)

                            barrier(xlocation, randomHeight, barrier_width)

                            gameDisplay.fill(green, rect=(0, display_height - ground_height, display_width, ground_height))

                            pygame.display.update()


                    damage = e_fireShell(enemy_gun, enemyTankX, enemyTankY, 8, 50, xlocation, barrier_width, randomHeight, mainTankX, mainTankY)
                    player_health -= damage
                    print(damage)

                elif event.key == pygame.K_a:
                    power_change = -1

                elif event.key == pygame.K_d:
                    power_change = 1

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeTur = 0
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    power_change = 0


        mainTankX += tankMove
        currentTurPos += changeTur
        fire_power += power_change

        if currentTurPos > 8:
            currentTurPos = 8
        elif currentTurPos < 0:
            currentTurPos = 0

        if mainTankX - (tankWidth/2) < xlocation + barrier_width:
            mainTankX += 5

        gameDisplay.fill(white)
        health_bars(player_health, enemy_health)
        gun = tank(mainTankX, mainTankY, currentTurPos)
        enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
        
        power(fire_power)


        barrier(xlocation, randomHeight, barrier_width)

        gameDisplay.fill(green, rect=(0, display_height - ground_height, display_width, ground_height))

        pygame.display.update()
        
        if player_health < 1:
            game_over()
        elif enemy_health < 1:
            you_win()

        clock.tick(FPS)

    pygame.quit()
    quit()

game_intro()
gameLoop()