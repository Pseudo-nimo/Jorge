import pygame

pasta = "..\\assets\\"
gravidade = 9
class parede():
    distancia = 200
    
    
    cano1 = pygame.sprite.Sprite()
    cano2 = pygame.sprite.Sprite()

    
    def __init__(self):
        a=1
    def lepard(self):
        cano1.rect = cano1.image.get_rect()
        cano1.image = pygame.image.load(pasta+"canos_a.png")
        cano1.rect.top = -100
        cano2.image = pygame.image.load(pasta+"canos_b.png")
        cano2.rect = cano2.image.get_rect()
        cano2.rect.top = (cano1.rect.bottom + distancia)
        cano2.rect.centerx = cano1.rect.centerx
        
class player(pygame.sprite.Sprite):
    
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(pasta+"ave.png")  # qual imagem
        self.rect = self.image.get_rect()
    
    #gravidade = 0
    def jump(self):
        global gravidade
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE:
                    print("debug")
                    gravidade = -20
                    gravidade = gravidade + 1
        self.rect.y = self.rect.y + gravidade



#screen.blit(heroi, heroi_rect)
        
