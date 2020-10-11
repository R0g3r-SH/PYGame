import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum
import random 

def main():
    numero_a_adivinar = random.randint(1,25)
    pygame.init()

    screen = pygame.display.set_mode((800, 600))

    pygame.display.set_caption("\Proyecto")
    icon = pygame.image.load("matematicas.png")
    pygame.display.set_icon(icon)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            if event.type == pygame.QUIT:
                running = False

main()