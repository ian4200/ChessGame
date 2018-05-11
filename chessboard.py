#importing and intializing
import pygame, sys

from pygame import *

pygame.init 



#advice on rectangles from here https://stackoverflow.com/questions/19780411/pygame-drawing-a-rectangle

white=(255,255,255)
#black is actually gray to differntiate from the black pieces
black=(50,50,50)
screen=pygame.display.set_mode((640,640)) 
screen.fill(white)
#moves around creating black squares on a white background
#making a board

def drawBoard():
    board_x=0
    board_y=0
    count1=0
    while count1<32:    
        count2 = 0
        count3= 0
        while count2<4:
            pygame.draw.rect(screen,black,(board_x,board_y,80,80))
            board_x+=160
            count1+=1
            count2+=1
        board_x+=80
        board_y+=80
        pygame.draw.rect(screen,black,(board_x,board_y,80,80))
        while count3<4:
            board_x-=160
            pygame.draw.rect(screen,black,(board_x,board_y,80,80))
            count1+=1
            count3+=1
        board_x-=80
        board_y+=80
        pygame.draw.rect(screen,black,(board_x,board_y,80,80))
    pygame.display.update()
