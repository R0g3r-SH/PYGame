
import pygame
import sys
pygame.init()
pygame.display.set_mode((900, 500 ) )


while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)