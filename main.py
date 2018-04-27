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
#piece of code i took from https://stackoverflow.com/questions/19780411/pygame-drawing-a-rectangle
#checks and updates the screen so that things actually show up in pygame
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()




global piecemoveinput



#creating a class to try to be able to move a piece
# gving up on this for now, using function instead
# class ChessPiece():
#     def __init__(self, whatever):
#         self.whatever =whatever
#     def piecemove(self):
#         global xposition
#         global yposition
#         while True:
#             piecemoveinput=input("Where do you want to  move the piece ")
#             piecexpos()
#             pieceypos()
#             pygame.draw.rect(screen,white,(xposition,yposition,10,10))
#             if piecemoveinput[0]=="q" or piecemoveinput[0]=="Q":
#                break
#function to try to move a piece
#keep failing out of pygame though, maybe because processor, but i am not sure
def movepiece():
    while True:
        global xposition
        global yposition
        piecexpos()
        pieceypos()
        pygame.draw.rect(screen,white,(xposition,yposition,10,10))
        if piecemoveinput[0]=="q" or piecemoveinput[0]=="Q":
               break 
#getting x position on the chessboard from a user input of chess formula
def piecexpos():
    
    if piecemoveinput[0]=="a":
        xposition=40
        #print(xposition)
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
       # print(xposition)
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
global piecemoveinput
global currentpositon
currentposition="a1"
piecemoveinput=input("move piece ")
#changes chess formula to numbers i can use
def currentpositionhelper():
   # print("current position helper")
    global currentpositionDiagonalHelperY
    global currentpositionDiagonalHelperX
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
#changes your input in chess formula to numbers
def diagonalhelp():
   # print("diagonal help")
    global diagonalHelperX
    global diagonalHelperY
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
#flips the numbering on the x side in order to leverage a method of 
# checking if diagonal moves are legal. More on that later.
def flipdiagonalHelperX():
   # print("flipdiagonalhelperX")
    global flipHelperX
    if diagonalHelperX==1:
        flipHelperX=8
    if diagonalHelperX==2:
        flipHelperX=7
    if diagonalHelperX==3:
        flipHelperX=6
    if diagonalHelperX==4:
        flipHelperX=5
    if diagonalHelperX==5:
        flipHelperX=4
    if diagonalHelperX==6:
        flipHelperX=3
    if diagonalHelperX==7:
        flipHelperX=2
    if diagonalHelperX==8:
        flipHelperX=1
#same thing as above, but for current position
def currentPositionFlipper():
   # print("currentpositionflipper")
    global currentpositionflipHelperX
    if currentpositionDiagonalHelperX==1:
        currentpositionflipHelperX=8
    if currentpositionDiagonalHelperX==2:
        currentpositionflipHelperX=7
    if currentpositionDiagonalHelperX==3:
        currentpositionflipHelperX=6
    if currentpositionDiagonalHelperX==4:
        currentpositionflipHelperX=5
    if currentpositionDiagonalHelperX==5:
        currentpositionflipHelperX=4
    if currentpositionDiagonalHelperX==6:
        currentpositionflipHelperX=3
    if currentpositionDiagonalHelperX==7:
        currentpositionflipHelperX=2
    if currentpositionDiagonalHelperX==8:
        currentpositionflipHelperX=1
#putting all of the functions above in one thing
def diagonalmover():
    global piecemoveinput
    global currentposition
    currentpositionhelper()
    diagonalhelp()
    flipdiagonalHelperX()
    currentPositionFlipper()
   # print (piecemoveinput)
   # print(currentposition)

#leveraging the fact that if you add the x y coordinates you get one number diagonally from there
    if (diagonalHelperX+diagonalHelperY)==(currentpositionDiagonalHelperY +currentpositionDiagonalHelperX) :
        movepiece()
        #print(diagonalHelperX+diagonalHelperY)
        #print(currentpositionDiagonalHelperY +currentpositionDiagonalHelperX)
        currentposition=piecemoveinput
        piecemoveinput=input("Pick a move1 ")
#flipping it to check the other diagonal
    elif (diagonalHelperX+diagonalHelperY)!=(currentpositionDiagonalHelperY +currentpositionDiagonalHelperX) and (flipHelperX+ diagonalHelperY)==(currentpositionflipHelperX+ currentpositionDiagonalHelperY):
        movepiece()
        #print(flipHelperX+ diagonalHelperY)
        #print(currentpositionflipHelperX+ currentpositionDiagonalHelperY)
        currentposition=piecemoveinput
        piecemoveinput=input("Pick a move2 ")
        
#if nothing works resets
    else:
        # print(flipHelperX+ diagonalHelperY)
        # print(currentpositionflipHelperX+ currentpositionDiagonalHelperY)
        # print(diagonalHelperX+diagonalHelperY)
        # print(currentpositionDiagonalHelperY +currentpositionDiagonalHelperX)
        print("illegal move")
        piecemoveinput=input("Pick a move to a legal postion1 ")
    diagonalmover()

#class with the move options
class Moves():
    def __init__(self, moves1,moves2):
        self.moves1=moves1
        self.moves2=moves2
    def moveOption(self):
        if self.moves1== "straight":
            global piecemoveinput
            while True:
#straight moves just check to see if the formula matches with one piece of current position
                if currentposition[0]==piecemoveinput[0] or  currentposition[1]==piecemoveinput[1]:
                    movepiece()
                    break
                else:
                    print("Illegal move")
                    piecemoveinput=input("Pick a move to a legal postion ")
        if self.moves2== "diagonal":
            diagonalmover()
        currentposition = piecemoveinput
        piecemoveinput=input("move piece")
        self.moveOption()

