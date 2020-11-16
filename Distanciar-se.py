import pygame
from pygame.locals import*
import sys
import os
import random
from pygame import mixer
import math
import time

font_name = pygame.font.match_font('arial')
W, H = 640, 480
HW, HH = W / 2, H/2
AREA = W * H
YELLOW = (255,255,0)
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
clock = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("Distanciar-se")
FPS = 120

background = pygame.image.load("bg.png").convert()
IMGMenu = pygame.image.load("Menu.png").convert()
fase1 = pygame.image.load("fase1.png").convert()
fase2 = pygame.image.load("fase2.png").convert()
fasefinal = pygame.image.load("fasefinal.png").convert()
gameover = pygame.image.load("gameover.png").convert()
vcganhou = pygame.image.load("vcganhou.png").convert()
IMGmanual = pygame.image.load("manual.png")
IMGpersonagem = pygame.image.load("pers.png")
IMGaglomeracao = pygame.image.load("aglomeracao.png")
IMGaglomeracao2 = pygame.image.load("aglomeracao2.png")
IMGaglomeracao3 = pygame.image.load("aglomeracao3.png")
IMGmascara = pygame.image.load("mascara.png")
IMGalcool = pygame.image.load("alcool.png")

vidaSound =  mixer.Sound('vidaPlus.wav')
invencibilitySound = mixer.Sound('invencibilitySound.wav')
danoSound = mixer.Sound('dano.wav')
numFase = 1


class Personagem:
    def __init__(self):
        self.img = IMGpersonagem
        self.vidas = 0
        self.y = 385
        self.x = 303
        self.invencibilidade = False
        self.alive = True
        self.vidas = 3

class Aglomeracao:
    def __init__(self,x,img):
        self.img = img
        self.x = x
        self.y = -200
        self.out = False
        self.contato = False

class Mascara:
    def __init__(self,x,img):
        self.img = img
        self.x = x
        self.y = -200
        self.out = False
        self.contato = False

class Alcool:
    def __init__(self,x,img):
        self.img = img
        self.x = x
        self.y = -200
        self.out = False
        self.contato = False


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name,size)
    text_surface = font.render(text, True, YELLOW)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def transicaoTela(texto):
    if texto == "Fase 1":
        DS.blit(fase1,(0, 0))
    elif texto == "Fase 2":
        DS.blit(fase2,(0, 0))
    elif texto == "Fase Final":
        DS.blit(fasefinal,(0, 0))
    elif texto == "Game Over!":
        DS.blit(gameover,(0, 0))
    else:
        DS.blit(vcganhou, (0, 0))

def manual():
    DS.blit(IMGmanual, (0,0))
    button_3 = pygame.Rect(530, 250, 170, 60)
    pygame.draw.rect(DS, (255, 0, 0), button_3)
    click = False
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True

        mx, my = pygame.mouse.get_pos()
        if button_3.collidepoint((mx, my)):
            if click:
                main_menu()

    pygame.display.update()



def main_menu():

    while True:
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        DS.blit(IMGMenu, (0,0))
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(125, 250, 170, 60)

        button_2 = pygame.Rect(330, 250, 170, 60)

        if button_1.collidepoint((mx, my)):
            if click:
                personagem.vidas = 3
                fase(4, 0, "Fase 1") #fase 1
        if button_2.collidepoint((mx, my)):
            if click:
                DS.blit(IMGmascara, (0,0))
                clock.tick(FPS)

        pygame.display.update()


def fase(velocidadeJogo,qtdObstaculoAleatoria,textoFase):

    global numFase, textoInvencibilidade
    tempoTexto = 0
    obst = [IMGaglomeracao, IMGaglomeracao2, IMGaglomeracao3]
    itens = [IMGmascara, IMGalcool]
    position_AUX_ANT = random.randint(105,425)
    obstaculos = []


    tempoInvencibilidade = 0
    y = 0
    end = False
    tempoJogo = 0

    personagem.y = 385
    velocidadeNivel = 0
    if velocidadeJogo == 4:
        velocidadeNivel = 208
    elif velocidadeJogo == 6:
        velocidadeNivel = 258

    while tempoTexto < 500:
        transicaoTela(textoFase)
        tempoTexto+=4
        pygame.display.update()
        clock.tick(FPS)

    while tempoJogo < 14000:
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                exit()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and personagem.x > 110:
            personagem.x -= 7
        if pressed[pygame.K_RIGHT] and personagem.x < 490:
            personagem.x += 7

        rel_y = y % background.get_rect().height
        DS.blit(background, (0, rel_y - background.get_rect().height))
        if rel_y < H:
            DS.blit(background, (0, rel_y))
        y += velocidadeJogo
        tempoJogo+=4

        if tempoInvencibilidade != 0:
            tempoInvencibilidade -= 1
        if tempoInvencibilidade == 0:
            personagem.invencibilidade = False


        if tempoJogo < 300:
            DS.blit(IMGpersonagem, (personagem.x, personagem.y))
        elif tempoJogo < 10000:

            if qtdObstaculoAleatoria == 0:
                qtdObstaculo = random.randint(1, 2)
            else:
                qtdObstaculo = 2

            for l in range(qtdObstaculo):
                if y % (velocidadeNivel)== 0:
                    position_AUX = random.randint(105, 425)
                    dif = math.fabs(position_AUX - position_AUX_ANT)
                    while dif < 130:
                        position_AUX = random.randint(105, 425)
                        dif = math.fabs(position_AUX - position_AUX_ANT)
                    position_AUX_ANT = position_AUX

                    sortear = random.randint(0, 101)
                    if sortear > 3:
                        next = random.choice(obst)
                    else:
                        next = random.choice(itens)
                    if next == IMGaglomeracao or next == IMGaglomeracao2 or next == IMGaglomeracao3:
                        obstaculos.append(Aglomeracao(position_AUX, next))
                    if next == IMGmascara:
                        obstaculos.append(Mascara(position_AUX, next))
                    if next == IMGalcool:
                        obstaculos.append(Alcool(position_AUX, next))
        elif tempoJogo > 10000 and tempoJogo < 11000:
            DS.blit(IMGpersonagem, (personagem.x, personagem.y))
        elif tempoJogo > 11000 and tempoJogo < 11400:
            end = True
            DS.blit(IMGpersonagem, (personagem.x, personagem.y))
        else:
            if personagem.y > -40:
                if velocidadeJogo == 4:
                    personagem.y -= 2
                else:
                    personagem.y -= 3
                DS.blit(IMGpersonagem, (personagem.x, personagem.y))
            else:
                if numFase == 1:
                    numFase+=1
                    fase(6, 0, "Fase 2")
                elif numFase == 2:
                    numFase+=1
                    fase(6, 1, "Fase Final")
                else:
                    tempoTexto = 0
                    while tempoTexto < 500:
                        transicaoTela(vcganhou)
                        tempoTexto += 4
                        pygame.display.update()
                        clock.tick(FPS)
                    main_menu()


        if end == False:
            for l in range(obstaculos.__len__()):
                DS.blit(obstaculos[l].img, (obstaculos[l].x, obstaculos[l].y))
                obstaculos[l].y += velocidadeJogo
                if obstaculos[l].y > 480:
                    obstaculos[l].out = True

            DS.blit(IMGpersonagem, (personagem.x, personagem.y))

            for l in range(obstaculos.__len__()):
                if (385 + 10 >= obstaculos[l].y and 385 - 10 <= obstaculos[l].y + 70) and (
                        personagem.x + 10 >= obstaculos[l].x - 10 and personagem.x - 10 <= obstaculos[l].x + 70) and obstaculos[l].out == False:
                    if isinstance(obstaculos[l], Mascara) and obstaculos[l].contato == False:
                        obstaculos[l].contato = True
                        personagem.invencibilidade = True
                        tempoInvencibilidade = 500
                        invencibilitySound.stop()
                        invencibilitySound.play(0)
                    elif isinstance(obstaculos[l], Alcool) and obstaculos[l].contato == False:
                        obstaculos[l].contato = True
                        personagem.vidas += 1
                        vidaSound.play(0)
                    elif personagem.invencibilidade == False and personagem.vidas == 0 and obstaculos[l].contato == False:
                        tempoTexto = 0
                        while tempoTexto < 500:
                            transicaoTela("Game Over!")
                            tempoTexto += 4
                            pygame.display.update()
                            clock.tick(FPS)
                        numFase = 1
                        main_menu()
                    elif personagem.invencibilidade == False and personagem.vidas >= 1 and obstaculos[l].contato == False:
                        obstaculos[l].contato = True
                        danoSound.play(0)
                        personagem.vidas -= 1

            textoVidas = 'Vidas: {0}'.format(personagem.vidas)
            draw_text(DS, str(textoVidas), 25, 42, 10)
            if tempoInvencibilidade > 100:
                textoInvencibilidade = "Tempo de Invencibilidade restante: 1"
            if tempoInvencibilidade > 200:
                textoInvencibilidade = "Tempo de Invencibilidade restante: 2"
            if tempoInvencibilidade > 300:
                textoInvencibilidade = "Tempo de Invencibilidade restante: 3"
            if tempoInvencibilidade > 400:
                textoInvencibilidade = "Tempo de Invencibilidade restante: 4"
            if personagem.invencibilidade == True:
                draw_text(DS, str(textoInvencibilidade), 25, 168, 40)

        pygame.display.update()
        clock.tick(FPS)

personagem = Personagem()
while True:

    main_menu()





