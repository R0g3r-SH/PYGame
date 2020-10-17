import sys
import pygame
import os
import random
import time

from main import UIElement, InputBox, running, Label

path = os.path.abspath("..\Resources")

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

    #text1=CreatingText('Baloo Bhai',50,"Instrucciones: ",False,(255,255,255))
    #text2=CreatingText('Comic Sans MS',50,"Sumar dos numeros aleatorios",False,(0,0,255))
    #text3=CreatingText('Comic Sans MS',50,"Facil: numeros aleatorios de 0-100",False,(0,255,0))
    #text4=CreatingText('Comic Sans MS',50,"Medio: numeros aleatorios de 0-500",False,(255,0,0))
    #text5=CreatingText('Comic Sans MS',50,"Loco: numeros aleatorios de 0-1000",False,(163, 73, 164))

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

        #screen2.blit(text1.textsurface,(150,100))
        #screen2.blit(text2.textsurface,(150,200))
        #screen2.blit(text3.textsurface,(150,300))
        #screen2.blit(text4.textsurface,(150,400))
        #screen2.blit(text5.textsurface,(150,500))

        pygame.display.update()

def preguntar():
    unido=''
    teclado=""
    size=(800,600)
    BG = (0,0,0)
    screend=pygame.display.set_mode(size)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
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
        te = CreatingText('Comic Sans MS', 60,
                        'Cuantas sumas haras?', True, (161, 156, 13))
        texto=CreatingText('Comic Sans MS',50,teclado,True,(0,0,0))
        screend.blit(texto.textsurface,(255,390))
        screend.blit(te.textsurface,(100,100))
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

    #numero1=CreatingText('Comic Sans MS',50,'{}'.format(str(numer1)),True,verde)
    #numero2=CreatingText('Comic Sans MS',50,'{}'.format(str(number2)),True,verde)
    #texto=CreatingText('Comic Sans MS',50,'Score: {}'.format(str(score)),True,verde)
    #vidas=CreatingText('Comic Sans MS',50,'Vidas: {} '.format(str(Vidas)),True,verde)

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
            """
            elif(event.type==pygame.KEYDOWN):
                    if (event.unicode=='\r'):
                        k-=1
                        suma=numer1+number2
                        if(str(suma)==tecleado.var):
                            score+=1
                            numer1=random.randrange(100)
                            number2=random.randrange(100)
                        else:
                            Vidas-=1
                            numer1=random.randrange(100)
                            number2=random.randrange(100)
                    
            """
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
            """
            elif(event.type==pygame.KEYDOWN):
                    if (event.unicode=='\r'):
                        k-=1
                        suma=numer1+number2
                        if(str(suma)==tecleado.var):
                            score+=1
                            numer1=random.randrange(100)
                            number2=random.randrange(100)
                        else:
                            Vidas-=1
                            numer1=random.randrange(100)
                            number2=random.randrange(100)
                    
            """
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
        center_position=(200, 60),
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
    help = UIElement(
        center_position=(60, 60),
        font_size=40,
        bg_rgb=BG,
        inactive_rgb=BG,
        active_rgb=BG,
        text="   ",
        action="Instrucciones()",
    )
    white=( 255, 255, 255)
    green=( 0, 255, 0)
    red=( 255, 0, 0)
    blue=( 0, 0, 255)
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

        """
        #butonFacil=pygame.draw.rect(screen,(255,0,0),(270,100,250,50))
        #butonIntermedio=pygame.draw.rect(screen,(0,255,0),(270,200,250,50))
        #butonDificil=pygame.draw.rect(screen,(0,0,255),(270,300,250,50))
        "x,my
        mx1,my2
        mx2,my2
        #texto=CreatingText('Comic Sans MS',50,'Facil',True,(255,255,255))
        #texto2=CreatingText('Comic Sans MS',50,'Normal',True,(255,255,255))
        #texto3=CreatingText('Comic Sans MS',50,'Loco',True,(255,255,255))
        #screen.blit(texto.textsurface,(350,100))
        #screen.blit(texto2.textsurface,(350,200))
        #screen.blit(texto3.textsurface,(350,300))
        """

        #sumando score
        """
        screen.blit(t1.textsurface,(200,500))
        screen.blit(t2.textsurface,(400,500))
        screen.blit(t3.textsurface,(600,500))
        """
        pygame.display.flip()

if __name__ == '__main__':
    Nivel_Facil()
