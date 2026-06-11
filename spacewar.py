import math
import random 
import pygame
screen_width=800
screen_height=500
player_start_x=370
player_start_y=380
enemy_start_y_min=50
enemy_start_y_max=150
enemy_speed_x=4
enemy_speed_y=40
bullet_speed_y=10
collision_distance=27
pygame.init()
screen=pygame.display.set_mode((screen_width,screen_height))
background=pygame.image.load('background.png')
pygame.display.set_caption("space invader")
icon=pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
playerimage=pygame.image.load('player.png')
playerx=player_start_x
playery=player_start_y
playerx_change=0
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for _i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, screen_width - 64))  # 64 is the size of the enemy
    enemyY.append(random.randint(enemy_start_y_max,enemy_start_y_min))
    enemyX_change.append(enemy_speed_x)
    enemyY_change.append(enemy_speed_y)
bulletImg=pygame.image.load('bullet.png')
bulletx=0
bullety=player_start_y
bulletx_change=0
bullety_change=bullet_speed_y
bullet_state="ready"
scorevalue=0
font=pygame.font.Font("TimesNewRoman",38)
textx=10
texty=10
overfont=pygame.font.Font("TimesNewRoman",70)
def show_score(x,y):
    score=font.render("score:",+str(scorevalue),True,(255,255,255))
    screen.blit(score,(x,y))
def game_over_text():
    over=overfont.render("Game Over!",True,(255,255,255))
    screen.blit(over,(200,250))
def player(x,y):
    screen.blit(playerimage,(x,y))
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))
def fire_bullets(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10))
def iscollision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt((enemyX-bulletX)**2 +(enemyY-bulletY)**2)
    return distance<collision_distance
