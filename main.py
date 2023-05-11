import pygame
import os
from sys import exit
from pytmx import load_pygame
import enemies,hero,map

HEIGHT, WIGHT = 400, 800

pygame.init()
screen = pygame.display.set_mode((WIGHT,HEIGHT))
pygame.display.set_caption('pygame project')
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)