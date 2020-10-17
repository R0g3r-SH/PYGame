from Extra import *

"""
import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum
import os
"""


#Bucle principal del juego.
def main():
    global running
    path = os.path.abspath("..\Resources")
    pygame.init()
    pygame.mixer.init(frequency=44100)

    #Lee el OST
    pygame.mixer.music.load(path + "\OST.mp3")

    #Comienza a reproducirlo
    pygame.mixer.music.play(-1)
    #Lee el logo del tec, lo reescala y define su futura posición
    logoDelTec = pygame.image.load(path + "\logotec2019.png")
    logoDelTec = pygame.transform.scale(logoDelTec, (250, 100))
    tecX = 0
    tecY = 0

    screen = pygame.display.set_mode((800, 600))
    #screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    #Define el nombre de la ventana y el logo
    pygame.display.set_caption("Proyecto")
    icon = pygame.image.load(path + "\matematicas.png")
    pygame.display.set_icon(icon)

    #Define alguna constantes de colroes
    BG = (0, 0, 0)
    #WHITE = (255, 255, 255)
    
    YELLOW_INACTIVE = (230, 234, 112)
    YELLOW_ACTIVE = (243, 250, 3)
    BLUE_INACTIVE = pygame.Color('lightskyblue3')
    BLUE_ACTIVE = pygame.Color('dodgerblue2')
    RED_INACTIVE = (246, 105, 105)
    RED_ACTIVE = (255, 12, 12)
    GREEN_INACTIVE = (123, 255, 91)
    GREEN_ACTIVE = (38, 190, 1)

    juego_de_dados = UIElement(
        center_position=(400, 250),
        font_size=30,
        bg_rgb=BG,
        inactive_rgb= BLUE_INACTIVE,
        active_rgb= BLUE_ACTIVE,
        text="Juego de dados",
    )

    juego_matematicas = UIElement(
        center_position=(400, 300),
        font_size = 30,
        bg_rgb = BG,
        inactive_rgb=YELLOW_INACTIVE,
        active_rgb = YELLOW_ACTIVE,
        text="Juego de sumas",
        )

    juego_extra = UIElement(
        center_position=(400, 350),
        font_size=30,
        bg_rgb=BG,
        inactive_rgb=GREEN_INACTIVE,
        active_rgb=GREEN_ACTIVE,
        text="Juego extra",
        action = "extra_main()" 
    )

    quit_btn = UIElement(
        center_position=(400, 400),
        font_size=30,
        bg_rgb=BG,
        inactive_rgb=RED_INACTIVE,
        active_rgb=RED_ACTIVE,
        text="Salir",
        #action="exit_main()"
        action="xd()"
    )

    while running.running:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            if event.type == pygame.QUIT:
                end_main(running)

        screen.fill(BG)

        #Dibuja en pantalla el logo
        screen.blit(logoDelTec, (tecX, tecY))

        quit_btn.update(pygame.mouse.get_pos(), mouse_up)
        #ui_action = quit_btn.update(pygame.mouse.get_pos(), mouse_up)
        #if ui_action is not None:
        #    return
        quit_btn.draw(screen)

        juego_de_dados.update(pygame.mouse.get_pos(), mouse_up)
        juego_de_dados.draw(screen)

        juego_extra.update(pygame.mouse.get_pos(), mouse_up)
        juego_extra.draw(screen)

        juego_matematicas.update(pygame.mouse.get_pos(), mouse_up)
        juego_matematicas.draw(screen)

        pygame.display.flip()

if __name__ == '__main__':
    main()
