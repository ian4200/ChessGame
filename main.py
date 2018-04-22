#created by Ian Bailey

# tyring to make a chess AI
#first thing is to make a working chess board and a piece or two, player controlled
#need to find out how to make the ai and work in pygame
#too ambitious in that it needs an ai
#possibly not ambitous enough b/c it is based on a known game

#my biggest thing is I don't know whether I can create the opponent

#importing and intializing
import pygame, sys
from pygame.locals import *
pygame.init 

#image calling
#wQimage= pygame.image.load("whitequeen.png")
#advice on rectangles from here https://stackoverflow.com/questions/19780411/pygame-drawing-a-rectangle

#making a board
white=(255,255,255)
black=(0,0,0)
screen=pygame.display.set_mode((640,640)) 
screen.fill(white)
board_x=0
board_y=0
count1=0

#moves around creating black squares on a white background
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
    


#funtctions to change an input of chess formula(ex. a1,b6, c4, etc) into positional coordinates on the board
global xposition
global yposition
global piecemoveinput
piecemoveinput=""


#creating a class to try to be able to move a piece
class ChessPiece():
    def __init__(self, whatever):
        self.whatever =whatever
    def piecemove(self):
        global xposition
        global yposition
        while True:
            piecemoveinput=input("Where do you want to  move the piece ")
            piecexpos()
            pieceypos()
            pygame.draw.rect(screen,white,(xposition,yposition,10,10))
            if piecemoveinput[0]=="q" or piecemoveinput[0]=="Q":
               break
#function to try to move a piece
#keep failing out of pygame though, maybe because processor, but i am not sure
def movepiece():
    while True:
        piecemoveinput=input("where do you want to move the piece ")
        xpositon=0
        yposition=0
        piecexpos()
        pieceypos()
        pygame.draw.rect(screen,white,(xposition,yposition,10,10))
        if piecemoveinput[0]=="q" or piecemoveinput[0]=="Q":
               break 
#getting x position on the chessboard from a user input of chess formula
def piecexpos():
    
    if piecemoveinput[0]=="a":
        xposition=40
        print(xposition)
    if piecemoveinput[0]=="b":
        xposition=120
    elif piecemoveinput[0]=="c":
        xposition=200
    elif piecemoveinput[0]=="d":
        xposition=280
    elif piecemoveinput[0]=="e":
        xposition=360
    elif piecemoveinput[0]=="f":
        xposition=440 
    elif piecemoveinput[0]=="g":
        xposition=520
    elif piecemoveinput[0]=="h":
        xposition=600
#getting y position on the chessboard from a user input of chess formula
def pieceypos():
    if piecemoveinput[1]=="8":
        yposition=40
        print(xposition)
    if piecemoveinput[1]=="7":
        yposition=120
    elif piecemoveinput[1]=="6":
        yposition=200
    elif piecemoveinput[1]=="5":
        yposition=280
    elif piecemoveinput[1]=="4":
        yposition=360
    elif piecemoveinput[1]=="3":
        yposition=440 
    elif piecemoveinput[1]=="2":
        yposition=520
    elif piecemoveinput[1]=="1":
        yposition=600
#changing a-h to 1-8 so i can use some math to be able to tell whether it is diagonal or not
diagonalHelperX=0
diagonalHelperY=0
def currentpostionhelper():
    currentpositionDiagonalHelperY= int(currentposition[1])
    if currentposition[0]== "a":
        currentpositionDiagonalHelperX=1
    elif currentposition[0]== "b":
        currentpositionDiagonalHelperX=2
    elif currentposition[0]== "c":
        currentpositionDiagonalHelperX=3
    elif currentposition[0]=="d":
        currentpositionDiagonalHelperX=4
    elif currentposition[0]== "e":
        currentpositionDiagonalHelperX=5
    elif currentposition[0]== "f":
        currentpositionDiagonalHelperX=6
    elif currentposition[0]== "g":
        currentpositionDiagonalHelperX=7
    elif currentposition[0]== "h":
        currentpositionDiagonalHelperX=8
def diagonalhelp():
    diagonalHelperY= int(piecemoveinput[1])
    if piecemoveinput[0]== "a":
        diagonalHelperX=1
    elif piecemoveinput[0]== "b":
        diagonalHelperX=2
    elif piecemoveinput[0]== "c":
        diagonalHelperX=3
    elif piecemoveinput[0]=="d":
        diagonalHelperX=4
    elif piecemoveinput[0]== "e":
        diagonalHelperX=5
    elif piecemoveinput[0]== "f":
        diagonalHelperX=6
    elif piecemoveinput[0]== "g":
        diagonalHelperX=7
    elif piecemoveinput[0]== "h":
        diagonalHelperX=8
    else:
        print("what are you doing!?!?!?!")
def flipdiagonalHelperX():
    if diagonalHelperX=1:
        flipHelperX=8
    if diagonalHelperX=2:
        flipHelperX=7
    if diagonalHelperX=3:
        flipHelperX=6
    if diagonalHelperX=4:
        flipHelperX=5
    if diagonalHelperX=5:
        flipHelperX=4
    if diagonalHelperX=6:
        flipHelperX=3
    if diagonalHelperX=7:
        flipHelperX=2
    if diagonalHelperX=8:
        flipHelperX=1
def flipdiagonalHelperY():
    if diagonalHelperY=1:
        flipHelperY=8
    if diagonalHelperY=2:
        flipHelperY=7
    if diagonalHelperY=3:
        flipHelperY=6
    if diagonalHelperY=4:
        flipHelperY=5
    if diagonalHelperY=5:
        flipHelperY=4
    if diagonalHelperY=6:
        flipHelperY=3
    if diagonalHelperY=7:
        flipHelperY=2
    if diagonalHelperY=8:
        flipHelperY=1

def diagonalmover():
    diagonalhelp()
    flipdiagonalhelper()
    currentpostionhelper()
    if (diagonalhelperX+diagonalHelperY)==(currentpositionDiagonalHelperX+ currentpositionDiagonalHelperY) :
         movepiece()
        break
    elif (flipdiagonalHelperX+flipdiagonalHelperY)==(currentpositionDiagonalHelperX+ currentpositionDiagonalHelperY):
        movepiece()
        break
    else:
        print("illegal move")
        piecemoveinput=input("Pick a move to a legal postion ")
        diagonalmover()

movenumber=0
while movenumber<50:
    piecemoveinput=input("Where do you want to  move the piece ")
    xposition=0
    yposition=0
    piecexpos()
    pieceypos()
    pygame.draw.rect(screen,black,(xposition,yposition,10,10))
    pygame.display.update()
    movenumber+=1
    if piecemoveinput[0]=="q" or piecemoveinput[0]=="Q":
        break
#piece of code i took from https://stackoverflow.com/questions/19780411/pygame-drawing-a-rectangle
#checks and updates the screen so that things actually show up in pygame
for event in pygame.event.get():
    if event.type==QUIT:
        pygame.quit()
        sys.exit()
def diagonalmover():
    diagonalhelp()
    flipdiagonalhelper()
    currentpostionhelper()
    if (diagonalhelperX+diagonalHelperY)==(currentpositionDiagonalHelperX+ currentpositionDiagonalHelperY) :
         movepiece()
        break
    elif (flipdiagonalHelperX+flipdiagonalHelperY)==(currentpositionDiagonalHelperX+ currentpositionDiagonalHelperY):
        movepiece()
        break
    else:
        print("illegal move")
        piecemoveinput=input("Pick a move to a legal postion ")
        diagonalmover()

class Moves():
    def __init__(self, moves1,moves2):
        self.moves1=moves1
        self.moves2=moves2
    def moveOption():
        if self.moves1== "straight":
            while True:
                if currentposition[0]==piecemoveinput[0] or  currentposition[1]==piecemoveinput[1]:
                    movepiece()
                    break
                else:
                    print("Illegal move")
                    piecemoveinput=input("Pick a move to a legal postion ")
        if self.moves1== "diagonal":
            diagonalmover()
        moveOption()
