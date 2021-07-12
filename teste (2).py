import random
import sys
import pygame as pygame
import ctypes

myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
vivo = False
jump_Speed = 8
clock = pygame.time.Clock()
Jump = 39  # final
pontos = 0
lim_y = -314
lin_y = -100
running = True
pulo = True
etapa = 1
# criando janela e iniciando
pygame.init()
display = pygame.display.set_mode([800, 600])
icone = pygame.image.load("ave.png")
pygame.display.set_icon(icone)
pygame.display.set_caption("Jorge")

# inicio
tela = pygame.sprite.Sprite()
tela.image = pygame.image.load("noite2.jpg")
tela.rect = pygame.Rect([0, 0, 800, 600])

inicio = pygame.sprite.Sprite()
inicio.image = pygame.image.load("BOTAO.png")
inicio.rect = pygame.Rect([0, 0, 200, 150])
inicio.rect.center = tela.rect.center
# scenery
fase = pygame.sprite.Sprite()
fase.image = pygame.image.load("noite.jpg")
fase.rect = fase.image.get_rect()

piso1 = pygame.sprite.Sprite()
piso1.image = pygame.image.load("piso.jpg")  # qual imagem
piso1.rect = pygame.Rect([0, 550, 3000, 50])  # x,y, tamanho_x(l), tamanho_y(h)

piso2 = pygame.sprite.Sprite()
piso2.image = pygame.image.load("piso.jpg")  # qual imagem
piso2.rect = pygame.Rect([2400, 550, 3000, 50])  # x,y, tamanho_x(l), tamanho_y(h)

# personagem
guy = pygame.sprite.Sprite()
guy.image = pygame.image.load("ave.png")  # qual imagem
# guy.image = pygame.transform.scale(guy.image, [60, 49])
guy.rect = pygame.Rect([400, 200, 50, 50])  # x,y, tamanho_x(l), tamanho_y(h)

# canos
cano1 = pygame.sprite.Sprite()
cano1.image = pygame.image.load("canos_a.png")
# cano1.image = pygame.transform.scale(cano1.image, [118,393])
cano1.rect = pygame.Rect([700, 0, 118, 393])
cano1.rect.top = random.randint(lim_y, lin_y)

cano2 = pygame.sprite.Sprite()
cano2.image = pygame.image.load("canos_b.png")
# cano2.image = pygame.transform.scale(cano2.image, [118,393])
cano2.rect = pygame.Rect([700, 0, 118, 393])
cano2.rect.top = (cano1.rect.bottom + 200)
cano2.rect.centerx = cano1.rect.centerx

cano3 = pygame.sprite.Sprite()
cano3.image = pygame.image.load("canos_a.png")
# cano1.image = pygame.transform.scale(cano1.image, [118,393])
cano3.rect = pygame.Rect([1100, 0, 118, 393])
cano3.rect.top = random.randint(lim_y, lin_y)

cano4 = pygame.sprite.Sprite()
cano4.image = pygame.image.load("canos_b.png")
# cano2.image = pygame.transform.scale(cano2.image, [118,393])
cano4.rect = pygame.Rect([1100, 0, 118, 393])
cano4.rect.top = (cano3.rect.bottom + 200)
cano4.rect.centerx = cano3.rect.centerx

# preto = pygame.sprite.Sprite()
preto = pygame.image.load("preto.png").convert()
# preto.rect = pygame.Rect([0, 0, 1000, 800])

# gameover images


botao_Tentar = pygame.sprite.Sprite()
botao_Tentar.image = pygame.image.load("Tentar novamente.png")
botao_Tentar.rect = pygame.Rect(0, 0, 200, 109)
botao_Tentar.rect.centerx = 550
botao_Tentar.rect.bottom = 450

Sair = pygame.sprite.Sprite()
Sair.image = pygame.image.load("Sair.png")
Sair.rect = pygame.Rect(0, 0, 200, 109)
Sair.rect.bottom = 450
Sair.rect.centerx = 250

# grupo
comeco = pygame.sprite.Group()
persona = pygame.sprite.Group()
grupo = pygame.sprite.Group()
tela_Final = pygame.sprite.Group()
comeco.add(tela)
comeco.add(inicio)
# tela_Final.add(gameover)
tela_Final.add(botao_Tentar)
tela_Final.add(Sair)
persona.add(guy)
grupo.add(fase)
grupo.add(cano1)
grupo.add(cano2)
grupo.add(cano3)
grupo.add(cano4)
grupo.add(piso1)
grupo.add(piso2)

# musica
pygame.mixer.music.load("Musica fofa.mp3")
pygame.mixer.music.play(0)

# fonte
pygame.font.init()
fonte = pygame.font.get_default_font()
fontesys = pygame.font.SysFont(fonte, 30)

# jogo

while running:
    if __name__ == "__main__":
        cano1.rect.left = 800
        cano3.rect.left = 1300
        guy.rect.centerx = fase.rect.centerx

        keys = pygame.key.get_pressed()  # boolean
        while etapa == 1:
            comeco.draw(display)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if inicio.rect.collidepoint(pygame.mouse.get_pos()):
                        vivo = True
                        etapa += 1
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

        while etapa == 2:

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

            # pontuacao
            txt = f"Pontuação: {pontos}"

            # manutencao

            grupo.draw(display)
            persona.draw(display)
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
                cano1.rect.top = random.randint(lim_y, lin_y)

                cano2.rect.top = (cano1.rect.bottom + 200)
            if cano3.rect.right < 0:
                cano3.rect.left = 850
                cano3.rect.top = random.randint(lim_y, lin_y)

                cano4.rect.top = (cano3.rect.bottom + 200)
            if piso2.rect.x < (-1000):
                piso2.rect.x = -100
                # if piso1.rect.x:# .rect.x=-10
            if cano3.rect.centerx == fase.rect.centerx:
                pontos += 1
            if cano1.rect.centerx == fase.rect.centerx:
                pontos += 1
            if vivo:
                cano1.rect.left -= 4
                cano3.rect.left -= 4
                piso1.rect.x -= 4
                piso2.rect.x -= 4
                if Jump < 40:
                    Jump += 1
            pygame.display.update()
        # gameover
        while etapa == 3:
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

if not running:
    pygame.quit()
    exit()
