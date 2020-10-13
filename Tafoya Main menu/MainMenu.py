import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum
import os

def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    """ Retorna una superficie con texto escrito encima """
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()


class UIElement(Sprite):
    """ Un elemento de interfaz grafica para añadir. """

    def __init__(self, center_position, text, font_size, bg_rgb, inactive_rgb, active_rgb, action=None):
        """
        Args:
            center_position - tuple (x, y)
            text - string
            font_size - int
            bg_rgb (background colour) - tuple (r, g, b)
            inactive_rgb (text colour) - tuple (r, g, b)
            active_rgb (text colour) - tuple (r, g, b)
            action - el estado de cambio asociado a este boton
        """
        self.mouse_over = False

        default_image = create_surface_with_text(
            text=text, font_size=font_size, text_rgb=inactive_rgb, bg_rgb=bg_rgb
        )

        highlighted_image = create_surface_with_text(
            text=text, font_size=font_size * 1.2, text_rgb=active_rgb, bg_rgb=bg_rgb
        )

        self.images = [default_image, highlighted_image]
        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position),
        ]

        # Asignar una accion al boton
        self.action = action

        super().__init__()

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos, mouse_up):
        """ 
            Actualiza la variable mouse_over y retorna la accion del boton al
            hacer click.
        """
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        """ Dibuja un elemento sobre la superficie."""
        surface.blit(self.image, self.rect)

#Bucle principal del juego.
def main():
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
    )

    quit_btn = UIElement(
        center_position=(400, 400),
        font_size=30,
        bg_rgb=BG,
        inactive_rgb=COLOR_INACTIVE,
        active_rgb=COLOR_ACTIVE,
        text="Salir",
        action=GameState.QUIT,
    )

    
    running = True
    while running:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            if event.type == pygame.QUIT:
                running = False

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

class GameState(Enum):
    QUIT = -1

if __name__ == '__main__':
    main()
