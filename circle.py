import pygame
pygame.init()
window=pygame.display.set_mode((400,400))
window.fill((0,12,222))
green=(0,255,0)
pygame.draw.circle(window,green,(100,100),50)
pygame.draw.circle(window,green,(200,200),50,2)
pygame.display.update()
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
pygame.quit()


