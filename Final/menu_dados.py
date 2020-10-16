import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum
import os
import random

from main import running, UIElement, InputBox


def print_names(player1 = "HOLA",player2 = "QUETAL"):
    print (f'Player 1: {player1}')
    print(f'Player 2: {player2}')

def end_menu_dados(running):
    running.menu_dados = False

def main_menu_dados():
    global running

    path = os.path.abspath("..\Resources")
    pygame.init()
    pygame.mixer.init(frequency=44100)

    #Lee el OST
    pygame.mixer.music.load(path + "\OST.mp3")

    #Comienza a reproducirlo
    pygame.mixer.music.play(-1)

    screen = pygame.display.set_mode((800, 600))
    #screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    #Define el nombre de la ventana y el logo
    pygame.display.set_caption("Proyecto")
    icon = pygame.image.load(path + "\matematicas.png")
    pygame.display.set_icon(icon)

    #Define alguna constantes de colroes
    BG = (0, 0, 0)
    #WHITE = (255, 255, 255)

    logoDados = pygame.image.load(path + "\dados.png")
    logoDados = pygame.transform.scale(logoDados, (100, 100))
    dadoX = 335
    dadoY = 40

    BLUE_INACTIVE = pygame.Color('lightskyblue3')
    BLUE_ACTIVE = pygame.Color('dodgerblue2')

    player_1 = InputBox(180, 280, 170, 25, "Nombre Jugador 1", 
                        BLUE_ACTIVE, BLUE_INACTIVE, FONT=pygame.font.Font(None, 25))

    player_2 = InputBox(450, 280, 170, 25, "Nombre Jugador 2", 
                        BLUE_ACTIVE, BLUE_INACTIVE, FONT=pygame.font.Font(None, 25))

    quien_empieza = UIElement(
        center_position=(400, 380),
        font_size=25,
        bg_rgb=BG,
        inactive_rgb=BLUE_INACTIVE,
        active_rgb=BLUE_ACTIVE,
        text="Elije el jugador que tirará primero:",
    )
    nombres = UIElement(
        center_position=(400, 200),
        font_size=25,
        bg_rgb=BG,
        inactive_rgb=BLUE_INACTIVE,
        active_rgb=BLUE_ACTIVE,
        text="Ingresa el nombre de los jugadores:",
    )

    jugador1 = UIElement(
        center_position=(250, 460),
        font_size=25,
        bg_rgb=BG,
        inactive_rgb=BLUE_INACTIVE,
        active_rgb=BLUE_ACTIVE,
        text="Jugador 1",
        action = "print_names()"
    )

    jugador2 = UIElement(
        center_position=(550, 460),
        font_size=25,
        bg_rgb=BG,
        inactive_rgb=BLUE_INACTIVE,
        active_rgb=BLUE_ACTIVE,
        text="Jugador 2",
        action="print_names(player_2.var,player_1.var)"
    )



    while running.menu_dados:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            if event.type == pygame.QUIT:
                end_menu_dados(running)
                return
            player_1.handle_event(event)
            player_2.handle_event(event)

        

        screen.fill(BG)

        screen.blit(logoDados, (dadoX, dadoY))

        player_1.update()
        player_1.draw(screen)

        player_2.update()
        player_2.draw(screen)

        quien_empieza.draw(screen)
        nombres.draw(screen)

        jugador1.update(pygame.mouse.get_pos(), mouse_up)
        jugador1.draw(screen)

        jugador2.update(pygame.mouse.get_pos(), mouse_up)
        jugador2.draw(screen)

        pygame.display.flip()

main_menu_dados()
