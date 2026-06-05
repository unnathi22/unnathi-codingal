import pygame
pygame.init()
screen=pygame.display.set_mode((600,700))
font=pygame.font.SysFont("Arial",38)
text=font.render("this is rectangle",True,"Green")
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    screen.fill("YELLOW")
    pygame.draw.rect(screen,"Green",pygame.Rect(80,80,90,90))
    screen.blit(text,(100,200))
    pygame.display.update()
pygame.quit()