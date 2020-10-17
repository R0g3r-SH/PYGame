import random
from typing import Text
import pygame
from pygame import surface
from pygame import font
# globals
pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
DICE_NUMBER = 5
TURN=''



FIRST_DICE = 0
SECOND_DICE = 0
F4RT_DICE = 0
TRD_DICE = 0
F5FT_DICE = 0

# ---->P2<-----
P2_FIRST_DICE = 0
P2_SECOND_DICE = 0
P2_F4RT_DICE = 0
P2_TRD_DICE = 0
P2_F5FT_DICE = 0


# Defines colours (not built in)
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
START = False

CONT = 0

gameDisplay = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
clock = pygame.time.Clock()
already_rolled = False

# Import Images for Dice 1-6
dice_1 = pygame.image.load("Dice_1.png")
dice_2 = pygame.image.load("Dice_2.png")
dice_3 = pygame.image.load("Dice_3.png")
dice_4 = pygame.image.load("Dice_4.png")
dice_5 = pygame.image.load("Dice_5.png")
dice_6 = pygame.image.load("Dice_6.png")
gameDisplay.blit(dice_1, (SCREEN_WIDTH/4, 0))

def draw_pointsP1(surface,text,size,x,y):
    font=pygame.font.SysFont("serif",size)
    text_suirface= font.render(text,True,white)
    text_rect= text_suirface.get_rect()
    text_rect=(x, y)
    surface.blit(text_suirface, text_rect)

def roll_a_dice():
    dice = random.randrange(1, 6)
    return dice


def roll_a_dice2():
    dice = random.randrange(1, 6)
    return dice


def display_dice(first, second, trd, f4rt, f5ft):
    display_first(first)
    display_second(second)
    display_trd(trd)
    display_f4rt(f4rt)
    display_f5ft(f5ft)


def p2display_dice(first_2, second_2, trd_2, f4rt_2, f5ft_2):
    display_first_2(first_2)
    display_second_2(second_2)
    display_trd_2(trd_2)
    display_f4rt_2(f4rt_2)
    display_f5ft_2(f5ft_2)


# determines which first dice is used


def display_first(first):
    if (first == 1):
        gameDisplay.blit(dice_1, (30, 10))
    elif (first == 2):
        gameDisplay.blit(dice_2, (30, 10))
    elif (first == 3):
        gameDisplay.blit(dice_3, (30, 10))
    elif (first == 4):
        gameDisplay.blit(dice_4, (30, 10))
    elif (first == 5):
        gameDisplay.blit(dice_5, (30, 10))
    elif (first == 6):
        gameDisplay.blit(dice_6, (30, 10))

# determines which second dice is used
def display_second(second):
    if (second == 1):
        gameDisplay.blit(dice_1, (120, 10))
    elif (second == 2):
        gameDisplay.blit(dice_2, (120, 10))
    elif (second == 3):
        gameDisplay.blit(dice_3, (120, 10))
    elif (second == 4):
        gameDisplay.blit(dice_4, (120, 10))
    elif (second == 5):
        gameDisplay.blit(dice_5, (120, 10))
    elif (second == 6):
        gameDisplay.blit(dice_6, (120, 10))


def display_trd(trd):
    if (trd == 1):
        gameDisplay.blit(dice_1, (210, 10))
    elif (trd == 2):
        gameDisplay.blit(dice_2, (210, 10))
    elif (trd == 3):
        gameDisplay.blit(dice_3, (210, 10))
    elif (trd == 4):
        gameDisplay.blit(dice_4, (210, 10))
    elif (trd == 5):
        gameDisplay.blit(dice_5, (210, 10))
    elif (trd == 6):
        gameDisplay.blit(dice_6, (210, 10))


def display_f4rt(f4rt):
    if (f4rt == 1):
        gameDisplay.blit(dice_1, (300, 10))
    elif (f4rt == 2):
        gameDisplay.blit(dice_2, (300, 10))
    elif (f4rt == 3):
        gameDisplay.blit(dice_3, (300, 10))
    elif (f4rt == 4):
        gameDisplay.blit(dice_4, (300, 10))
    elif (f4rt == 5):
        gameDisplay.blit(dice_5, (300, 10))
    elif (f4rt == 6):
        gameDisplay.blit(dice_6, (300, 10))


def display_f5ft(f5ft):
    if (f5ft == 1):
        gameDisplay.blit(dice_1, (390, 10))
    elif (f5ft == 2):
        gameDisplay.blit(dice_2, (390, 10))
    elif (f5ft == 3):
        gameDisplay.blit(dice_3, (390, 10))
    elif (f5ft == 4):
        gameDisplay.blit(dice_4, (390, 10))
    elif (f5ft == 5):
        gameDisplay.blit(dice_5, (390, 10))
    elif (f5ft == 6):
        gameDisplay.blit(dice_6, (400, 10))

# ->>>>>>>-----PLAYER 2 <_-----------------


def display_first_2(first_2):
    if (first_2 == 1):
        gameDisplay.blit(dice_1, (30, 110))
    elif (first_2 == 2):
        gameDisplay.blit(dice_2, (30, 110))
    elif (first_2 == 3):
        gameDisplay.blit(dice_3, (30, 110))
    elif (first_2 == 4):
        gameDisplay.blit(dice_4, (30, 110))
    elif (first_2 == 5):
        gameDisplay.blit(dice_5, (30, 110))
    elif (first_2 == 6):
        gameDisplay.blit(dice_6, (30, 110))
# determines which second dice is used

def display_second_2(second_2):
    if (second_2 == 1):
        gameDisplay.blit(dice_1, (120, 110))
    elif (second_2 == 2):
        gameDisplay.blit(dice_2, (120, 110))
    elif (second_2 == 3):
        gameDisplay.blit(dice_3, (120, 110))
    elif (second_2 == 4):
        gameDisplay.blit(dice_4, (120, 110))
    elif (second_2 == 5):
        gameDisplay.blit(dice_5, (120, 110))
    elif (second_2 == 6):
        gameDisplay.blit(dice_6, (120, 110))


def display_trd_2(trd_2):
    if (trd_2 == 1):
        gameDisplay.blit(dice_1, (210, 110))
    elif (trd_2 == 2):
        gameDisplay.blit(dice_2, (210, 110))
    elif (trd_2 == 3):
        gameDisplay.blit(dice_3, (210, 110))
    elif (trd_2 == 4):
        gameDisplay.blit(dice_4, (210, 110))
    elif (trd_2 == 5):
        gameDisplay.blit(dice_5, (210, 110))
    elif (trd_2 == 6):
        gameDisplay.blit(dice_6, (210, 110))


def display_f4rt_2(f4rt_2):
    if (f4rt_2 == 1):
        gameDisplay.blit(dice_1, (300, 110))
    elif (f4rt_2 == 2):
        gameDisplay.blit(dice_2, (300, 110))
    elif (f4rt_2 == 3):
        gameDisplay.blit(dice_3, (300, 110))
    elif (f4rt_2 == 4):
        gameDisplay.blit(dice_4, (300, 110))
    elif (f4rt_2 == 5):
        gameDisplay.blit(dice_5, (300, 110))
    elif (f4rt_2 == 6):
        gameDisplay.blit(dice_6, (300, 10))


def display_f5ft_2(f5ft_2):
    if (f5ft_2 == 1):
        gameDisplay.blit(dice_1, (390, 110))
    elif (f5ft_2 == 2):
        gameDisplay.blit(dice_2, (390, 110))
    elif (f5ft_2 == 3):
        gameDisplay.blit(dice_3, (390, 110))
    elif (f5ft_2 == 4):
        gameDisplay.blit(dice_4, (390, 110))
    elif (f5ft_2 == 5):
        gameDisplay.blit(dice_5, (390, 110))
    elif (f5ft_2 == 6):
        gameDisplay.blit(dice_6, (400, 110))


# tells the user how to roll
def produce_button_message(text):
    our_font = pygame.font.SysFont("monospace", 15)
    # render the text now
    produce_text = our_font.render(text, 1, black)
    gameDisplay.blit(produce_text, (SCREEN_WIDTH/8, SCREEN_HEIGHT/5))

# produce the roll results (in text)


def produce_roll_message(text):
    our_font = pygame.font.SysFont("monospace", 15)
    # render the text now. 1 refers to aliasing.
    produce_text = our_font.render(text, 1, white)
    gameDisplay.blit(produce_text, (50, 345))


def produce_roll_message_P2(text_P2):
    our_font = pygame.font.SysFont("monospace", 15)
    # render the text now. 1 refers to aliasing.
    produce_text = our_font.render(text_P2, 1, white)
    gameDisplay.blit(produce_text, (50, 350))


# our roll will display message with our roll converted to text form, alongside
def roll():
    # Completed roll Message. Cast int to str to output the message clearly
    text = " P1 ->> You've completed your roll " + str(FIRST_DICE) + "," + str(
        SECOND_DICE) + "," + str(TRD_DICE) + "," + str(F4RT_DICE) + "," + str(F5FT_DICE)

    #print(text)
    produce_roll_message(text)
    


def roll_p2():
    text = " P2 ->> You've completed your roll " + str(P2_FIRST_DICE) + "," + str(
        P2_SECOND_DICE) + "," + str(P2_TRD_DICE) + "," + str(P2_F4RT_DICE) + "," + str(P2_F5FT_DICE)
    #print(text)
    produce_roll_message_P2(text)







# We don't want our roll value output before the first roll occurs.


def getPairs_and_Index(array):
    xd=array.copy()
    potentialPair = []
    indexes = {}
    pairs = []
    for i in range(len(array)):
        if array[i] not in indexes.keys():
            indexes.setdefault(array[i], i)
        elif array[i] in indexes.keys() and array[i] not in potentialPair:
            pairs.append([indexes[array[i]], i])
            potentialPair.append(array[i])
        elif array[i]  in indexes.keys() and array[i] in potentialPair:
            return False
    if len(pairs):
        print(xd, pairs)
        print("ARRAYS:", pairs[0])
        return pairs[0]
    return False

def re_roll(array, pairs):
    global FIRST_DICE
    global SECOND_DICE
    global TRD_DICE
    global F4RT_DICE
    global F5FT_DICE
    if pairs == False:
        return
    for i in range(len(array)):
        if i not in pairs:
            if i == 0:
                FIRST_DICE = roll_a_dice()
            elif i == 1:
                SECOND_DICE = roll_a_dice()
            elif i == 2: 
                TRD_DICE = roll_a_dice()
            elif i == 3:
                F4RT_DICE = roll_a_dice()
            else:
                F5FT_DICE = roll_a_dice()
            array[i] = roll_a_dice()

def re_roll2(array, pairs):
    global P2_FIRST_DICE
    global P2_SECOND_DICE
    global P2_TRD_DICE
    global P2_F4RT_DICE
    global P2_F5FT_DICE
    if pairs == False:
        return
    for i in range(len(array)):
        if i not in pairs:
            if i == 0:
                P2_FIRST_DICE = roll_a_dice()
            elif i == 1:
                P2_SECOND_DICE = roll_a_dice()
            elif i == 2: 
                P2_TRD_DICE = roll_a_dice()
            elif i == 3:
                P2_F4RT_DICE = roll_a_dice()
            else:
                P2_F5FT_DICE = roll_a_dice()
            array[i] = roll_a_dice()

def addPoints1(array):
    global P1_POINTS
    one=array.count(1)
    two=array.count(2)
    three=array.count(3)
    four=array.count(4)
    five=array.count(5)
    six=array.count(6)
    if(one==3 or two==3 or three==3 or four==3 or five==3 or six==3):
        P1_POINTS+=3
        print(P1_POINTS)
    if(one==4 or two==4 or three==4 or four==4 or five==4 or six==4):
        P1_POINTS+=6
        print(P1_POINTS)
    if(one==5 or two==5 or three==5 or four==5 or five==5 or six==5):
        P1_POINTS+=12
        print(P1_POINTS)

def addPoints2(array):
    global P2_POINTS
    one=array.count(1)
    two=array.count(2)
    three=array.count(3)
    four=array.count(4)
    five=array.count(5)
    six=array.count(6)
    if(one==3 or two==3 or three==3 or four==3 or five==3 or six==3):
        P2_POINTS+=3
        print(P2_POINTS)
    if(one==4 or two==4 or three==4 or four==4 or five==4 or six==4):
        P2_POINTS+=6
        print(P2_POINTS)
    if(one==5 or two==5 or three==5 or four==5 or five==5 or six==5):
        P2_POINTS+=12
        print(P2_POINTS)



menu = True
RONDA=0
P1_POINTS=0
P1_info=""
P1_2Dados=False
P2_2Dados=False
P2_POINTS=0



# main loop
def main():
    global CONT
    global FIRST_DICE
    global SECOND_DICE
    global TRD_DICE
    global F4RT_DICE
    global F5FT_DICE
    global P2_FIRST_DICE
    global P2_SECOND_DICE
    global P2_TRD_DICE
    global P2_F4RT_DICE
    global P2_F5FT_DICE
    global already_rolled
    global menu
    global RONDA
    global P1_POINTS
    global P1_info
    global P1_2Dados
    global P2_2Dados
    global P2_POINTS
    roll_occur = False
    roll_occur_p2 = False

    Turn = True

    dta = []
    dta2 = []

    while already_rolled == False:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                already_rolled = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                    if Turn == True:
                        RONDA += 1

                        #cuando dos Dados son iguales 
                        if isinstance(P1_2Dados, list): # Segundo tiro
                            re_roll(dta, P1_2Dados)
                            one=dta.count(1)
                            two=dta.count(2)
                            three=dta.count(3)
                            four=dta.count(4)
                            five=dta.count(5)
                            six = dta.count(6)
                            roll_occur = True
                            roll_occur_p2 = False
                            P1_2Dados=False
                            Turn = False
                            if not (one >= 3 or two >= 3 or three >= 3 or four >= 3 or five >= 3 or six >= 3):
                                continue
                            addPoints1(dta)
                            
                            
                        elif P1_2Dados == False: # Primer tiro
                            FIRST_DICE = roll_a_dice()
                            SECOND_DICE = roll_a_dice()
                            TRD_DICE = roll_a_dice()
                            F4RT_DICE = roll_a_dice()
                            F5FT_DICE = roll_a_dice()
                            dta=[FIRST_DICE,SECOND_DICE,TRD_DICE,F4RT_DICE,F5FT_DICE]
                            addPoints1(dta)
                            P1_2Dados = getPairs_and_Index(dta)
                            one=dta.count(1)
                            two=dta.count(2)
                            three=dta.count(3)
                            four=dta.count(4)
                            five=dta.count(5)
                            six = dta.count(6)
                            roll_occur = True
                            roll_occur_p2 = False
                            if len(dta) == len(set(dta)) or (one >= 3 or two >= 3 or three >= 3 or four >= 3 or five >= 3 or six >= 3):
                                Turn = False
                                continue
                    else:

                        if isinstance(P2_2Dados, list): #Segundo tiro
                            re_roll2(dta2, P2_2Dados)
                            one=dta2.count(1)
                            two=dta2.count(2)
                            three=dta2.count(3)
                            four=dta2.count(4)
                            five=dta2.count(5)
                            six = dta2.count(6)
                            roll_occur_p2 = True
                            roll_occur = False
                            P2_2Dados = False
                            Turn = True
                            if not (one >= 3 or two >= 3 or three >= 3 or four >= 3 or five >= 3 or six >= 3):
                                    continue
                            addPoints2(dta2)

                        elif P2_2Dados == False: #Primer tiro
                            P2_FIRST_DICE = roll_a_dice2()
                            P2_SECOND_DICE = roll_a_dice2()
                            P2_TRD_DICE = roll_a_dice2()
                            P2_F4RT_DICE = roll_a_dice2()
                            P2_F5FT_DICE = roll_a_dice2()
                            dta2=[P2_FIRST_DICE,P2_SECOND_DICE,P2_TRD_DICE,P2_F4RT_DICE,P2_F5FT_DICE]
                            addPoints2(dta2)
                            P2_2Dados = getPairs_and_Index(dta2)
                            one=dta2.count(1)
                            two=dta2.count(2)
                            three=dta2.count(3)
                            four=dta2.count(4)
                            five=dta2.count(5)
                            six = dta2.count(6)
                            roll_occur_p2 = True
                            roll_occur = False
                            if len(dta2) == len(set(dta2)) or (one >= 3 or two >= 3 or three >= 3 or four >= 3 or five >= 3 or six >= 3):
                                Turn = True
                                continue
                        

        gameDisplay.fill(black)
        display_dice(FIRST_DICE, SECOND_DICE, TRD_DICE, F4RT_DICE, F5FT_DICE)
        p2display_dice(P2_FIRST_DICE, P2_SECOND_DICE,
                    P2_TRD_DICE, P2_F4RT_DICE, P2_F5FT_DICE)
        # If the roll is requested, our_roll will execute.
        while CONT==0:
            P2_FIRST_DICE = roll_a_dice2()
            P2_SECOND_DICE = roll_a_dice2()
            P2_TRD_DICE = roll_a_dice2()
            P2_F4RT_DICE = roll_a_dice2()
            P2_F5FT_DICE = roll_a_dice2()
            FIRST_DICE = roll_a_dice()
            SECOND_DICE = roll_a_dice()
            TRD_DICE = roll_a_dice()
            F4RT_DICE = roll_a_dice()
            F5FT_DICE = roll_a_dice()
            CONT+=1

        draw_pointsP1(gameDisplay,('>> SCORE P1: '+str(P1_POINTS)),25,550,100)

        if (roll_occur):
            roll()
        if (roll_occur_p2):
            roll_p2()

        pygame.display.update()
        clock.tick(30)

    # Once the loop exits, the program will quit.
    # Loop will exit when the 'Exit' button on the window is clicked.This bit of code just ensures you can actually
    # click that and exit.
    pygame.quit()
    quit()


main()
