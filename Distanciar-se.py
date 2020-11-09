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

def transicaoTela(fase):
    DS.fill((0, 0, 0))
    textFase = "Fase {0}".format(fase)
    draw_text(DS, str(textFase), 50, 200, 240)


def main_menu():
    while True:

        DS.fill((0, 0, 0))
        draw_text(DS, str("Distanciar-se"), 70, 320, 80)
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(110, 250, 190, 50)

        button_2 = pygame.Rect(350, 250, 190, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                fase(4) #fase 1
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(DS, (255, 0, 0), button_1)
        pygame.draw.rect(DS, (255, 0, 0), button_2)
        draw_text(DS, str("Jogar"), 20, 202, 262)
        draw_text(DS, str("Manual"), 20, 442, 262)

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

        pygame.display.update()


def fase(velocidadeJogo):
    position = [105, 135, 165, 195, 225, 255, 285, 215, 245, 275, 305, 335, 365, 390, 425]
    obst = [IMGaglomeracao, IMGaglomeracao2, IMGaglomeracao3]
    itens = [IMGmascara, IMGalcool]

    obstaculos = []

    gerado = False

    position_AUX = 0
    position_AUX_ANT = 1

    personagem = Personagem()
    tempoInvencibilidade = 0
    y = 0
    end = False

    while y < 14000:
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

        if tempoInvencibilidade != 0:
            tempoInvencibilidade -= 1
        if tempoInvencibilidade == 0:
            personagem.invencibilidade = False


        if y < 300:
            DS.blit(IMGpersonagem, (personagem.x, personagem.y))
        elif y < 10000:
            for l in range(random.randint(1, 2)):
                if y % 200 == 0:
                    position_AUX = random.choice(position)
                    dif = math.fabs(position_AUX - position_AUX_ANT)
                    while dif < 70:
                        position_AUX = random.choice(position)
                        dif = math.fabs(position_AUX - position_AUX_ANT)
                    position_AUX_ANT = position_AUX
                    sortear = random.randint(0, 101)
                    if sortear > 3:
                        next = random.choice(obst)
                    else:
                        next = random.choice(itens)
                    if next == IMGaglomeracao or next == IMGaglomeracao2 or next == IMGaglomeracao3:
                        obstaculos.append(Aglomeracao(position_AUX_ANT, next))
                    if next == IMGmascara:
                        obstaculos.append(Mascara(position_AUX_ANT, next))
                    if next == IMGalcool:
                        obstaculos.append(Alcool(position_AUX_ANT, next))
        elif y > 10000 and y < 10600:
            DS.blit(IMGpersonagem, (personagem.x, personagem.y))
        elif y > 10600 and y < 11200:
            end = True
            DS.blit(IMGpersonagem, (personagem.x, personagem.y))
        else:
            if personagem.y > -20:
                personagem.y -= 2
                DS.blit(IMGpersonagem, (personagem.x, personagem.y))
            else:
                transicaoTela(2)


        if end == False:
            for l in range(obstaculos.__len__()):
                DS.blit(obstaculos[l].img, (obstaculos[l].x, obstaculos[l].y))
                obstaculos[l].y += velocidadeJogo
                if obstaculos[l].y > 480:
                    obstaculos[l].out = True

            DS.blit(IMGpersonagem, (personagem.x, personagem.y))

            for l in range(obstaculos.__len__()):
                if (385 + 10 >= obstaculos[l].y and 385 - 10 <= obstaculos[l].y + 70) and (
                        personagem.x + 10 >= obstaculos[l].x and personagem.x - 10 <= obstaculos[l].x + 70) and obstaculos[l].out == False:
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
                        sys.exit(1)
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




background = pygame.image.load("bg.png").convert()
IMGpersonagem = pygame.image.load("pers.jpg").convert()
IMGaglomeracao = pygame.image.load("aglomeracao.png")
IMGaglomeracao2 = pygame.image.load("aglomeracao2.png")
IMGaglomeracao3 = pygame.image.load("aglomeracao3.png")
IMGmascara = pygame.image.load("mascara.png")
IMGalcool = pygame.image.load("alcool.png")

vidaSound =  mixer.Sound('vidaPlus.wav')
invencibilitySound = mixer.Sound('invencibilitySound.wav')
danoSound = mixer.Sound('dano.wav')


while True:

    main_menu()





