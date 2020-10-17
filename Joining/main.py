import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum
import random
import time
import sys

pygame.init()

num_to_guess = random.randint(1, 25)
intentos = 3
state = ''
done = False

path = os.path.abspath("..\Resources")

def init():
    # Inicializa el reproductor de música
    pygame.mixer.init()
    # Lee el OST
    pygame.mixer.music.load(path + "\OST.mp3")
    # Comienza a reproducirlo
    pygame.mixer.music.play(-1)

#Clase mutable para poder cambiar entre juegos

class gameState():
    def __init__(self):
        self.running = True
        self.exitState = True
        self.menu_dados = True
        self.ayuda_sumas = True
        self.numeros_aleatorios = True
        self.facil = True
        self.normal = True
        self.dificil = True


running = gameState()


def end_main(running):
    running.running = False

#Define el nombre de la ventana y el logo

COLOR_INACTIVE = (123, 255, 91)
COLOR_ACTIVE = (38, 190, 1)
READABLE_GREEN = (76, 251, 33)

BG = (0, 0, 0)

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

    def __init__(self, txt, location, size=(160, 30), bg=BG, fg=READABLE_GREEN, font_name="Segoe Print", font_size=20):
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
        self.txt_surf, _ = self.font.render(
            text=self.txt, fgcolor=self.fg, bgcolor=self.bg)
        self.txt_rect = self.txt_surf.get_rect(
            center=[s//2 for s in self.size])

        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(topleft=location)

    def update(self):
        """ 
            Actualiza el sprite.
        """
        self.surface.fill(self.bg)
        self.txt_surf, _ = self.font.render(
            text=self.txt, fgcolor=self.fg, bgcolor=self.bg)
        self.surface.blit(self.txt_surf, self.txt_rect)

    def draw(self, screen):
        """ Dibuja un elemento sobre la superficie."""
        screen.blit(self.surface, self.rect)

class InputBox():

    def __init__(self, x, y, w, h, text='', COLOR_ACTIVE = COLOR_ACTIVE, 
    COLOR_INACTIVE= COLOR_INACTIVE, FONT=pygame.font.Font(None, 32), VAR = None ):
        """ 
        args
        x, y, anchura, altura, texto de default
        """
        self.FONT = FONT
        self.var = VAR
        self.default_text = text
        self.width = w
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.color_inactive = COLOR_INACTIVE
        self.color_active = COLOR_ACTIVE
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
                if self.text == self.default_text:
                    self.text = ''
                    self.txt_surface = self.FONT.render(self.text, True, self.color)
            else:
                self.active = False
            # Cambia el color de la caja para avisarle al ususario que si esta interactuando con el objeto.
            self.color = self.color_active if self.active else self.color_inactive
        if event.type == pygame.KEYDOWN:
            if self.active:

                if event.key == pygame.K_RETURN:
                    try:
                        take_a_guess(int(self.text))
                    except:
                        if intentos > 0 and state != "      ¡Lo adivinaste! ¡Guau!":
                            state = "       Ingresa un número."
                    self.var = self.text
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    #Se asegura que no se salga del rectangulo
                    if self.txt_surface.get_width() < self.width-20:
                        self.text += event.unicode
                # Renderiza el texto (lo actualiza).
                self.txt_surface = self.FONT.render(self.text, True, self.color)

    def update(self):
        # Ajusta el tamaño de la caja al texto.
        width = max(self.width, self.txt_surface.get_width()+10)
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
    num_to_guess = random.randint(1, 25)
    intentos = 3
    state = ''

#Termina la pantalla

def end():
    global done
    reintentar()
    done = True

def extra_main():
    global intentos
    global done
    screen = pygame.display.set_mode((800, 600))
    reintentar()
    done = False
    clock = pygame.time.Clock()
    input_box = InputBox(
        275, 300, 250, 32, "Ingresa tu intento aquí")

    state1 = Label(
        txt='Estoy pensando en un numero entre 1 y 25.',
        location=(150, 150),
        size=(500, 30),
    )
    state2 = Label(
        txt=f'Tienes {intentos} intentos para adivinarlo.',
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
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            if event.type == pygame.QUIT:
                end()
                end_main(running)
                return
                

            input_box.handle_event(event)

        screen.fill(BG)

        ui_action = regresar_main_menu.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return
        regresar_main_menu.draw(screen)

        #input_box.update()
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

        pygame.display.flip()
        clock.tick(30)

def end_exit_main(running):
    running.exitState = False

def finish(running):
    end_main(running)
    end_exit_main(running)

def exit_main():

    global running
    global path

    logoDelTec = pygame.image.load(path + "\logotec2019.png")
    logoDelTec = pygame.transform.scale(logoDelTec, (250, 100))
    tecX = 0
    tecY = 0

    screen = pygame.display.set_mode((800, 600))
    #screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

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

    thanks = UIElement(
        center_position=(400, 250),
        font_size=25,
        bg_rgb=BG,
        inactive_rgb=RED_INACTIVE,
        active_rgb=RED_INACTIVE,
        text="Agradecemos tu participación",
    )

    finish = UIElement(
        center_position=(400, 400),
        font_size=30,
        bg_rgb=BG,
        inactive_rgb=RED_INACTIVE,
        active_rgb=RED_ACTIVE,
        text="Finalizar",
        action="finish(running)"
    )

    while running.exitState:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            if event.type == pygame.QUIT:
                end_main(running)
                end_exit_main(running)
                return

        screen.fill(BG)

        #Dibuja en pantalla el logo
        screen.blit(logoDelTec, (tecX, tecY))

        ui_action = finish.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return
        finish.draw(screen)

        thanks.draw(screen)

        pygame.display.flip()

#Bucle principal del juego.

def main():
    global running
    path = os.path.abspath("..\Resources")
    screen = pygame.display.set_mode((800, 600))

    #Lee el logo del tec, lo reescala y define su futura posición
    logoDelTec = pygame.image.load(path + "\logotec2019.png")
    logoDelTec = pygame.transform.scale(logoDelTec, (250, 100))
    tecX = 0
    tecY = 0

    
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
        inactive_rgb=BLUE_INACTIVE,
        active_rgb=BLUE_ACTIVE,
        text="Juego de dados",
        action="main_menu_dados()"
    )

    juego_matematicas = UIElement(
        center_position=(400, 300),
        font_size=30,
        bg_rgb=BG,
        inactive_rgb=YELLOW_INACTIVE,
        active_rgb=YELLOW_ACTIVE,
        text="Juego de sumas",
        action="juego_sumas_main()"
    )

    juego_extra = UIElement(
        center_position=(400, 350),
        font_size=30,
        bg_rgb=BG,
        inactive_rgb=GREEN_INACTIVE,
        active_rgb=GREEN_ACTIVE,
        text="Juego extra",
        action="extra_main()"
    )

    quit_btn = UIElement(
        center_position=(400, 400),
        font_size=30,
        bg_rgb=BG,
        inactive_rgb=RED_INACTIVE,
        active_rgb=RED_ACTIVE,
        text="Salir",
        action="exit_main()"

    )

    while running.running:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            if event.type == pygame.QUIT:
                end_main(running)
                return

        screen.fill(BG)

        #Dibuja en pantalla el logo
        screen.blit(logoDelTec, (tecX, tecY))
        
        quit_btn.update(pygame.mouse.get_pos(), mouse_up)
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

def end_menu_dados(running):
    running.menu_dados = False

NAME1 = "PLAYER"
NAME2 = "PLAYER"

def print_names1():
    global NAME1
    global NAME2
    print(f'Player 1: {NAME1}')
    print(f'Player 2: {NAME2}')

def print_names2():
    global NAME1
    global NAME2
    print(f'Player 1: {NAME2}')
    print(f'Player 2: {NAME1}')

def main_menu_dados():
    global running
    global NAME1
    global NAME2
    screen = pygame.display.set_mode((800, 600))

    running.menu_dados = True
    NAME1 = "PLAYER"
    NAME2 = "PLAYER"
    path = os.path.abspath("..\Resources")

    #Define alguna constantes de colroes
    BG = (0, 0, 0)

    logoDados = pygame.image.load(path + "\dados.png")
    logoDados = pygame.transform.scale(logoDados, (100, 100))
    dadoX = 335
    dadoY = 40

    BLUE_INACTIVE = pygame.Color('lightskyblue3')
    BLUE_ACTIVE = pygame.Color('dodgerblue2')
    Extra_BLUE = (63, 84, 128)

    player_1 = InputBox(180, 280, 170, 25, "Nombre Jugador 1", 
                        BLUE_ACTIVE, BLUE_INACTIVE, FONT=pygame.font.Font(None, 25), VAR = "PLAYER")

    player_2 = InputBox(450, 280, 170, 25, "Nombre Jugador 2", 
                        BLUE_ACTIVE, BLUE_INACTIVE, FONT=pygame.font.Font(None, 25), VAR="PLAYER")

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
    aclaracion = UIElement(
        center_position=(400, 240),
        font_size=20,
        bg_rgb=BG,
        inactive_rgb=Extra_BLUE,
        active_rgb=BLUE_ACTIVE,
        text="Presiona ENTER para confirmar",
    )


    jugador1 = UIElement(
        center_position=(250, 460),
        font_size=25,
        bg_rgb=BG,
        inactive_rgb=BLUE_INACTIVE,
        active_rgb=BLUE_ACTIVE,
        text="Jugador 1",
        action = "print_names1()"
    )

    jugador2 = UIElement(
        center_position=(550, 460),
        font_size=25,
        bg_rgb=BG,
        inactive_rgb=BLUE_INACTIVE,
        active_rgb=BLUE_ACTIVE,
        text="Jugador 2",
        action="print_names2()"
    )

    regresar = UIElement(
        center_position=(100, 62),
        font_size=22,
        bg_rgb=BG,
        inactive_rgb=BLUE_INACTIVE,
        active_rgb=BLUE_ACTIVE,
        text="Regresar",
        action="end_menu_dados(running)",
    )

    while running.menu_dados:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            if event.type == pygame.QUIT:
                end_main(running)
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

        regresar.update(pygame.mouse.get_pos(), mouse_up)
        regresar.draw(screen)

        quien_empieza.draw(screen)
        nombres.draw(screen)
        aclaracion.draw(screen)

        jugador1.update(pygame.mouse.get_pos(), mouse_up)
        jugador1.draw(screen)

        jugador2.update(pygame.mouse.get_pos(), mouse_up)
        jugador2.draw(screen)

        pygame.display.flip()

        NAME1 = player_1.var
        NAME2 = player_2.var


##################################################################################################################

class CreatingText:
    def __init__(self,font,sizet,text,tf,color):
        self.myfont=pygame.font.SysFont(font,sizet)
        self.textsurface=self.myfont.render(text,tf,color)

def exit_all():
    global running
    running.running = False
    running.exitState = False
    running.menu_dados = False
    running.ayuda_sumas = False
    running.numeros_aleatorios = False
    running.facil = False
    running.normal = False
    running.dificil = False
    running.nuevaP = False

def ayuda_sumas_end():
    global running
    running.ayuda_sumas = False

def Instrucciones():
    global running
    running.ayuda_sumas = True

    BG=(0,0,0)
    COLOR_INACTIVE = (230, 234, 112)
    COLOR_ACTIVE = (243, 250, 3)
    
    screen2=pygame.display.set_mode((800,600))

    text1 = UIElement(
        center_position=(400, 150),
        font_size=30,
        bg_rgb=BG,
        inactive_rgb=COLOR_INACTIVE,
        active_rgb=COLOR_ACTIVE,
        text="Instrucciones juego de sumas:",
    )
    text2 = UIElement(
        center_position=(400, 220),
        font_size=25,
        bg_rgb=BG,
        inactive_rgb=COLOR_INACTIVE,
        active_rgb=COLOR_ACTIVE,
        text="»Sumar dos numeros aleatorios",
    )
    text3 = UIElement(
        center_position=(400, 270),
        font_size=25,
        bg_rgb=BG,
        inactive_rgb=COLOR_INACTIVE,
        active_rgb=COLOR_ACTIVE,
        text="»Facil: numeros aleatorios de 0-100",
    )
    text4 = UIElement(
        center_position=(400, 320),
        font_size=25,
        bg_rgb=BG,
        inactive_rgb=COLOR_INACTIVE,
        active_rgb=COLOR_ACTIVE,
        text="»Medio: numeros aleatorios de 0-5000",
    )
    text5 = UIElement(
        center_position=(400, 370),
        font_size=25,
        bg_rgb=BG,
        inactive_rgb=COLOR_INACTIVE,
        active_rgb=COLOR_ACTIVE,
        text="»Loco: numeros aleatorios de 0-1000",
    )
    regresar_main_menu = UIElement(
        center_position=(100, 62),
        font_size=22,
        bg_rgb=BG,
        inactive_rgb=COLOR_INACTIVE,
        active_rgb=COLOR_ACTIVE,
        text="Regresar",
        action="ayuda_sumas_end()",
    )
    
    while running.ayuda_sumas:
        mouse_up = False
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            if(event.type==pygame.KEYDOWN):
                if(event.key==pygame.K_ESCAPE):
                    screen2=pygame.display.set_mode((800,600))
                    running.ayuda_sumas = False
                    return
        
        screen2.fill(BG)
        text1.draw(screen2)
        text2.draw(screen2)
        text3.draw(screen2)
        text4.draw(screen2)
        text5.draw(screen2)

        ui_action = regresar_main_menu.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return
        regresar_main_menu.draw(screen2)

        pygame.display.update()

def preguntar():
    teclado=""
    size=(800,600)
    BG = (0,0,0)
    screend=pygame.display.set_mode(size)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_all()
                return
            if(event.type==pygame.KEYDOWN):
                if(event.unicode=='1'or event.unicode=='2'or event.unicode=='3'or event.unicode=='4'or event.unicode=='5'or event.unicode=='6' or event.unicode=='7'or event.unicode=='9'or event.unicode=='8' or event.unicode=='0'):
                    if len(teclado) < 7:
                        teclado += event.unicode
                elif(event.unicode=='\r'):
                    return teclado
                elif(event.key == pygame.K_BACKSPACE):
                    teclado = teclado[:-1]

        screend.fill(BG)
        entry=pygame.draw.rect(screend,( 71, 69, 18 ),(250,400,250,50))
        te = CreatingText('Comic Sans MS', 40,
                        'Cuantas sumas realizarás?', True, (161, 156, 13))
        texto=CreatingText('Comic Sans MS',50,teclado,True,(0,0,0))
        screend.blit(texto.textsurface,(255,390))
        screend.blit(te.textsurface,(120,100))
        pygame.display.update()

def check_ans(numer1,number2,k,score,Vidas,tecleado, r):
    if tecleado.var is not None:
        k -= 1
        suma = numer1+number2
        if(str(suma) == str(tecleado.var)):
            score += 1
            numer1 = random.randrange(r)
            number2 = random.randrange(r)
        else:
            Vidas -= 1
            numer1 = random.randrange(r)
            number2 = random.randrange(r)
        tecleado.var = None
    return [k, score, Vidas, numer1, number2]

def nivel_dificil():
    global running
    running.dificil = True
    HARD_INACTIVE = (208, 142, 52)
    HARD_ACTIVE = (209, 3, 3)

    l = preguntar()
    k = int(l)
    tp = ''
    size = (800, 600)
    screen = pygame.display.set_mode(size)
    n = (0, 0, 0)
    verde = (0, 0, 255)
    score = 0
    Vidas = 3
    numer1 = random.randrange(1000)
    number2 = random.randrange(1000)

    tecleado = InputBox(
        250, 300, 300, 32, "Ingresa tu respuesta aquí", COLOR_ACTIVE=HARD_ACTIVE,
        COLOR_INACTIVE=HARD_INACTIVE, FONT=pygame.font.Font(None, 32), VAR=None)

    numero1 = Label(
        txt=str(numer1),
        location=(75, 200),
        size=(250, 30),
        fg=HARD_INACTIVE
    )
    numero2 = Label(
        txt=str(numer1),
        location=(375, 200),
        size=(250, 30),
        fg=HARD_INACTIVE
    )
    texto = Label(
        txt=str(score),
        location=(-40, 80),
        size=(300, 30),
        fg=HARD_INACTIVE
    )

    vidas = Label(
        txt=str(Vidas),
        location=(30, 40),
        size=(150, 30),
        fg=HARD_INACTIVE
    )

    h = 0
    #Contar tiempo
    #Hacer el entry
    #Validar,sumar score y restar vidas
    while running.dificil:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_all()
                return

            tecleado.handle_event(event)

        screen.fill(n)

        tecleado.update()
        tecleado.draw(screen)

        texto.txt = f'Puntuación: {score}'
        texto.update()
        texto.draw(screen)

        vidas.txt = f'Vidas: {Vidas} '
        vidas.update()
        vidas.draw(screen)

        numero1.txt = f'Num1: {numer1}'
        numero1.update()
        numero1.draw(screen)

        numero2.txt = f'Num2: {str(number2)}'
        numero2.update()
        numero2.draw(screen)

        checkpoint = check_ans(numer1, number2, k, score,
                            Vidas, tecleado, 1000)
        k = checkpoint[0]
        score = checkpoint[1]
        Vidas = checkpoint[2]
        numer1 = checkpoint[3]
        number2 = checkpoint[4]

        if(Vidas == 0):
            Nueva_pestana((800, 600), HARD_INACTIVE, HARD_ACTIVE, "Uy, creo que se te acabaron las vidas",
                        F'Tu puntación fue de {score} ')
            running.dificil = False
            return
        elif(k == 0):
            Nueva_pestana((800, 600), HARD_INACTIVE, HARD_ACTIVE, "Juego concluido",
                        f'Puntuación: {score}', f'Vidas: {Vidas} ')
            running.dificil = False
            return
        pygame.display.flip()

def nivel_medio():
    global running
    running.normal = True
    NORMAL_INACTIVE = (208, 201, 52)
    NORMAL_ACTIVE = (249, 249, 35)

    l = preguntar()
    k = int(l)
    tp = ''
    size = (800, 600)
    screen = pygame.display.set_mode(size)
    n = (0, 0, 0)
    verde = (0, 0, 255)
    score = 0
    Vidas = 3
    numer1 = random.randrange(500)
    number2 = random.randrange(500)

    tecleado = InputBox(
        250, 300, 300, 32, "Ingresa tu respuesta aquí", COLOR_ACTIVE=NORMAL_ACTIVE,
        COLOR_INACTIVE=NORMAL_INACTIVE, FONT=pygame.font.Font(None, 32), VAR=None)

    #numero1=CreatingText('Comic Sans MS',50,'{}'.format(str(numer1)),True,verde)
    #numero2=CreatingText('Comic Sans MS',50,'{}'.format(str(number2)),True,verde)
    #texto=CreatingText('Comic Sans MS',50,'Score: {}'.format(str(score)),True,verde)
    #vidas=CreatingText('Comic Sans MS',50,'Vidas: {} '.format(str(Vidas)),True,verde)

    numero1 = Label(
        txt=str(numer1),
        location=(75, 200),
        size=(250, 30),
        fg=NORMAL_INACTIVE
    )
    numero2 = Label(
        txt=str(numer1),
        location=(375, 200),
        size=(250, 30),
        fg=NORMAL_INACTIVE
    )
    texto = Label(
        txt=str(score),
        location=(-40, 80),
        size=(300, 30),
        fg=NORMAL_INACTIVE
    )

    vidas = Label(
        txt=str(Vidas),
        location=(30, 40),
        size=(150, 30),
        fg=NORMAL_INACTIVE
    )

    h = 0
    #Contar tiempo
    #Hacer el entry
    #Validar,sumar score y restar vidas
    while running.normal:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_all()
                return
            tecleado.handle_event(event)

        screen.fill(n)

        tecleado.update()
        tecleado.draw(screen)

        texto.txt = f'Puntuación: {score}'
        texto.update()
        texto.draw(screen)

        vidas.txt = f'Vidas: {Vidas} '
        vidas.update()
        vidas.draw(screen)

        numero1.txt = f'Num1: {numer1}'
        numero1.update()
        numero1.draw(screen)

        numero2.txt = f'Num2: {number2}'
        numero2.update()
        numero2.draw(screen)

        checkpoint = check_ans(numer1, number2, k, score, Vidas, tecleado, 500)
        k = checkpoint[0]
        score = checkpoint[1]
        Vidas = checkpoint[2]
        numer1 = checkpoint[3]
        number2 = checkpoint[4]

        if(Vidas == 0):
            Nueva_pestana((800, 600), NORMAL_INACTIVE, NORMAL_ACTIVE, "Uy, creo que se te acabaron las vidas",
                        F'Tu puntación fue de {score} ')
            running.normal = False
            return
        elif(k == 0):
            Nueva_pestana((800, 600), NORMAL_INACTIVE, NORMAL_ACTIVE, "Juego concluido",
                        f'Puntuación: {score}', f'Vidas: {Vidas} ')
            running.normal = False
            return
        pygame.display.flip()

def Nivel_Facil():
    global running
    running.facil = True
    EASY_INACTIVE = (203, 221, 52)
    EASY_ACTIVE = (116, 249, 35)


    l=preguntar()
    k=int(l)
    tp=''
    size=(800,600)
    screen=pygame.display.set_mode(size)
    n=(0,0,0)

    score=0
    Vidas=3
    numer1=random.randrange(100)
    number2=random.randrange(100)

    tecleado = InputBox(
        250, 300, 300, 32, "Ingresa tu respuesta aquí", COLOR_ACTIVE = EASY_ACTIVE, 
    COLOR_INACTIVE= EASY_INACTIVE, FONT=pygame.font.Font(None, 32), VAR = None )

    #numero1=CreatingText('Comic Sans MS',50,'{}'.format(str(numer1)),True,verde)
    #numero2=CreatingText('Comic Sans MS',50,'{}'.format(str(number2)),True,verde)
    #texto=CreatingText('Comic Sans MS',50,'Score: {}'.format(str(score)),True,verde)
    #vidas=CreatingText('Comic Sans MS',50,'Vidas: {} '.format(str(Vidas)),True,verde)

    numero1= Label(
        txt=str(numer1),
        location=(75, 200),
        size=(250, 30),
        fg=EASY_INACTIVE
    )
    numero2= Label(
        txt=str(numer1),
        location=(375, 200),
        size=(250, 30),
        fg=EASY_INACTIVE
    )
    texto = Label(
        txt=str(score),
        location=(-40, 80),
        size=(300, 30),
        fg=EASY_INACTIVE
    )

    vidas = Label(
        txt=str(Vidas),
        location=(30, 40),
        size=(150, 30),
        fg=EASY_INACTIVE
    )

    #Contar tiempo
    #Hacer el entry
    #Validar,sumar score y restar vidas
    while running.facil:
        mouse_up = False
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_all()
                return

            tecleado.handle_event(event)
            
        screen.fill(n)

        tecleado.update()
        tecleado.draw(screen)

        texto.txt = f'Puntuación: {score}'
        texto.update()
        texto.draw(screen)

        vidas.txt = f'Vidas: {Vidas} '
        vidas.update()
        vidas.draw(screen)

        numero1.txt = f'Num1: {numer1}'
        numero1.update()
        numero1.draw(screen)

        numero2.txt = f'Num2: {number2}'
        numero2.update()
        numero2.draw(screen)

        checkpoint = check_ans(numer1,number2,k,score,Vidas,tecleado,100)
        k = checkpoint[0]
        score = checkpoint[1]
        Vidas = checkpoint[2]
        numer1 = checkpoint[3]
        number2 = checkpoint[4]

        

        if(Vidas == 0):
            Nueva_pestana((800, 600), EASY_INACTIVE, EASY_ACTIVE, "Uy, creo que se te acabaron las vidas", 
            F'Tu puntación fue de {score} ')
            running.facil = False
            return
        elif(k == 0):
            Nueva_pestana((800, 600), EASY_INACTIVE, EASY_ACTIVE, "Juego concluido", 
            f'Puntuación: {score}', f'Vidas: {Vidas} ')
            running.facil = False
            return

        pygame.display.flip()

def toMain():
    global running
    running.nuevaP = False
    juego_sumas_main()

def end_np():
    global running
    running.numeros_aleatorios = True
    running.facil = False
    running.normal = False
    running.dificil = False
    running.nuevaP = False

def Nueva_pestana(size, COLOR_INACTIVE, COLOR_ACTIVE, *textos):
    global running
    running.nuevaP = True
    BG=( 0, 0, 0)
    screen2=pygame.display.set_mode(size)
    
    to_display = []
    Y = 0
    for texto in textos:
        to_display.append(
        UIElement(
        center_position=(400, 200 + Y),
        font_size=30,
        bg_rgb=BG,
        inactive_rgb=COLOR_ACTIVE,
            active_rgb=COLOR_ACTIVE,
        text = texto,
    )
    )   
        Y += 50

    regresar_main_menu = UIElement(
        center_position=(100, 40),
        font_size=22,
        bg_rgb=BG,
        inactive_rgb=COLOR_INACTIVE,
        active_rgb=COLOR_ACTIVE,
        text="Regresar",
        action="end_np()",
    )
    

    while running.nuevaP:
        mouse_up = False
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_all()
                return
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        
        screen2.fill(BG)
        
        ui_action = regresar_main_menu.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return
        regresar_main_menu.draw(screen2)

        for texto in to_display:
            texto.draw(screen2)

        pygame.display.flip()

def exit_radnnum():
    global running
    running.numeros_aleatorios = False

def juego_sumas_main():
    global running
    running.numeros_aleatorios = True
    
    pygame.init()
    screen=pygame.display.set_mode((800,600))

    COLOR_INACTIVE = (230, 234, 112)
    COLOR_ACTIVE = (243, 250, 3)
    EASY_INACTIVE = (203, 221, 52)
    EASY_ACTIVE = (116, 249, 35)
    NORMAL_INACTIVE = (208, 201, 52)
    NORMAL_ACTIVE = (249, 249, 35)
    HARD_INACTIVE = (208, 142, 52)
    HARD_ACTIVE = (209, 3, 3)
    BG = (0,0,0)

    regresar_main_menu = UIElement(
        center_position=(100, 60),
        font_size=22,
        bg_rgb=BG,
        inactive_rgb=COLOR_INACTIVE,
        active_rgb=COLOR_ACTIVE,
        text="Regresar",
        action="exit_radnnum()",
    )

    facil = UIElement(
        center_position=(400, 225),
        font_size=40,
        bg_rgb=BG,
        inactive_rgb=EASY_INACTIVE,
        active_rgb=EASY_ACTIVE,
        text="Fácil",
        action="Nivel_Facil()",
    )
    normal = UIElement(
        center_position=(400, 300),
        font_size=40,
        bg_rgb=BG,
        inactive_rgb=NORMAL_INACTIVE,
        active_rgb=NORMAL_ACTIVE,
        text="Normal",
        action="nivel_medio()",
    )
    loco = UIElement(
        center_position=(400, 375),
        font_size=40,
        bg_rgb=BG,
        inactive_rgb=HARD_INACTIVE,
        active_rgb=HARD_ACTIVE,
        text="Loco",
        action="nivel_dificil()",
    )

    #image0=pygame.image.load(path + '\interrogation.png')
    #image0=pygame.transform.scale(image0,(40,40))
    #lx=40
    #ly=40
    while running.numeros_aleatorios:
        mouse_up = False
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_all()
                return
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True

        screen.fill(BG)

        ui_action = regresar_main_menu.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return
        regresar_main_menu.draw(screen)
        
        """
        button=Button(image0,(lx,ly))# creamos un objeto button
        button.on_click(event)# llamamos a la funcion on_click
        screen.blit(button.image,button.rect)# lo proyectamos en la pantalla
        """

        #screen.blit(image0,(lx,ly))

        #Dificultad

        facil.update(pygame.mouse.get_pos(), mouse_up)
        facil.draw(screen)

        normal.update(pygame.mouse.get_pos(), mouse_up)
        normal.draw(screen)

        loco.update(pygame.mouse.get_pos(), mouse_up)
        loco.draw(screen)

        pygame.display.flip()

##################################################################################################################

if __name__ == '__main__':
    init()
    BIENVENIDA = open(path + "\Bienvenida.txt", 'r')
    print(BIENVENIDA.read())
    BIENVENIDA.close()
    input("Presiona ENTER para continuar;")
    main()
