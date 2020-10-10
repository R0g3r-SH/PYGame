import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum


def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    """ Returns surface with text written on """
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()


class UIElement(Sprite):
    """ An user interface element that can be added to a surface """

    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, action=None):
        """
        Args:
            center_position - tuple (x, y)
            text - string of text to write
            font_size - int
            bg_rgb (background colour) - tuple (r, g, b)
            text_rgb (text colour) - tuple (r, g, b)
            action - the gamestate change associated with this button
        """
        self.mouse_over = False

        default_image = create_surface_with_text(
            text=text, font_size=font_size, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        highlighted_image = create_surface_with_text(
            text=text, font_size=font_size * 1.2, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        self.images = [default_image, highlighted_image]
        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position),
        ]

        # assign button action
        self.action = action

        super().__init__()

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos, mouse_up):
        """ Updates the mouse_over variable and returns the button's
            action value when clicked.
        """
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        """ Draws element onto a surface """
        surface.blit(self.image, self.rect)
#Bucle principal del juego.
def main():
    pygame.init()

    #Lee el logo del tec, lo reescala y define su futura posición
    logoDelTec = pygame.image.load("logotec2019.png")
    logoDelTec = pygame.transform.scale(logoDelTec, (250, 100))
    tecX = 0
    tecY = 0

    screen = pygame.display.set_mode((800, 600))
    #screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    #Define el nombre de la ventana y el logo
    pygame.display.set_caption("Proyecto")
    icon = pygame.image.load("matematicas.png")
    pygame.display.set_icon(icon)

    BLUE = (41, 45, 111)
    WHITE = (255, 255, 255)

    # create a ui element

    quit_btn = UIElement(
        center_position=(400, 500),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Salir",
        action=GameState.QUIT,
    )

    
    uielement = UIElement(
        center_position=(400, 400),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Juego de dados",
    )

    
    running = True
    while running:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            if event.type == pygame.QUIT:
                running = False


        screen.fill(BLUE)

        #Dibuja en pantalla el logo
        screen.blit(logoDelTec, (tecX, tecY))

        ui_action = quit_btn.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return
        quit_btn.draw(screen)

        uielement.update(pygame.mouse.get_pos(), mouse_up)
        uielement.draw(screen)
        pygame.display.flip()

class GameState(Enum):
    QUIT = -1

if __name__ == '__main__':
    main()
