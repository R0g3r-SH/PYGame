import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum
import os
import random


num_to_guess = random.randint(1,25)
intentos = 3
state=''
done = False

pygame.init()
screen = pygame.display.set_mode((800, 600))

FONT = pygame.font.Font(None, 32)
path = os.path.abspath("..\Resources")


#Cierra el global
class gameState():
    def __init__(self):
        self.running = True

running = gameState()


def end_main(running):
    running.running = False

#Define el nombre de la ventana y el logo
pygame.display.set_caption("Juego Extra")
icon = pygame.image.load(path + "\matematicas.png")
pygame.display.set_icon(icon)

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
BG = (30, 30, 30)


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
            text=text, font_size=font_size * 1.1, text_rgb=active_rgb, bg_rgb=bg_rgb
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
                
                try:
                    eval(self.action)
                except:
                    running = False
                
        else:
            self.mouse_over = False

    def draw(self, surface):
        """ Dibuja un elemento sobre la superficie."""
        surface.blit(self.image, self.rect)

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
        global state
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Si el usuario hizo click en la caja de texto.
            if self.rect.collidepoint(event.pos):
                # Activa la variable de que esta siendo seleccionado.
                self.active = not self.active
                if self.text == "Ingresa tu intento aquí.":
                    self.text = ''
                    self.txt_surface = FONT.render(self.text, True, self.color)
            else:
                self.active = False
            # Cambia el color de la caja para avisarle al ususario que si esta interactuando con el objeto.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:

                if event.key == pygame.K_RETURN:
                    try:
                        take_a_guess(int(self.text))
                    except:
                        if intentos > 0 and state != "      ¡Lo adivinaste! ¡Guau!":
                            state = "       Ingresa un número."
                    
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    #Se asegura que no se salga del rectangulo
                    if self.txt_surface.get_width() < 240:
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
        
#Comprueba el numero de intentos restantes
def check_tries(case):
    global intentos
    if intentos > 0:
        return " Muy bajo. Vuelve a intentarlo." if case == 0 else "Muy alto. Vuelve a intentarlo."
    return "     Lo siento, has perdido."

#Logica para mostrar si el intento es muy alto, muy bajo, le atino o perdio.
def take_a_guess(guess):
    global num_to_guess
    global intentos
    global state
    if intentos == 0 or state == "      ¡Lo adivinaste! ¡Guau!":
        return
    if guess == num_to_guess:
        state = "      ¡Lo adivinaste! ¡Guau!"
    elif guess < num_to_guess:
        intentos -= 1
        #state = " Muy bajo. Vuelve a intentarlo."
        state = check_tries(0)
    else:
        intentos -= 1
        #state = "Muy alto. Vuelve a intentarlo."
        state = check_tries(1)

#Reinicia los valores
def reintentar():
    global intentos
    global num_to_guess
    global state
    num_to_guess = random.randint(1,25)
    intentos = 3
    state=''

def end():
    global done
    done = True

def extra_main():
    global intentos
    global done

    done = False
    clock = pygame.time.Clock()
    input_box = InputBox(275, 300, 140, 32, "Ingresa tu intento aquí.")
    

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
    state3 = Label(
        txt=state,
        location=(-150, 400),
        size=(800, 30),
    )

    ans = Label(
        txt="",
        location=(-150, 450),
        size=(800, 30),
    )

    retry = UIElement(
        center_position=(250, 60),
        font_size=20,
        bg_rgb=BG,
        inactive_rgb=COLOR_INACTIVE,
        active_rgb=COLOR_ACTIVE,
        text="Reintentar",
        action="reintentar()",
    )

    regresar_main_menu = UIElement(
        center_position=(100, 62),
        font_size=22,
        bg_rgb=BG,
        inactive_rgb=COLOR_INACTIVE,
        active_rgb=COLOR_ACTIVE,
        text="Regresar",
        action="end()",
    )

    while not done:
        mouse_up= False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            if event.type == pygame.QUIT:
                end()
                end_main(running)
            input_box.handle_event(event)

        screen.fill((30, 30, 30))
        
        input_box.update()
        input_box.draw(screen)

        state1.update()
        state1.draw(screen)

        state2.txt = f'Tienes {intentos} intentos para adivinarlo.'
        state2.update()
        state2.draw(screen)

        state3.txt = state
        state3.update()
        state3.draw(screen)

        if intentos == 0:
            ans.txt = "  El numero que pensé era " + str(num_to_guess)
            ans.update()
            ans.draw(screen)

        retry.update(pygame.mouse.get_pos(), mouse_up)
        retry.draw(screen)

        regresar_main_menu.update(pygame.mouse.get_pos(), mouse_up)
        regresar_main_menu.draw(screen)

        pygame.display.flip()
        clock.tick(30)

"""
if __name__ == '__main__':
    extra_main()
    pygame.quit()
"""
