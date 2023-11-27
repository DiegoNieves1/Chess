from cmu_graphics import *
from imageManager import *

def onAppStart(app):
    loadImages(app)
    app.turn=0
    app.board=[['BlackRook','BlackKnight','BlackBishop','BlackQueen','BlackKing','BlackBishop','BlackKnight','BlackRook'],
               ['BlackPawn','BlackPawn','BlackPawn','BlackPawn','BlackPawn','BlackPawn','BlackPawn','BlackPawn'],
               [None,None,None,None,None,None,None,None],
               [None,None,None,None,None,None,None,None],
               [None,None,None,None,None,None,None,None],
               [None,None,None,None,None,None,None,None],
               ['WhitePawn','WhitePawn','WhitePawn','WhitePawn','WhitePawn','WhitePawn','WhitePawn','WhitePawn'],
               ['WhiteRook','WhiteKnight','WhiteBishop','WhiteQueen','WhiteKing','WhiteBishop','WhiteKnight','WhiteRook']]
    app.boardWidthPixels=(app.width-200)
    app.rows=len(app.board)
    app.boardHeightPixels=(app.height-200)
    app.cols=len(app.board[0])
    app.clicked=None
    app.clickedRow=None
    app.clickedCol=None
    pass
def redrawAll(app):
    drawBoard(app)
    pass

def drawBoard(app):

    #drawing background

    drawRect(0,0,app.width,app.height,fill=rgb(48,46,43))

    #drawing the turns on the board

    drawLabel(f'Move:{app.turn+1}',60,50,fill='white',size=30, bold=True)

    #these nested loops draw the colored squares in the same format as chess.com

    for row in range(app.rows):
        for col in range(app.cols):
            if (row%2==0 and col%2==1) or (col%2==0 and row%2==1):
                drawRect(100+(app.boardWidthPixels/app.rows)*row,
                        100+(app.boardHeightPixels/app.cols)*col,
                        (app.boardWidthPixels/app.rows),
                        (app.boardHeightPixels/app.cols),fill=rgb(115,148,90))
            else:
                drawRect(100+(app.boardWidthPixels/app.rows)*row,
                        100+(app.boardHeightPixels/app.cols)*col,
                        (app.boardWidthPixels/app.rows),
                        (app.boardHeightPixels/app.cols),fill=rgb(235,236,210))
    #these nested loops draw the pieces which are all copied from chess.com
    for row in range(app.rows):
        for col in range(app.cols):
            if app.board[row][col]=='BlackKing':
                drawImage(app.imageDict['BlackKing'],
                          100+(app.boardWidthPixels/app.cols)*col,
                          100+(app.boardHeightPixels/app.rows)*row,
                    width=(app.boardWidthPixels/app.rows),
                    height=(app.boardHeightPixels/app.cols))
            elif app.board[row][col]=='BlackQueen':
                drawImage(app.imageDict['BlackQueen'],
                          100+(app.boardWidthPixels/app.cols)*col,
                          100+(app.boardHeightPixels/app.rows)*row,
                    width=(app.boardWidthPixels/app.rows),
                    height=(app.boardHeightPixels/app.cols))
            elif app.board[row][col]=='BlackBishop':
                drawImage(app.imageDict['BlackBishop'],
                          100+(app.boardWidthPixels/app.cols)*col,
                          100+(app.boardHeightPixels/app.rows)*row,
                    width=(app.boardWidthPixels/app.rows),
                    height=(app.boardHeightPixels/app.cols))
            elif app.board[row][col]=='BlackKnight':
                drawImage(app.imageDict['BlackKnight'],
                          100+(app.boardWidthPixels/app.cols)*col,
                          100+(app.boardHeightPixels/app.rows)*row,
                    width=(app.boardWidthPixels/app.rows),
                    height=(app.boardHeightPixels/app.cols))
            elif app.board[row][col]=='BlackRook':
                drawImage(app.imageDict['BlackRook'],
                          100+(app.boardWidthPixels/app.cols)*col,
                          100+(app.boardHeightPixels/app.rows)*row,
                    width=(app.boardWidthPixels/app.rows),
                    height=(app.boardHeightPixels/app.cols))
            elif app.board[row][col]=='BlackPawn':
                drawImage(app.imageDict['BlackPawn'],
                          100+(app.boardWidthPixels/app.cols)*col,
                          100+(app.boardHeightPixels/app.rows)*row,
                    width=(app.boardWidthPixels/app.rows),
                    height=(app.boardHeightPixels/app.cols))
            elif app.board[row][col]=='WhiteKing':
                drawImage(app.imageDict['WhiteKing'],
                          100+(app.boardWidthPixels/app.cols)*col,
                          100+(app.boardHeightPixels/app.rows)*row,
                    width=(app.boardWidthPixels/app.rows),
                    height=(app.boardHeightPixels/app.cols))
            elif app.board[row][col]=='WhiteQueen':
                drawImage(app.imageDict['WhiteQueen'],
                          100+(app.boardWidthPixels/app.cols)*col,
                          100+(app.boardHeightPixels/app.rows)*row,
                    width=(app.boardWidthPixels/app.rows),
                    height=(app.boardHeightPixels/app.cols))
            elif app.board[row][col]=='WhiteBishop':
                drawImage(app.imageDict['WhiteBishop'],
                          100+(app.boardWidthPixels/app.cols)*col,
                          100+(app.boardHeightPixels/app.rows)*row,
                    width=(app.boardWidthPixels/app.rows),
                    height=(app.boardHeightPixels/app.cols))
            elif app.board[row][col]=='WhiteKnight':
                drawImage(app.imageDict['WhiteKnight'],
                          100+(app.boardWidthPixels/app.cols)*col,
                          100+(app.boardHeightPixels/app.rows)*row,
                    width=(app.boardWidthPixels/app.rows),
                    height=(app.boardHeightPixels/app.cols))
            elif app.board[row][col]=='WhiteRook':
                drawImage(app.imageDict['WhiteRook'],
                          100+(app.boardWidthPixels/app.cols)*col,
                          100+(app.boardHeightPixels/app.rows)*row,
                    width=(app.boardWidthPixels/app.rows),
                    height=(app.boardHeightPixels/app.cols))
            elif app.board[row][col]=='WhitePawn':
                drawImage(app.imageDict['WhitePawn'],
                          100+(app.boardWidthPixels/app.cols)*col,
                          100+(app.boardHeightPixels/app.rows)*row,
                    width=(app.boardWidthPixels/app.rows),
                    height=(app.boardHeightPixels/app.cols))


def onMousePress(app,mouseX,mouseY):
    movePiece(app,mouseX,mouseY)
    pass

def movePiece(app,mouseX,mouseY):
    for row in range(app.rows):
        for col in range(app.cols):
            #setting up which piece was clicked if one is not already clicked
            if ((mouseX>(100+(app.boardWidthPixels/app.cols)*col)
            and mouseX<((100+(app.boardWidthPixels/app.cols)*col)+app.boardWidthPixels/app.rows))
            and(mouseY>(100+(app.boardHeightPixels/app.rows)*row)
            and mouseY<((100+(app.boardHeightPixels/app.rows)*row)+app.boardHeightPixels/app.cols))
            and app.clicked==None):
                app.clicked=app.board[row][col]
                app.clickedRow=row
                app.clickedCol=col
            #switching positions of piece and adding one to the turn
            elif ((mouseX>(100+(app.boardWidthPixels/app.cols)*col)
            and mouseX<((100+(app.boardWidthPixels/app.cols)*col)+app.boardWidthPixels/app.rows))
            and(mouseY>(100+(app.boardHeightPixels/app.rows)*row)
            and mouseY<((100+(app.boardHeightPixels/app.rows)*row)+app.boardHeightPixels/app.cols))
            and app.clicked!=None and isLegal(app,row,col)):
                app.board[app.clickedRow][app.clickedCol]=None
                app.board[row][col]=app.clicked
                app.turn+=1
                app.clicked=None
                app.clickedRow=None
                app.clickedCol=None
                removeEnpassants(app)
            elif ((mouseX>(100+(app.boardWidthPixels/app.cols)*col)
            and mouseX<((100+(app.boardWidthPixels/app.cols)*col)+app.boardWidthPixels/app.rows))
            and(mouseY>(100+(app.boardHeightPixels/app.rows)*row)
            and mouseY<((100+(app.boardHeightPixels/app.rows)*row)+app.boardHeightPixels/app.cols))
            and app.clicked!=None):
                app.clicked=None
                app.clickedRow=None
                app.clickedCol=None
    
def isLegal(app,row,col):

    # checking which colors turn it is

    if app.turn%2==0 and 'Black' in app.clicked:
        return False
    if app.turn%2==1 and 'White' in app.clicked:
        return False

    # conditions for pieces to be able to move

    if (app.clicked == 'WhiteKing' and app.clickedCol-col<2
        and app.clickedCol-col>-2 and app.clickedRow-row<2
        and app.clickedRow-row>-2
        and nothingInWayDiagonally(app,row,col)
        and nothingInWayVerHornally(app,row,col)):
        return True
    if (app.clicked == 'WhiteQueen' and ((app.clickedRow==row or app.clickedCol==col)
                                          or (((app.clickedCol-col)/(app.clickedRow-row)==1)
                                               or ((app.clickedCol-col)/(app.clickedRow-row)==-1)))
                                               and nothingInWayDiagonally(app,row,col)
                                               and nothingInWayVerHornally(app,row,col)):
        return True
    if (app.clicked == 'WhiteBishop' and app.clickedCol!=col
         and app.clickedRow!=row and (((app.clickedCol-col)/(app.clickedRow-row)==1)
                                       or ((app.clickedCol-col)/(app.clickedRow-row)==-1))
                                       and nothingInWayDiagonally(app,row,col)):
        return True
    if (app.clicked == 'WhiteKnight' and ((app.clickedRow-row==1 
                                          and app.clickedCol-col==2) 
                                          or (app.clickedRow-row==-1 
                                          and app.clickedCol-col==-2) 
                                          or (app.clickedRow-row==1 
                                          and app.clickedCol-col==-2) 
                                          or (app.clickedRow-row==-1 
                                          and app.clickedCol-col==2)
                                          or (app.clickedCol-col==1
                                          and app.clickedRow-row==2)
                                          or (app.clickedCol-col==-1
                                          and app.clickedRow-row==-2)
                                          or (app.clickedCol-col==-1
                                          and app.clickedRow-row==2)
                                          or (app.clickedCol-col==1
                                          and app.clickedRow-row==-2))):
        return True
    if (app.clicked == 'WhiteRook' and (app.clickedRow==row or app.clickedCol==col)
        and nothingInWayVerHornally(app,row,col)):
        return True
    if (app.clicked == 'WhitePawn' and nothingInWayVerHornally(app,row,col)
        and pawnMoves(app,row,col)):
        return True
    if (app.clicked == 'BlackKing' and app.clickedCol-col<2
        and app.clickedCol-col>-2 and app.clickedRow-row<2
        and app.clickedRow-row>-2
        and nothingInWayDiagonally(app,row,col)
        and nothingInWayVerHornally(app,row,col)):
        return True
    if (app.clicked == 'BlackQueen' and ((app.clickedRow==row or app.clickedCol==col)
                                          or (((app.clickedCol-col)/(app.clickedRow-row)==1)
                                               or ((app.clickedCol-col)/(app.clickedRow-row)==-1)))
                                               and nothingInWayDiagonally(app,row,col)
                                               and nothingInWayVerHornally(app,row,col)):
        return True
    if (app.clicked == 'BlackBishop' and app.clickedCol!=col
         and app.clickedRow!=row and (((app.clickedCol-col)/(app.clickedRow-row)==1)
                                       or ((app.clickedCol-col)/(app.clickedRow-row)==-1))
                                       and nothingInWayDiagonally(app,row,col)):
        return True
    if (app.clicked == 'BlackKnight' and ((app.clickedRow-row==1 
                                          and app.clickedCol-col==2) 
                                          or (app.clickedRow-row==-1 
                                          and app.clickedCol-col==-2) 
                                          or (app.clickedRow-row==1 
                                          and app.clickedCol-col==-2) 
                                          or (app.clickedRow-row==-1 
                                          and app.clickedCol-col==2)
                                          or (app.clickedCol-col==1
                                          and app.clickedRow-row==2)
                                          or (app.clickedCol-col==-1
                                          and app.clickedRow-row==-2)
                                          or (app.clickedCol-col==-1
                                          and app.clickedRow-row==2)
                                          or (app.clickedCol-col==1
                                          and app.clickedRow-row==-2))):
        return True
    if (app.clicked == 'BlackRook' and (app.clickedRow==row or app.clickedCol==col)
        and nothingInWayVerHornally(app,row,col)):
        return True
    if (app.clicked == 'BlackPawn' and nothingInWayVerHornally(app,row,col)
        and pawnMoves(app,row,col)):
        return True
    return False

def nothingInWayDiagonally(app,row,col):

    # checks for any pieces in the way of pieces moving diagonally so that the piece knows not to go

    verticalMovement= app.clickedRow-row
    horizontalMovement= col-app.clickedCol

    # checks if there is a same side piece on the spot that were moving to

    if app.board[row][col] != None and 'Black' in app.clicked and 'Black' in app.board[row][col]:
        return False
    if app.board[row][col] != None and 'White' in app.clicked and 'White' in app.board[row][col]:
        return False
    
    # for loop checking every block the piece would have to traverse in order to know
    # if it has a piece there and returning False if it does
    
    for i in range(1,abs(verticalMovement)):
        if verticalMovement>0 and horizontalMovement>0:
            if app.board[app.clickedRow-i][app.clickedCol+i]!=None:
                return False
        elif verticalMovement<0 and horizontalMovement>0:
            if app.board[app.clickedRow+i][app.clickedCol+i]!=None:
                return False
        elif verticalMovement>0 and horizontalMovement<0:
            if app.board[app.clickedRow-i][app.clickedCol-i]!=None:
                return False
        elif verticalMovement<0 and horizontalMovement<0:
            if app.board[app.clickedRow+i][app.clickedCol-i]!=None:
                return False
    return True

def nothingInWayVerHornally(app,row,col):

    #checks if there are any pieces in the way of a verically/horizontally moving piece

    verticalMovement= app.clickedRow-row
    horizontalMovement= col-app.clickedCol

    # checks if there is a same side piece on the spot that were moving to

    if app.board[row][col] != None and 'Black' in app.clicked and 'Black' in app.board[row][col]:
        return False
    if app.board[row][col] != None and 'White' in app.clicked and 'White' in app.board[row][col]:
        return False
    
    # for loop checking every block the piece would have to traverse in order to know
    # if it has a piece there and returning False if it does
    
    if verticalMovement==0 and horizontalMovement>0:
        for i in range(1,abs(horizontalMovement)):
            if app.board[app.clickedRow][app.clickedCol+i]!=None:
                return False
    elif verticalMovement==0 and horizontalMovement<0:
        for i in range(1,abs(horizontalMovement)):
            if app.board[app.clickedRow][app.clickedCol-i]!=None:
                return False
    elif horizontalMovement==0 and verticalMovement>0:
        for i in range(1,abs(verticalMovement)):
            if app.board[app.clickedRow-i][app.clickedCol]!=None:
                return False
    elif horizontalMovement==0 and verticalMovement<0:
        for i in range(1,abs(verticalMovement)):
            if app.board[app.clickedRow+i][app.clickedCol]!=None:
                return False
    return True

def pawnMoves(app,row,col):
    
     #checks if there are any pieces in the way of a verically/horizontally moving piece

    verticalMovement= app.clickedRow-row
    horizontalMovement= col-app.clickedCol

    if verticalMovement==2 and app.clickedRow==6 and app.clickedCol==col:
        app.board[row+1][col]='WhiteEnpassant'
        return True
    elif verticalMovement==-2 and app.clickedRow==1 and app.clickedCol==col:
        app.board[row-1][col]='BlackEnpassant'
        return True
    elif abs(verticalMovement)>1:
        return False
    elif (verticalMovement==1 and horizontalMovement==0 and
    'WhitePawn'==app.clicked) and app.board[row][col]==None:
        return True
    elif (verticalMovement==1 and abs(horizontalMovement)==1 and 'WhitePawn' == app.clicked
          and app.board[row][col]!=None):
        app.board[row+1][col]=None
        return True
    elif (verticalMovement==-1 and horizontalMovement==0 and
    'BlackPawn'==app.clicked and app.board[row][col]==None):
        return True
    elif (verticalMovement==-1 and abs(horizontalMovement)==1 and 'BlackPawn' == app.clicked
          and app.board[row][col]!=None):
        app.board[row-1][col]=None
        return True

def removeEnpassants(app):
    if app.turn%2==0:
        for row in range(len(app.board)):
            for col in range(len(app.board[0])):
                if app.board[row][col]=='WhiteEnpassant':
                    app.board[row][col]=None
    elif app.turn%2==1:
        for row in range(len(app.board)):
            for col in range(len(app.board[0])):
                if app.board[row][col]=='BlackEnpassant':
                    app.board[row][col]=None

# def castle(app,row,col):
#     if (app.board[len(app.board)-1][4] == 'WhiteKing' and app.board[len(app.board)-1][len(app.board[0])-1] == 'WhiteRook'
#         and app.board[len(app.board)-1][5] == None and app.board[len(app.board)-1][6] == None
#         and app.clicked=='WhiteKing' and app.board[row][col]=='WhiteRook'):
#         app.board[len(app.board)-1][5] = 'WhiteRook' 
#         app.board[len(app.board)-1][6] = 'WhiteKing'
#         return False
#     return True

# def inCheck(app):
    

def main():
    runApp(800,800)

main()