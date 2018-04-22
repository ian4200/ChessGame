global piecemoveinput
global currentpositon
def movepiece():
    print("piece moved")

def currentpositionhelper():
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
def diagonalhelp():
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
def flipdiagonalHelperX():
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
def currentPositionFlipper():
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

def diagonalmover():
    
    currentpositionhelper()
    diagonalhelp()
    flipdiagonalHelperX()
    currentPositionFlipper()
    
    if (diagonalHelperX+diagonalHelperY)==(currentpositionDiagonalHelperY +currentpositionDiagonalHelperX) :
        movepiece()
        print(diagonalHelperX+diagonalHelperY)
        print(currentpositionDiagonalHelperY +currentpositionDiagonalHelperX)
        piecemoveinput=input("Pick a move1 ")
        #break
    elif (diagonalHelperX+diagonalHelperY)!=(currentpositionDiagonalHelperY +currentpositionDiagonalHelperX) and (flipHelperX+ diagonalHelperY)==(currentpositionflipHelperX+ currentpositionDiagonalHelperY):
        movepiece()
        print(flipHelperX+ diagonalHelperY)
        print(currentpositionflipHelperX+ currentpositionDiagonalHelperY)
        piecemoveinput=input("Pick a move2 ")
        #break
    
    else:
        print(flipHelperX+ diagonalHelperY)
        print(currentpositionflipHelperX+ currentpositionDiagonalHelperY)
        print(diagonalHelperX+diagonalHelperY)
        print(currentpositionDiagonalHelperY +currentpositionDiagonalHelperX)
        print("illegal move")
        piecemoveinput=input("Pick a move to a legal postion1 ")
    diagonalmover()

currentposition="a1"
piecemoveinput="b2"
class Moves():
    def __init__(self, moves1,moves2):
        self.moves1=moves1
        self.moves2=moves2
    def moveOption(self):
        if self.moves1== "straight":
            global piecemoveinput
            while True:
                if currentposition[0]==piecemoveinput[0] or  currentposition[1]==piecemoveinput[1]:
                    movepiece()
                    break
                else:
                    print("Illegal move")
                    piecemoveinput=input("Pick a move to a legal postion ")
        if self.moves1== "diagonal":
            diagonalmover()
        currentposition = piecemoveinput
        piecemoveinput=input("move piece")
        self.moveOption()
diagonalmover()
