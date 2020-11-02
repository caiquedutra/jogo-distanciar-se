import pygame
from pygame.locals import*
import sys
import os
import random

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


W, H = 640, 480
HW, HH = W / 2, H/2
AREA = W * H

font_name = pygame.font.match_font('arial')

YELLOW = (255,255,0)

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name,size)
    text_surface = font.render(text, True, YELLOW)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
clock = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("Distanciar-se")
FPS = 120

background = pygame.image.load("bg.png").convert()
IMGpersonagem = pygame.image.load("pers.jpg").convert()
IMGaglomeracao = pygame.image.load("aglomeracao.png")
IMGaglomeracao2 = pygame.image.load("aglomeracao2.png")
IMGaglomeracao3 = pygame.image.load("aglomeracao3.png")
IMGmascara = pygame.image.load("mascara.png")
IMGalcool = pygame.image.load("alcool.png")
y = 0

position = [105, 275, 435]
obst = [IMGaglomeracao,IMGaglomeracao2,IMGaglomeracao3]
itens = [IMGmascara,IMGalcool]

obstaculos=[]

gerado = False

position_AUX = 0
position_AUX_ANT = 1

personagem = Personagem()
tempoInvencibilidade = 0


while True:

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            exit()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT] and personagem.x > 110:
        personagem.x -= 5
    if pressed[pygame.K_RIGHT] and personagem.x < 490:
        personagem.x += 5

    rel_y = y % background.get_rect().height
    DS.blit(background, (0, rel_y - background.get_rect().height))
    if rel_y < H:
        DS.blit(background, (0,rel_y))
    y+=3

    if tempoInvencibilidade != 0:
        tempoInvencibilidade-= 1
    if tempoInvencibilidade == 0:
        personagem.invencibilidade = False

    if y % 153 == 0:
        position_AUX = random.choice(position)
        while position_AUX == position_AUX_ANT:
            position_AUX = random.choice(position)
        position_AUX_ANT = position_AUX
        sortear = random.randint(0,101)
        if sortear > 8:
            next = random.choice(obst)
        else:
            next = random.choice(itens)
        if next == IMGaglomeracao or next == IMGaglomeracao2 or next ==IMGaglomeracao3:
            obstaculos.append(Aglomeracao(position_AUX_ANT, next))
        if next == IMGmascara:
            obstaculos.append(Mascara(position_AUX_ANT, next))
        if next == IMGalcool:
            obstaculos.append(Alcool(position_AUX_ANT, next))
    for l in range(obstaculos.__len__()):
        DS.blit(obstaculos[l].img,(obstaculos[l].x, obstaculos[l].y))
        obstaculos[l].y+=3
        if obstaculos[l].y > 480:
            obstaculos[l].out = True

    DS.blit(IMGpersonagem, (personagem.x, personagem.y))


    for l in range(obstaculos.__len__()):
        if (385 + 10 >= obstaculos[l].y  and 385 - 10 <= obstaculos[l].y + 70) and (personagem.x + 10 >= obstaculos[l].x  and personagem.x - 10 <= obstaculos[l].x+70) and obstaculos[l].out == False:
            if isinstance(obstaculos[l],Mascara) and obstaculos[l].contato == False:
                print("mascara")
                obstaculos[l].contato = True
                personagem.invencibilidade = True
                tempoInvencibilidade = 500
            elif isinstance(obstaculos[l],Alcool) and obstaculos[l].contato == False:
                print("alcool")
                obstaculos[l].contato = True
                personagem.vidas+=1
            elif personagem.invencibilidade == False and personagem.vidas == 0 and obstaculos[l].contato == False:
                sys.exit(1)
            elif personagem.invencibilidade == False and personagem.vidas >= 1 and obstaculos[l].contato == False:
                obstaculos[l].contato = True
                personagem.vidas-=1

    draw_text(DS, str(personagem.vidas), 25, 10, 10)
    if tempoInvencibilidade > 100:
        text = "Tempo de Invencibilidade restante: 1"
    if tempoInvencibilidade > 200:
        text = "Tempo de Invencibilidade restante: 2"
    if tempoInvencibilidade > 300:
        text = "Tempo de Invencibilidade restante: 3"
    if tempoInvencibilidade > 400:
        text = "Tempo de Invencibilidade restante: 4"
    if personagem.invencibilidade == True:
        draw_text(DS, str(text), 25, 168, 40)

    pygame.display.update()
    clock.tick(FPS)
