import pygame
from pygame.locals import*
import sys
import os
import random



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
y = 800
posicaoPersonagem = 300
position = [150, 300, 450]
obstaculosGerados = False

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



    DS.blit(personagem, (posicaoPersonagem, 360))

    if obstaculosGerados == False:
        for l in range(0,2100,100):
            background.blit(personagem, (random.choice(position), l))
            print(random.choice(position))
            obstaculosGerados = True


    pygame.display.update()
    clock.tick(FPS)
