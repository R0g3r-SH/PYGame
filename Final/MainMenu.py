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

    BG = (30, 30, 30)
    #WHITE = (255, 255, 255)
    COLOR_INACTIVE = pygame.Color('lightskyblue3')
    COLOR_ACTIVE = pygame.Color('dodgerblue2')
    # create a ui element

    
    juego_de_dados = UIElement(
        center_position=(400, 250),
        font_size=30,
        bg_rgb=BG,
        inactive_rgb=COLOR_INACTIVE,
        active_rgb=COLOR_ACTIVE,
        text="Juego de dados",
    )

    juego_matematicas = UIElement(
        center_position=(400, 300),
        font_size = 30,
        bg_rgb = BG,
        inactive_rgb = COLOR_INACTIVE,
        active_rgb = COLOR_ACTIVE,
        text="Juego de sumas",
        )

    juego_extra = UIElement(
        center_position=(400, 350),
        font_size=30,
        bg_rgb=BG,
        inactive_rgb=COLOR_INACTIVE,
        active_rgb=COLOR_ACTIVE,
        text="Juego extra",
        action = "extra_main()" 
    )

    quit_btn = UIElement(
        center_position=(400, 400),
        font_size=30,
        bg_rgb=BG,
        inactive_rgb=COLOR_INACTIVE,
        active_rgb=COLOR_ACTIVE,
        text="Salir",
        action="end_main(running)"
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

        ui_action = quit_btn.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return
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
