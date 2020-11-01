import pygame
from pygame.locals import*
import sys
import os
import random


class Obstaculo:
    def __init__(self,x):
        self.x = x
        self.y = -50
        self.out = False

W, H = 640, 480
HW, HH = W / 2, H/2
AREA = W * H



pygame.init()
clock = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("Distanciar-se")
FPS = 120

background = pygame.image.load("bg.png").convert()
personagem = pygame.image.load("pers.jpg").convert()
y = 0
posicaoPersonagem = 300
position = [150, 300, 450]

obstaculos=[]

gerado = False
while True:



    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            exit()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT] and posicaoPersonagem > 150:
        posicaoPersonagem -= 5
    if pressed[pygame.K_RIGHT] and posicaoPersonagem < 450:
        posicaoPersonagem += 5

    rel_y = y % background.get_rect().height
    DS.blit(background, (0, rel_y - background.get_rect().height))
    if rel_y < H:
        DS.blit(background, (0,rel_y))
    y+=3


    if y % 90 == 0:
        obstaculos.append(Obstaculo(random.choice(position)))
    for l in range(obstaculos.__len__()):
        DS.blit(personagem,(obstaculos[l].x, obstaculos[l].y))
        obstaculos[l].y+=3
        if obstaculos[l].y > 480:
            obstaculos[l].out = True

    DS.blit(personagem, (posicaoPersonagem, 360))

    for l in range(obstaculos.__len__()):
        if (360 + 10 >= obstaculos[l].y - 5 and 360 - 10 <= obstaculos[l].y + 5) and (posicaoPersonagem + 10 >= obstaculos[l].x - 5 and posicaoPersonagem - 10 <= obstaculos[l].x + 10) and obstaculos[l].out == False:
            sys.exit(1)

    pygame.display.update()
    clock.tick(FPS)
