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
    enemyY.append(random.randint(enemy_start_y_min,enemy_start_y_max))
    enemyX_change.append(enemy_speed_x)
    enemyY_change.append(enemy_speed_y)
bulletImg=pygame.image.load('bullet.png')
bulletx=0
bullety=player_start_y
bulletx_change=0
bullety_change=bullet_speed_y
bullet_state="ready"
scorevalue=0
font=pygame.font.SysFont("TimesNewRoman",38)
textx=10
texty=10
overfont=pygame.font.SysFont("TimesNewRoman",70)
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
running=True
while running:
    screen.fill((0,0,0,))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
             playerx_change=-5
            if event.key==pygame.K_RIGHT:
                playerx_change==5
            if event.key==pygame.K_SPACE and bullet_state=="ready":
                bulletx=playerx
                fire_bullets(bulletx,bullety)
        if event.type==pygame.KEYUP and event.key in [pygame.K_LEFT,pygame.K_RIGHT]:
         playerx_change=0
    playerx+=playerx_change
    playerx=max(0,min(playerx,screen_width-64))
    for i in range(num_of_enemies):
        if enemyY[i]>340:
            for j in range(num_of_enemies):
                enemyY[j]=2000
                game_over_text()
                break
        enemyX[i]=enemyX_change[i]
        if enemyX[i]<=0 or enemyX[i]>=screen_width-64:
         enemyX_change[i]*=-1
         enemyY[i]+=enemyY_change[i]
         if iscollision(enemyX[i],enemyY[i],bulletx,bullety):
             bullety=player_start_y
             bullet_state="ready"
             scorevalue+=1
             enemyX[i]=random.randint(0,screen_width-64)
             enemyY[i]=random.randint(enemy_start_y_min,enemy_start_y_max)
             enemy(enemyX[i],enemyY[i],i)
    if bullety<=0:
        bullety=player_start_y
        bullet_state="ready"
    elif bullet_state=="fire":
        fire_bullets(bulletx,bullety)
        bullety-=bullety_change
    player(playerx,playery)
    show_score(textx,texty)
    pygame.display.update()


