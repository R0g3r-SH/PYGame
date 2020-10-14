import pygame,sys
import random

class Player (pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.sprites=[]
        self.is_animating=False
        self.sprites.append(pygame.image.load('Dice_1.png'))
        self.sprites.append(pygame.image.load('Dice_2.png'))
        self.sprites.append(pygame.image.load('Dice_3.png'))
        self.sprites.append(pygame.image.load('Dice_4.png'))
        self.sprites.append(pygame.image.load('Dice_5.png'))
        self.sprites.append(pygame.image.load('Dice_6.png'))

        self.current_sprite=0
        self.image =self.sprites[self.current_sprite]

        self.rect=self.image.get_rect()
        self.rect.topleft =[pos_x,pos_y]

    def animate(self):
        self.is_animating= True


    def update(self):
        if self.is_animating == True:
            self.current_sprite += 0.2
            
            if self.current_sprite >= len(self.sprites):
                self.current_sprite=0
                self.is_animating=False
            dice = random.randint(0,5)
            self.image=self.sprites[int(dice)]


pygame.init()
clock=pygame.time.Clock()


#gameScreen
screen_width=800
screen_heigth=400
background_colour = (255,255,255)

screen= pygame.display.set_mode((screen_width,screen_heigth))

pygame.display.flip()
pygame.display.set_caption('SPRITE aNIMATION')



#creating sprites ando groups
moving_sprites=pygame.sprite.Group()
player=Player(100,100)
moving_sprites.add(player)

while True:
    for event in pygame.event.get():

        if event.type  == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            player.animate()


    color = (0, 0, 0) 
    screen.fill(color)
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()
    clock.tick(60)