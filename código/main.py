import pygame
import parede

screen = [800,600]
pygame.sprite.Sprite().__init__()
vivo = False
speed = 4
pisu = [pygame.sprite.Sprite(), pygame.sprite.Sprite()]
jump_Speed = 5
clock = pygame.time.Clock()
pontos = 0
lim_y = -314
lin_y = -100
gameloop = True
pulo = True
etapa = 1
opacidade = 0.0

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

inicio = pygame.sprite.Sprite()
inicio.image = pygame.image.load(parede.pasta+"BOTAO.png")
inicio.rect = inicio.image.get_rect()
inicio.rect.center = (int(screen[0]/2),int(screen[1]/2))
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
# canos


canoteste = parede.parede()
preto = pygame.image.load(parede.pasta+"preto.png").convert()

botao_Tentar = pygame.sprite.Sprite()
botao_Tentar.image = pygame.image.load(parede.pasta+"Tentar novamente.png")
botao_Tentar.rect = botao_Tentar.image.get_rect()
botao_Tentar.rect.centerx = 550
botao_Tentar.rect.bottom = 450

Sair = pygame.sprite.Sprite()
Sair.image = pygame.image.load(parede.pasta+"Sair.png")
Sair.rect = Sair.image.get_rect()
Sair.rect.bottom = 450
Sair.rect.centerx = 250

def setup():
    canoteste.reinit()
    guy.jumpForce = 90
    guy.gravidade = 0
    guy.rect.centery = 300
    guy.rect.centerx = fase.rect.centerx
    
    
comeco.add(tela)
comeco.add(inicio)

tela_Final.add(botao_Tentar)
tela_Final.add(Sair)

grupo.add(fase)
persona.add(guy)

colisors.add(pisu[0])
colisors.add(pisu[1])
colisors.add(canoteste.canos[0])
colisors.add(canoteste.canos[1])

# musica
pygame.mixer.music.load(parede.pasta+"Musica fofa.mp3")
#pygame.mixer.music.play(0)


setup()
moving = False
space = False
mouseclick = False
fps = 100

while gameloop:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseclick = True
            moving = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouseclick = False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE:
                moving = True
                space = True
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_SPACE:
                space = False
        
          
    if etapa == 1:
        comeco.draw(display)
        if inicio.rect.collidepoint(pygame.mouse.get_pos()) and mouseclick:
            etapa = 2
            vivo = True
            setup()
            
    if etapa == 2:
        guy.fps = fps
        grupo.draw(display)
        persona.draw(display)
        colisors.draw(display)
        txt = f"Pontuação: {pontos}"
        txttela = fontesys.render(txt, True, (0, 0, 0))
        display.blit(txttela, (50, 500))
        
        if moving:
            canoteste.walk()
            pisu[0].rect.x -= speed
            pisu[1].rect.x -= speed
            
            guy.jump()
            if pisu[1].rect.x < (-1000):
                pisu[1].rect.x = -100
        
        if guy.rect.top < -1:
            guy.rect.top = 0
            vivo = False
             
        for batida in pygame.sprite.spritecollide(guy, colisors, False):
            a = 0
            vivo=False
        
        if not vivo:
            etapa=3
        
    
    if etapa == 3:
        
        if opacidade < 255:
            opacidade += 255 / 60
        preto.set_alpha(opacidade)
        fontes = pygame.font.SysFont(fonte, 72)
        txtr = fontes.render(f"Pontuação: {pontos}", True, [255, 255, 255])
        display.blit(preto, (0, 0))  
        display.blit(txtr, (200, 250))
        tela_Final.draw(display)
        if botao_Tentar.rect.collidepoint(pygame.mouse.get_pos()) and mouseclick:
            etapa = 2
            vivo = True
            setup()
        if Sair.rect.collidepoint(pygame.mouse.get_pos()) and mouseclick:
            break

    pygame.display.update()  # Update the screen
pygame.quit()        
