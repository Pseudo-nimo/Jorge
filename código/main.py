import random
import pygame
import parede

screen = [800,600]
vivo = False
speed = 4
pisu = [pygame.sprite.Sprite(), pygame.sprite.Sprite()]
jump_Speed = 5
clock = pygame.time.Clock()
Jump = 20   # final
pontos = 0
lim_y = -314
lin_y = -100
gameLoop = True
pulo = True
etapa = 1
opacidade = 0
init = False
meio = (screen[0]/2,screen[1]/2)
# grupo
comeco = pygame.sprite.Group()
persona = pygame.sprite.Group()
grupo = pygame.sprite.Group()
tela_Final = pygame.sprite.Group()
colisors = pygame.sprite.Group()

# fonte
pygame.font.init()
fonte = pygame.font.get_default_font()
fontesys = pygame.font.SysFont(fonte, 30)


pygame.init()
display = pygame.display.set_mode(screen)

icone = pygame.image.load(parede.pasta+"ave.png")
pygame.display.set_icon(icone)
pygame.display.set_caption(parede.pasta+"Jorge")

# inicio
tela = pygame.sprite.Sprite()
tela.image = pygame.image.load(parede.pasta+"noite2.jpg")
tela.rect = tela.image.get_rect()


# scenery
fase = pygame.sprite.Sprite()
fase.image = pygame.image.load(parede.pasta+"noite.jpg")
fase.rect = fase.image.get_rect()

for i in range(2):
    pisu[i] = pygame.sprite.Sprite()
    pisu[i].image = pygame.image.load(parede.pasta+"piso.jpg")
    pisu[i].rect = pisu[i].image.get_rect()
    pisu[i].rect.bottom = 600
    colisors.add(pisu[i])
    
guy = parede.player()
cano1 = pygame.sprite.Sprite()
cano1.image = pygame.image.load(parede.pasta+"canos_a.png")
cano1.rect = cano1.image.get_rect()
cano1.rect.top = random.randint(lim_y, lin_y)
cano2 = pygame.sprite.Sprite()
cano2.image = pygame.image.load(parede.pasta+"canos_b.png")
cano2.rect = cano2.image.get_rect()
cano2.rect.top = (cano1.rect.bottom + 200)
cano2.rect.centerx = cano1.rect.centerx
cano3 = pygame.sprite.Sprite()
cano3.image = pygame.image.load(parede.pasta+"canos_a.png")
cano3.rect = cano1.image.get_rect()
cano3.rect.top = random.randint(lim_y, lin_y)
cano4 = pygame.sprite.Sprite()
cano4.image = pygame.image.load(parede.pasta+"canos_b.png")
cano4.rect = cano1.image.get_rect()
cano4.rect.top = (cano3.rect.bottom + 200)
cano4.rect.centerx = cano3.rect.centerx


preto = pygame.image.load(parede.pasta+"preto.png").convert()
inicio = parede.button("BOTAO.png")
inicio.rect.center = (meio)

againButton = pygame.sprite.Sprite()
againButton.image = pygame.image.load(parede.pasta+"Tentar novamente.png")
againButton.rect = againButton.image.get_rect()
againButton.rect.centerx = 550
againButton.rect.bottom = 450

Sair = pygame.sprite.Sprite()
Sair.image = pygame.image.load(parede.pasta+"Sair.png")
Sair.rect = Sair.image.get_rect()
Sair.rect.bottom = 450
Sair.rect.centerx = 250

def setup():
    
    speed = 0
    init = False
    pontos=0
    cano1.rect.left = 800
    cano3.rect.left = 1300
    guy.rect.centery = 300
    guy.rect.centerx = fase.rect.centerx
    guy.gravidade = 20
    persona.add(guy)

comeco.add(tela)
comeco.add(inicio)

tela_Final.add(againButton)
tela_Final.add(Sair)

grupo.add(fase)
colisors.add(cano1)
colisors.add(cano2)
colisors.add(cano3)
colisors.add(cano4)
colisors.add(pisu[0])
colisors.add(pisu[1])

# musica
pygame.mixer.music.load(parede.pasta+"Musica fofa.mp3")
pygame.mixer.music.play(0)


setup()

mouseclick = False

while gameLoop:
    print("a")
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseclick = True
            
        if event.type == pygame.MOUSEBUTTONUP:
            mouseclick = False
            
        if event.type == pygame.QUIT:
            gameLoop = False
            
            
    if etapa == 1:
        comeco.draw(display)
        if inicio.rect.collidepoint(pygame.mouse.get_pos()) and mouseclick:
            vivo = True
            etapa+=1
            
    if etapa == 2:
        
        for event in pygame.event.get():
            print("debug")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("debug")
                    init = True
                    
        if init:
            speed = 4
            guy.jump()
        else:
            speed = 0
        if guy.rect.top < -1:
            guy.rect.top = 0
            vivo = False
             
        for batida in pygame.sprite.spritecollide(guy, colisors, 0):
            vivo=False
         
        # manutencao

        grupo.draw(display)
        persona.draw(display)
        colisors.draw(display)
        txt = f"Pontuação: {pontos}"
        txttela = fontesys.render(txt, True, (0, 0, 0))
        display.blit(txttela, (50, 500))
        cano1.rect.left -= speed
        cano3.rect.left -= speed
        pisu[0].rect.x -= speed
        pisu[1].rect.x -= speed
        
        

        cano2.rect.centerx = cano1.rect.centerx
        cano4.rect.centerx = cano3.rect.centerx
        
        if cano1.rect.right < 0:
            cano1.rect.left = 850
            pontos+=1
            cano1.rect.top = random.randint(lim_y, lin_y)

            cano2.rect.top = (cano1.rect.bottom + 200)
        if cano3.rect.right < 0:
            cano3.rect.left = 850
            pontos+=1
            cano3.rect.top = random.randint(lim_y, lin_y)
            cano4.rect.top = (cano3.rect.bottom + 200)
        if pisu[1].rect.x < (-1000):
            pisu[1].rect.x = -100
            
        if not vivo:
            etapa+=1
        
    # gameover
    if etapa == 3:
        
        display.blit(preto, (0, 0))         
        tela_Final.draw(display)

        fontes = pygame.font.SysFont(fonte, 72)
        txtr = fontes.render(f"Pontuação: {pontos}", True, [255, 255, 255])

        if opacidade < 255:
           opacidade += 255 / 60
     
        preto.set_alpha(opacidade) 
        display.blit(txtr, (200, 250))
        
        if againButton.rect.collidepoint(pygame.mouse.get_pos()) and mouseclick:
            vivo = True
            etapa -= 1
            setup()
            
        if Sair.rect.collidepoint(pygame.mouse.get_pos()) and mouseclick:
            gameLoop=False
    
    pygame.display.update()  # Update the screen
pygame.quit()
