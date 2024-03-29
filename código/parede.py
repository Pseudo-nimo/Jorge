import pygame
import random

pasta = "..\\assets\\"

class parede():
    distancia = 200
    speed =4
    canos = [pygame.sprite.Sprite(),pygame.sprite.Sprite()]
    points = 0
    reinitX = 3000
    def __init__(self):
        
        self.canos[1-1].image = pygame.image.load(pasta+"canos_a.png")
        self.canos[1-1].rect = self.canos[0].image.get_rect()
        self.canos[2-1].image = pygame.image.load(pasta+"canos_b.png")
        self.canos[2-1].rect = self.canos[1].image.get_rect()
        self.canos[0].rect.top = random.randint(-350,-200)
        self.reinitX = pygame.display.get_window_size()[0]
        self.original()
        
        
    def atualize(self):
        self.canos[1].rect.centerx = self.canos[0].rect.centerx
        self.canos[1].rect.top = (self.canos[0].rect.bottom + 200)
        
        
    def walk(self):
        self.canos[0].rect.right -= self.speed
        if self.canos[0].rect.right < 0:
            self.canos[0].rect.top = random.randint(-314,-100)
            self.original()
        if round(self.canos[0].rect.right) < round(pygame.display.get_window_size()[0]/2):
            self.points+=1
        self.atualize()
    def original(self):
        self.canos[0].rect.left = self.reinitX
        self.atualize()
    
        
    
    
        
        
class player(pygame.sprite.Sprite):
    jumpForce = 0.0
    momentum = 0.0
    gravidade = 0.0
    fps = 1
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(pasta+"ave.png")  # qual imagem
        self.rect = self.image.get_rect()
    def jump(self):        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE or event.key == pygame.K_k: 
                    self.momentum = -self.jumpForce/self.fps
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.momentum = -self.jumpForce/self.fps

        self.momentum += self.gravidade/self.fps
        self.rect.y += self.momentum
        
class button(pygame.sprite.Sprite):
    
    def __init__(self, a: str):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(pasta+a)
        self.rect = self.image.get_rect()
    


        

