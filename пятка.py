from tkinter import Tk, Canvas
from random import shuffle

BOARDSIZE = 4
SQUARESIZE = 80
EMPTYSQUARE = BOARDSIZE ** 2

board = list(range(1,EMPTYSQUARE + 1))
CorrectBoard = board[:]

shuffle(board)

root = Tk()
root.title("Павел Шардин 21ИСС1") 
c = Canvas(root, width = BOARDSIZE * SQUARESIZE,
           height = BOARDSIZE * SQUARESIZE, 
            bg = '#808080')

c.pack()


def drawboard():
    c.delete('all')
    for i in range(BOARDSIZE):
        for j in range(BOARDSIZE):
            index = str(board[BOARDSIZE * i + j])
            if index != str(EMPTYSQUARE):
                c.create_rectangle(j * SQUARESIZE,
                                   i * SQUARESIZE,
                                   j * SQUARESIZE + SQUARESIZE,
                                   i * SQUARESIZE + SQUARESIZE,
                                   fill = '#43ABC9',
                                   outline = '#FFFFFF')
                c.create_text(j * SQUARESIZE + SQUARESIZE // 2,
                                   i * SQUARESIZE + SQUARESIZE // 2,
                                   text = index,
                                   font="Arial {} italic".format(int(SQUARESIZE // 4)),
                                   fill = '#FFFFFF')
                      
def click(event):
    x, y = event.x, event.y
    x = x // SQUARESIZE
    y = y // SQUARESIZE
    BoardIndex = x + (y * BOARDSIZE)
    EmptyIndex = GetEmptyNeighbor(BoardIndex)
    board[BoardIndex], board[EmptyIndex] = board[EmptyIndex], board[BoardIndex]
    drawboard()
    if board == CorrectBoard:
        ShowVictoryPlate()
        
def GetEmptyNeighbor(index):
    EmptyIndex = board.index(EMPTYSQUARE)
    ABSValue = abs(EmptyIndex - index)
    if ABSValue == BOARDSIZE:
        return EmptyIndex
    elif ABSValue == 1:
        MaxIndex = max(index, EmptyIndex)
        if MaxIndex % BOARDSIZE != 0:
            return EmptyIndex
    return index
    
def ShowVictoryPlate():
    c.create_rectangle(SQUARESIZE // 5,
                       SQUARESIZE * BOARDSIZE // 2 - 10 * BOARDSIZE,
                       BOARDSIZE * SQUARESIZE - SQUARESIZE // 5,
                       SQUARESIZE * BOARDSIZE // 2 + 10 * BOARDSIZE,
                       fill = '#000000',
                       outline='#FFFFFF')
    c.create_text(SQUARESIZE * BOARDSIZE // 2, 
                  SQUARESIZE * BOARDSIZE // 1.9, 
                  text="WIN!", 
                  font="Helvetica {} bold".format(int(10 * BOARDSIZE)), fill='#DC143C')
def GetInvCount():
    inversions = 0
    InversionBoard = board[:]
    InversionBoard.remove(EMPTYSQUARE)
    for i in range(len(InversionBoard)):
        FirstItem = InversionBoard[i]
        for j in range(i+1, len(InversionBoard)):
            SecondItem = InversionBoard[j]
            if FirstItem > SecondItem:
                inversions += 1
    print(inversions)
    return inversions
    
def IsSolvable():
    NumInversions = GetInvCount()
    if BOARDSIZE % 2 != 0:
        return NumInversions % 2 == 0
    else:
        EmptySquareRow = BOARDSIZE - (board.index(EMPTYSQUARE) // BOARDSIZE)
        if EmptySquareRow % 2 == 0:
            return NumInversions % 2 != 0
        else:
            return NumInversions % 2 == 0
while not IsSolvable():
    shuffle(board)
    print("1")
drawboard()

c.bind('<Button-1>', click)


root.mainloop()


