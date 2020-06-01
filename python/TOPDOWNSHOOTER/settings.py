import pygame
vec = pygame.math.Vector2

# CONSTANTS

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
LIGHTGREY = (40, 40, 40)
BROWN = (106, 55, 5)

# Game Properties
WIDTH = 1024
HEIGHT = 768
FPS = 60
TITLE = 'ZOMBIE'
BGCOLOR = BROWN

TILESIZE = 64
GRIDWIDTH = WIDTH/TILESIZE
GRIDHEIGHT = HEIGHT/TILESIZE

# Wall IMAGE
WALL_IMG = 'wall_img.png'

# Player Properties
PLAYER_HEALTH = 100
PLAYER_SPEED = 200
PLAYER_ROT_SPEED = 250
PLAYER_IMG = 'manBlue_gun.png'
PLAYER_HIT_RECT = pygame.Rect(0, 0, 35, 35)
BARREL_OFFSET = vec(30, 10)

# Weapon Properties
BULLET_IMG = 'bullet.png'
WEAPONS = {}
WEAPONS['pistol'] = {'bullet_speed': 500,
                     'bullet_lifetime': 1000,
                     'rate': 250,
                     'kickback': 200,
                     'spread': 5,
                     'damage': 10,
                     'bullet_size': 'lg',
                     'bullet_count': 1}

WEAPONS['shotgun'] = {'bullet_speed': 400,
                     'bullet_lifetime': 500,
                     'rate': 900,
                     'kickback': 300,
                     'spread': 20,
                     'damage': 5,
                     'bullet_size': 'sm',
                     'bullet_count': 12}

""" we don't need these variables anymore
BULLET_SPEED = 500
BULLET_LIFETIME = 1000
BULLET_RATE = 150
KICKBACK = 200
GUN_SPREAD = 5
BULLET_DAMAGE = 10
"""
# Mob Properties
MOB_IMG = "zoimbie1_hold.png"
MOB_SPEED = [150, 100, 75, 50]
MOB_HIT_RECT = pygame.Rect(0, 0, 30, 30)
MOB_HEALTH = 100
MOB_DAMAGE = 10
MOB_KNOCKBACK = 20
AVOID_RADIUS = 50
DETECT_RADIUS = 400
SPLAT = 'splat green.png'

# Effects
MUZZLE_FLASH = ['flash00.png','flash01.png','flash02.png',
                'flash03.png','flash04.png','flash05.png',
                'flash06.png','flash07.png','flash08.png']
FLASH_DURATION = 40
DAMAGE_ALPHA = [i for i in range(0, 255, 25)]
NIGHT_COLOR = (20, 20, 20)
LIGHT_RADIUS = (500, 500)
LIGHT_MASK = "light_350_med.png"

# Layers
WALL_LAYER = 1
PLAYER_LAYER = 2
BULLET_LAYER = 3
MOB_LAYER = 2
EFFECTS_LAYER = 4
ITEMS_LAYER  = 1

# Items
ITEM_IMAGES = {'health': 'health_pack.png',
               'shotgun': 'obj_shotgun.png'}
HEALTH_PACK_AMOUNT = 20
BOB_RANGE = 20
BOB_SPEED = 0.6

# Sounds
BG_MUSIC = 'espionage.ogg'
PLAYER_HIT_SOUNDS = ['pain/8.wav','pain/9.wav',
                     'pain/10.wav','pain/10.wav']
ZOMBIE_MOAN_SOUNDS = ['brains2.wav','brains3.wav',
                      'zombie-roar-1.wav','zombie-roar-2.wav',
                      'zombie-roar-3.wav','zombie-roar-4.wav',
                      'zombie-roar-5.wav','zombie-roar-6.wav',
                      'zombie-roar-7.wav','zombie-roar-8.wav']
ZOMBIE_HIT_SOUNDS = ['splat-15.wav']
WEAPON_SOUNDS = {'pistol': ['sfx_weapon_singleshot2.wav'],
                 'shotgun': ['shotgun.wav']}
EFFECTS_SOUNDS = {'level_start': 'level_start.wav',
                  'health_up': 'health_pack.wav',
                  'gun_pickup': 'gun_pickup.wav'}