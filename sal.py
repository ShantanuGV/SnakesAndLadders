import pygame
import random
import time
import os

pygame.init()

screen = pygame.display.set_mode((700,570))
pygame.display.set_caption("🐍Snakes and 🖇Lader")

bimag=pygame.image.load("101692.jpg")
bordimag=pygame.image.load("100.png")

player_red=pygame.image.load("pin_red.png")
player_red=pygame.transform.scale(player_red, (30,30))
player_blue=pygame.image.load("pin_blue.png")
player_blue=pygame.transform.scale(player_blue, (30,30))

dice_1=pygame.image.load("dice_1.png")
dice_1=pygame.transform.scale(dice_1, (100,100))
dice_2=pygame.image.load("dice_2.png")
dice_2=pygame.transform.scale(dice_2, (100,100))
dice_3=pygame.image.load("dice_3.png")
dice_3=pygame.transform.scale(dice_3, (100,100))
dice_4=pygame.image.load("dice_4.png")
dice_4=pygame.transform.scale(dice_4, (100,100))
dice_5=pygame.image.load("dice_5.png")
dice_5=pygame.transform.scale(dice_5, (100,100))
dice_6=pygame.image.load("dice_6.png")
dice_6=pygame.transform.scale(dice_6, (100,100))

button_color = (255, 0, 0)
button_rect = pygame.Rect(500, 400, 100, 40)
font = pygame.font.Font(None, 30)

rx=10
ry=520
bx=35
by=520
dx=570
dy=20


def salgame():
    n=1
    screen.blit(bimag,(0,0))
    screen.blit(bordimag,(10,10))
    r_player()
    b_player()
    draw_button()
    i=0         
         


def r_player():
        screen.blit(player_red,(rx,ry))

def b_player():
        screen.blit(player_blue,(bx,by))

def roll_dice():
        dn=random.randint(1, 6)
        if dn<7 and dn>0:
                if dn == 1:
                    screen.blit(dice_1,(dx,dy))
                elif dn ==2:
                    screen.blit(dice_2,(dx,dy)) 
                elif dn == 3:
                    screen.blit(dice_1,(dx,dy))
                elif dn ==4:
                    screen.blit(dice_2,(dx,dy))
                elif dn == 5:
                    screen.blit(dice_1,(dx,dy))
                elif dn ==6:
                    screen.blit(dice_2,(dx,dy))

def draw_button():
    pygame.draw.rect(screen, button_color, button_rect)
    text = font.render("Roll Dice", True, (255, 255, 255))
    screen.blit(text, (button_rect.x + 10, button_rect.y + 10))                    

salgame()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                roll_dice()    

    salgame()
    pygame.display.update()

pygame.quit()

