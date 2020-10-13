import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum
import os
import random

num_to_guess = random.randint(1,25)
intentos = 3

pygame.init()
screen = pygame.display.set_mode((800, 600))

FONT = pygame.font.Font(None, 32)
path = os.path.abspath("..\Resources")
pygame.init()

screen = pygame.display.set_mode((800, 600))

#Define el nombre de la ventana y el logo
pygame.display.set_caption("Juego Extra")
icon = pygame.image.load(path + "\matematicas.png")
pygame.display.set_icon(icon)

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
BG = (30, 30, 30)


class Label():

    def __init__(self, txt, location, size=(160, 30), bg=BG, fg=COLOR_INACTIVE, font_name="Segoe Print", font_size=20):
        """
            Args:
            txt = string 
            location = tuple
            size= tuple
            bg= rgb
            fg= rgb
            font_name= string 
            font_size= int
        """
        self.bg = BG
        self.fg = fg
        self.size = size

        self.font = pygame.freetype.SysFont(font_name, font_size, bold=True)
        self.txt = txt
        self.txt_surf, _= self.font.render(text=self.txt, fgcolor=self.fg, bgcolor=self.bg)
        self.txt_rect = self.txt_surf.get_rect(center=[s//2 for s in self.size])

        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(topleft=location)

    def update(self):
        """ 
            Actualiza el sprite.
        """
        self.surface.fill(self.bg)
        self.txt_surf, _= self.font.render(text=self.txt, fgcolor=self.fg, bgcolor=self.bg)
        self.surface.blit(self.txt_surf, self.txt_rect)

    def draw(self, screen):
        """ Dibuja un elemento sobre la superficie."""
        screen.blit(self.surface, self.rect)

class InputBox():

    def __init__(self, x, y, w, h, text=''):
        """ 
        args
        x, y, anchura, altura, texto de default
        """
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Si el usuario hizo click en la caja de texto.
            if self.rect.collidepoint(event.pos):
                # Activa la variable de que esta siendo seleccionado.
                self.active = not self.active
                if self.text == "Ingresa tu intento aquí.":
                    self.text = ''
            else:
                self.active = False
            # Cambia el color de la caja para avisarle al ususario que si esta interactuando con el objeto.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:

                if event.key == pygame.K_RETURN:
                    try:
                        guess = int(self.text)
                    except:
                        print("Eso no es un número.")
                    take_a_guess(guess)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    #Se asegura que no se salga del rectangulo
                    if self.txt_surface.get_width() < 255:
                        self.text += event.unicode
                # Renderiza el texto (lo actualiza).
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Ajusta el tamaño de la caja al texto.
        width = max(255, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Dibuja el texto.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Dibuja el rectangulo.
        pygame.draw.rect(screen, self.color, self.rect, 2)
        

def take_a_guess(guess):
    global num_to_guess
    global intentos
    if guess == num_to_guess:
        print("¡Lo adivinaste! ¡Guau!")
    elif guess < num_to_guess:
        print("Muy bajo. Vuelve a intentarlo.")
        intentos -= 1
        print("Intentos:", intentos)
    else:
        print("Muy alto. Vuelve a intentarlo.")
        intentos -= 1
        print("Intentos:", intentos)

def main():
    global intentos
    clock = pygame.time.Clock()
    input_box = InputBox(275, 300, 140, 32, "Ingresa tu intento aquí.")
    done = False

    state1= Label(
        txt= 'Estoy pensando en un numero entre 1 y 25.',
        location=(150, 150),
        size= (500,30),
    )
    state2= Label(
        txt= f'Tienes {intentos} intentos para adivinarlo.',
        location=(200, 200),
        size=(400, 30),
    )

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            input_box.handle_event(event)

        screen.fill((30, 30, 30))
        
        input_box.update()
        input_box.draw(screen)

        state1.update()
        state1.draw(screen)

        state2.txt = f'Tienes {intentos} intentos para adivinarlo.'
        state2.update()
        state2.draw(screen)

        pygame.display.flip()
        clock.tick(30)

if __name__ == '__main__':
    main()
    pygame.quit()
