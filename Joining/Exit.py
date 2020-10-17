from Extra import *
print("AJUA")
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.init()
pygame.mixer.init(frequency=44100)
pygame.mixer.music.load(path + "\OST.mp3")
pygame.mixer.music.play(-1)

def xd():
    print("hola que tal")

def exit_main():
    
    print("Is doing shit")
    global running
    global path

    #path = os.path.abspath("..\Resources")
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
        font_size=30,
        bg_rgb=BG,
        inactive_rgb=BLUE_INACTIVE,
        active_rgb=BLUE_ACTIVE,
        text="Prueba",
    )

    c = UIElement(
        center_position=(400, 400),
        font_size=30,
        bg_rgb=BG,
        inactive_rgb=RED_INACTIVE,
        active_rgb=RED_ACTIVE,
        text="Salir",
        #action="end_main(running)"
    )

    while running.exitState:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            if event.type == pygame.QUIT:
                end_main(running)

        screen.fill(BG)

        #Dibuja en pantalla el logo
        screen.blit(logoDelTec, (tecX, tecY))

        ui_action = c.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return
        c.draw(screen)

        thanks.update(pygame.mouse.get_pos(), mouse_up)
        thanks.draw(screen)

        pygame.display.flip()
