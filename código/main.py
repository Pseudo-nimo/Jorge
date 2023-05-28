import random
import sys
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
running = True
pulo = True
etapa = 1


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
inicio.rect.center = (screen[0]/2,screen[1]/2)
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


# personagem
guy = pygame.sprite.Sprite()
guy.image = pygame.image.load(parede.pasta+"ave.png")  # qual imagem

guy.rect = guy.image.get_rect()

# canos

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
# preto.rect = pygame.Rect([0, 0, 1000, 800])

# gameover images


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
    cano1.rect.left = 800
    cano3.rect.left = 1300
    guy.rect.centerx = fase.rect.centerx

comeco.add(tela)
comeco.add(inicio)

tela_Final.add(botao_Tentar)
tela_Final.add(Sair)
persona.add(guy)
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



while running:
    if True:
        

        #keys = pygame.key.get_pressed()
        # boolean
        if etapa == 1:
            comeco.draw(display)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if inicio.rect.collidepoint(pygame.mouse.get_pos()):
                        vivo = True
                        etapa += 1
                if event.type == pygame.QUIT:
                    pygame.quit()
                    
            pygame.display.update()

        if etapa == 2:

            for event in pygame.event.get():
                if vivo:
                    # pular
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        Jump = 0

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            Jump = 0
                    if event.type == pygame.QUIT:
                        sys.exit()
                # fechar

            clock.tick(60)
            # morrer
            if guy.rect.top < -1:
                guy.rect.top = 0
                vivo = False
            if guy.rect.bottom > 558:
                guy.rect.bottom = 558

                # guy.rect.bottom += jump_Speed
                # pygame.time.wait(1000)
                etapa += 1
            if ((guy.rect.colliderect(cano1.rect)) or (guy.rect.colliderect(cano3.rect)) or (
                    guy.rect.colliderect(cano2.rect)) or (guy.rect.colliderect(cano4.rect))):
                vivo = False
                # a

            
            # manutencao

            grupo.draw(display)
            persona.draw(display)
            colisors.draw(display)
            txt = f"Pontuação: {pontos}"
            txttela = fontesys.render(txt, True, (0, 0, 0))
            display.blit(txttela, (50, 500))

            if not vivo:
                Jump = 39
            if Jump < 15:
                guy.rect.centery -= jump_Speed
                guy.image = pygame.transform.rotate(guy.image, 0.5)
            elif Jump < 17:
                # a
                guy.rect.centery = guy.rect.centery
            elif Jump > 16:
                # a
                guy.rect.centery += jump_Speed

            # cano

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
                # if pisu[0].rect.x:# .rect.x=-10
            if vivo:
                cano1.rect.left -= speed
                cano3.rect.left -= speed
                pisu[0].rect.x -= speed
                pisu[1].rect.x -= speed
                if Jump < 40:
                    Jump += 1
            pygame.display.update()
        # gameover
        if etapa == 3:
            opacidade = 0

            tela_Final.draw(display)
            # Set the image"s alpha value

            fontes = pygame.font.SysFont(fonte, 72)
            txtr = fontes.render(f"Pontuação: {pontos}", True, [255, 255, 255])

            if opacidade < 255:
                # a
                opacidade += 255 / 60  # Change the transparency variable
            preto.set_alpha(opacidade)  # Set the image"s alpha value
            display.blit(preto, (0, 0))  # Display the image
            display.blit(txtr, (200, 250))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameLoop = False
                    running = False
                    print(f"{running}")

                    sys.exit()

                    # ir de novo
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_Tentar.rect.collidepoint(pygame.mouse.get_pos()):
                        vivo = True
                        etapa -= 1

                        pontos = 0
                        guy.rect.centery = 300
                        cano1.rect.left = 800
                        cano3.rect.left = 1300

                    if Sair.rect.collidepoint(pygame.mouse.get_pos()):
                        sys.exit()
            pygame.display.update()  # Update the screen
            clock.tick(60)

