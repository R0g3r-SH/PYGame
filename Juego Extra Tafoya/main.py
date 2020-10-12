import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum

pygame.init()
screen = pygame.display.set_mode((800, 600))
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)


class InputBox:

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
            else:
                self.active = False
            # Cambia el color de la caja para avisarle al ususario que si esta interactuando con el objeto.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Renderiza el texto (lo actualiza).
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Ajusta el tamaño de la caja al texto.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Dibuja el texto.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Dibuja el rectangulo.
        pygame.draw.rect(screen, self.color, self.rect, 2)
        
def main():
    
    clock = pygame.time.Clock()
    input_box1 = InputBox(100, 100, 140, 32)
    input_box2 = InputBox(100, 300, 140, 32)
    input_boxes = [input_box1, input_box2]
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.update()

        screen.fill((30, 30, 30))
        for box in input_boxes:
            box.draw(screen)

        pygame.display.flip()
        clock.tick(30)

if __name__ == '__main__':
    main()
    pygame.quit()
