import pygame
import time
import random
from pygame.locals import *
pygame.init()
red = (155,0,0)
blue =(51,153,255)
grey =(192,192,192)
snake = (51,102,0)



win_width = 600 
win_height = 400
window = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption("Snake Game")
time.sleep(2)

snake = 10 
snake_speed = 15 
font_style =pygame.font.SysFont("calibir",26)
score_font = pygame.font.SysFont("comicsansms",30)

def score_user(score):
    number = score_font_render("Score",score,True,red)
    window.blit(number,[0,0])
#score_user(12)
def game_snake():
    pass 

def messgae():
    msg = font_style.render(msg,True,red)
    window.blit(msg,[win_width/6,win_height/3])
def game_loop():
    gameOver = False
    GameClose = False 

    x1 = win_width/2
    y1 = win_height/2

    x1_change = 0
    y1_change = 0

    snake_length_list=[]
    snake_length = 1

    foodx= round(random.randrange(0,win_width - snake)/10.0)*10.0
    foody = round(random.randrange(0,win_height - snake)/10.0)*10.0

    while not gameOver:
        while GameClose == True :
            window.fill(grey)
            message("You lost!press P to play again and Q to quit the game ")
            score_user(snake_length-1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN :
                    if event.key ==pygame.K_q:
                        gameOver == True
                        GameClose == True 
                    if event.key == pygame.K_p:
                        game_loop()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN :
            if event.key == K.LEFT :
                x1_change = -snake
                y1_change = 0
            if event.key == K_RIGHT :
                x1_change = snake
                y1_chang = 0
            if event.key ==K_UP :
                x1_change = 0
                y1_change =-snake
            if event.key == K_DOWN:
                x1_change = 0
                y1_change = snake

'''font = pygame.font.get_fonts()
print(font)'''
