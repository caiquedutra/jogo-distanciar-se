import pygame
from pygame.locals import*
import sys
import os

def events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

W, H = 640, 480
HW, HH = W / 2, H/2
AREA = W * H

pygame.init()
clock = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("Distanciar-se")
FPS = 120

background = pygame.image.load("bg.png").convert()
y = 0
while True:
    events()

    rel_y = y % background.get_rect().height
    DS.blit(background, (0, rel_y - background.get_rect().height))
    if rel_y < H:
        DS.blit(background, (0,rel_y))
    y+=1

    pygame.display.update()
    clock.tick(FPS)
