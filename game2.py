import pygame
import random 
screen_width,screen_height=500,300
movement_speed=5
font_size=50
pygame.init()
background_image=pygame.transform.scale(pygame.image.load("background.png"),(screen_width,screen_height))
font=pygame.font.SysFont("Times New Roman",font_size)
class sprite(pygame.sprite.Sprite()):
    def __init__(self,color,height,width):
        super().__init__()
        self.image=pygame.Surface(width,height)
        self.image.fill(pygame.Color("Blue"))
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
        self.rect=self.image.get_rect()
        
