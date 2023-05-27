import pygame
class parede():
    distancia = 200
    pasta = "./assets/"
    cano1 = pygame.sprite.Sprite()
    cano2 = pygame.sprite.Sprite()

    
    def __init__(self):
        cano1.rect = cano1.image.get_rect()
        cano1.image = pygame.image.load(pasta+"canos_a.png")
        cano1.rect.top = -100
        cano2.image = pygame.image.load(pasta+"canos_b.png")
        cano2.rect = cano2.image.get_rect()
        cano2.rect.top = (cano1.rect.bottom + distancia)
        cano2.rect.centerx = cano1.rect.centerx