import pygame
pygame.init()
screen=pygame.display.set_mode((400,400))
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pygame.draw.rect(screen,(0,255,3),pygame.Rect(20,20,30,30))
    pygame.display.flip()
