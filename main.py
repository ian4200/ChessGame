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
from pygame import *
from time import sleep
from chessboard import drawBoard
pygame.init 

#image stuff https://pixabay.com/en/chess-queen-meeple-crown-black-36311/
whitequeen=pygame.image.load("finalProject/images/whitequeen.png")
blackqueen=pygame.image.load("finalProject/images/blackqueen.png")
#image calling

white=(255,255,255)
black=(50,50,50)
drawBoard()

# sleep(4)
#piece of code i took from https://stackoverflow.com/questions/19780411/pygame-drawing-a-rectangle
#checks and updates the screen so that things actually show up in pygame
# while True:
#     for event in pygame.event.get():
#         if event.type==QUIT:
#             pygame.quit()
#             sys.exit()
#         pygame.display.update()

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
player=1
pastmoves=[""]
listposition=0
def movepiece():
    global xposition
    global yposition
    global player
    global currentposition
    global piecemoveinput
    global listposition
    global pastmoves
    #erasePiece()
    piecexpos()
    pieceypos()
    if player==1:
        screen.blit(whitequeen,(xposition,yposition))
        player+=1
        currentposition = piecemoveinput
        pastmoves+=[currentposition]
        listposition+=1
        print(pastmoves)
        #currentposition1=currentposition
        #erasePiece()
    elif player==2:
        screen.blit(blackqueen,(xposition,yposition))
        player-=1
        currentposition = piecemoveinput
        pastmoves+=[currentposition]
        listposition+=1
        print(pastmoves)
        #currentposition2=currentposition
        #erasePiece()
    pygame.display.update()
    
def erasePiece():
    global piecemoveinput
    global currentposition
    global listposition
    global pastmoves

    pieceEraser = piecemoveinput
    piecemoveinput=pastmoves[(listposition-2)]
    if listposition==1 or listposition==2:
        pass
    else:
        piecexpos()
        pieceypos()
        diagonalhelp()
        if  (diagonalHelperX+diagonalHelperY)%2==1 :
            pygame.draw.rect(screen,black,(xposition,yposition,80,80))
            pygame.display.update()
        else:
            pygame.draw.rect(screen,white,(xposition,yposition,80,80)) 
            pygame.display.update()
        #piecemoveinput=pieceEraser

#getting x position on the chessboard from a user input of chess formula
def piecexpos():
    global xposition

    if piecemoveinput[0]=="a":
        xposition=0
        #print(xposition)
    if piecemoveinput[0]=="b":
        xposition=80
    elif piecemoveinput[0]=="c":
        xposition=160
    elif piecemoveinput[0]=="d":
        xposition=240
    elif piecemoveinput[0]=="e":
        xposition=320
    elif piecemoveinput[0]=="f":
        xposition=400 
    elif piecemoveinput[0]=="g":
        xposition=480
    elif piecemoveinput[0]=="h":
        xposition=560
#getting y position on the chessboard from a user input of chess formula
def pieceypos():
    global yposition
    if piecemoveinput[1]=="8":
        yposition=0
       # print(xposition)
    if piecemoveinput[1]=="7":
        yposition=80
    elif piecemoveinput[1]=="6":
        yposition=160
    elif piecemoveinput[1]=="5":
        yposition=240
    elif piecemoveinput[1]=="4":
        yposition=320
    elif piecemoveinput[1]=="3":
        yposition=400 
    elif piecemoveinput[1]=="2":
        yposition=480
    elif piecemoveinput[1]=="1":
        yposition=560

#changing a-h to 1-8 so i can use some math to be able to tell whether it is diagonal or not
global piecemoveinput
global currentpositon
curretnposition=""

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
    elif diagonalHelperX==2:
        flipHelperX=7
    elif diagonalHelperX==3:
        flipHelperX=6
    elif diagonalHelperX==4:
        flipHelperX=5
    elif diagonalHelperX==5:
        flipHelperX=4
    elif diagonalHelperX==6:
        flipHelperX=3
    elif diagonalHelperX==7:
        flipHelperX=2
    elif diagonalHelperX==8:
        flipHelperX=1
#same thing as above, but for current position
def currentPositionFlipper():
   # print("currentpositionflipper")
    global currentpositionflipHelperX
    if currentpositionDiagonalHelperX==1:
        currentpositionflipHelperX=8
    elif currentpositionDiagonalHelperX==2:
        currentpositionflipHelperX=7
    elif currentpositionDiagonalHelperX==3:
        currentpositionflipHelperX=6
    elif currentpositionDiagonalHelperX==4:
        currentpositionflipHelperX=5
    elif currentpositionDiagonalHelperX==5:
        currentpositionflipHelperX=4
    elif currentpositionDiagonalHelperX==6:
        currentpositionflipHelperX=3
    elif currentpositionDiagonalHelperX==7:
        currentpositionflipHelperX=2
    elif currentpositionDiagonalHelperX==8:
        currentpositionflipHelperX=1
#putting all of the functions above in one thing

#one giant class that lets me create pieces that can move around the board straight or diagonally
class Moves():
    def __init__(self, moves1,moves2, startPosition):
        global currentposition
        self.moves1=moves1
        self.moves2=moves2
        self.startPosition=startPosition
        currentposition=self.startPosition
    def moveOption(self):
        global currentposition
        global piecemoveinput
        #piecemoveinput=input("move piece")
        #print(listposition)
        #this uses the pastmoves list toget the position of the piece that didn't just move
        #doesn't effect the first 2 times though
        if listposition!=1 and listposition!=2 and listposition!=0:
            currentposition=pastmoves[listposition-1]
            #print(currentposition)
#if the moves are straight it goes through this conditional
        if self.moves1== "straight":
            #erasePiece()
#straight moves just check to see if the formula matches with one piece of current position
            if currentposition[0]==piecemoveinput[0] or  currentposition[1]==piecemoveinput[1]:
                movepiece()
                erasePiece()
        #if the piece can move both straight and diagonal it goes though here
            elif self.moves2== "diagonal":
                self.diagonalmover()
            else:
                print("Illegal move")
                self.playGame()
#if it is a bishop and can only move diagonal it goes though here
        elif self.moves2== "diagonal":
            self.diagonalmover()
        
    #putting all of the functions above in one thing
    def diagonalmover(self):
        global piecemoveinput
        global currentposition
        currentpositionhelper()
        diagonalhelp()
        flipdiagonalHelperX()
        currentPositionFlipper()
    # print (piecemoveinput)
    # print(currentposition)
        #erasePiece()
    #leveraging the fact that if you add the x y coordinates you get one number diagonally from there
        if (diagonalHelperX+diagonalHelperY)==(currentpositionDiagonalHelperY +currentpositionDiagonalHelperX) :
            movepiece()
            #print(diagonalHelperX+diagonalHelperY)
            #print(currentpositionDiagonalHelperY +currentpositionDiagonalHelperX)
            erasePiece()
        
    #flipping it to check the other diagonal
        elif (diagonalHelperX+diagonalHelperY)!=(currentpositionDiagonalHelperY +currentpositionDiagonalHelperX) and (flipHelperX+ diagonalHelperY)==(currentpositionflipHelperX+ currentpositionDiagonalHelperY):
            movepiece()
            #print(flipHelperX+ diagonalHelperY)
            #print(currentpositionflipHelperX+ currentpositionDiagonalHelperY)
            erasePiece()
            
    #if nothing works resets
        else:
            # print(flipHelperX+ diagonalHelperY)
            # print(currentpositionflipHelperX+ currentpositionDiagonalHelperY)
            # print(diagonalHelperX+diagonalHelperY)
            # print(currentpositionDiagonalHelperY +currentpositionDiagonalHelperX)
            print("illegal move")
            self.playGame() 
    def playGame(self):
        global piecemoveinput
        global player
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    piecemoveinput="a"        
                elif event.key == pygame.K_b:
                    piecemoveinput="b"
                elif event.key == pygame.K_c:
                    piecemoveinput="c"
                elif event.key == pygame.K_d:
                    piecemoveinput="d"
                elif event.key == pygame.K_e:
                    piecemoveinput="e"
                elif event.key == pygame.K_f:
                    piecemoveinput="f"
                elif event.key == pygame.K_g:
                    piecemoveinput="g"
                elif event.key == pygame.K_h:
                    piecemoveinput="h"
                elif event.key == pygame.K_1:
                    piecemoveinput=piecemoveinput+"1"
                    self.moveOption()
                elif event.key == pygame.K_2:
                    piecemoveinput=piecemoveinput+"2"
                    self.moveOption()
                elif event.key == pygame.K_3:
                    piecemoveinput=piecemoveinput+"3"
                    self.moveOption()
                elif event.key == pygame.K_4:
                    piecemoveinput=piecemoveinput+"4"
                    self.moveOption()
                elif event.key == pygame.K_5:
                    piecemoveinput=piecemoveinput+"5"
                    self.moveOption()
                elif event.key == pygame.K_6:
                    piecemoveinput=piecemoveinput+"6"
                    self.moveOption()
                elif event.key == pygame.K_7:
                    piecemoveinput=piecemoveinput+"7"
                    self.moveOption()
                elif event.key == pygame.K_8:
                    piecemoveinput=piecemoveinput+"8"
                    self.moveOption()
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            
   
            


# while True:
#     printBoard()
#     events = pygame.event.get()
#     for event in events:
#         print("yay")
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_a:
#                 piecemoveinput="a2"
#                 print(piecemoveinput)
#                 pygame.draw.rect(screen,white,(40,40,10,10))
#                 pygame.display.update()
                
#             elif event.key == pygame.K_b:
#                 piecemoveinput="b"

pawn=Moves("","diagonal", "a2")
rook=Moves("straight", "diagonal", "a1")
while True:
    rook.playGame()
    
