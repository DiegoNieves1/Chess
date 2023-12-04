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
    app.whiteKingMoved=False
    app.blackKingMoved=False
    app.whiteRook1Moved=False
    app.whiteRook2Moved=False
    app.blackRook1Moved=False
    app.blackRook2Moved=False
    app.whitePawnIsPromoting=False
    app.blackPawnIsPromoting=False
    app.whiteInCheck=False
    app.blackInCheck=False
    app.whiteInCheckmate=False
    app.blackInCheckmate=False
    app.stepsPerSecond=5
    app.whitePawnPromotionBoard=['WhiteQueen','WhiteKnight','WhiteRook','WhiteBishop']
    app.blackPawnPromotionBoard=['BlackQueen','BlackKnight','BlackRook','BlackBishop']
    pass
def redrawAll(app):
    drawBoard(app)
    if app.whitePawnIsPromoting or app.blackPawnIsPromoting:
        drawPawnPromotionOptions(app)
    if app.whiteInCheck and app.whiteInCheckmate==False:
        drawLabel('White In Check!!!',app.width/2,50,size=40,fill='white', bold=True)
    if app.blackInCheck and app.blackInCheckmate==False:
        drawLabel('Black In Check!!!',app.width/2,50,size=40,fill='white', bold=True)
    if app.whiteInCheckmate==True:
        drawLabel('Black Wins!!!',app.width/2,50,size=40,fill='white',bold=True)
    if app.blackInCheckmate==True:
        drawLabel('White Wins!!!',app.width/2,50,size=40,fill='white',bold=True)
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
    #images are from chess.com but I got them from https://github.com/lichess-org/lila/issues/3411
    #the background of the images were removed with https://www.remove.bg/
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

def drawPawnPromotionOptions(app):
    if app.whitePawnIsPromoting:
        for i in range(len(app.whitePawnPromotionBoard)):
            drawImage(app.imageDict[app.whitePawnPromotionBoard[i]],
                            app.width-75,
                            app.height-50-(app.height-200)/(12/(i+1)),
                        width=(50),
                        height=(50))
    if app.blackPawnIsPromoting:
        for i in range(len(app.blackPawnPromotionBoard)):
            drawImage(app.imageDict[app.blackPawnPromotionBoard[i]],
                            app.width-75,
                            (app.height-200)/(12/(i+1)),
                        width=(50),
                        height=(50))

def onMousePress(app,mouseX,mouseY):
    if app.whitePawnIsPromoting or app.blackPawnIsPromoting:
        pawnPromotionClicks(app,mouseX,mouseY)
    else:
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
                # if app.whiteInCheck==True:
                #     app.whiteInCheckmate=whiteInCheckmate(app)
                # if app.blackInCheck==True:
                #     app.blackInCheckmate==blackInCheckmate(app)
                app.clicked=None
                app.clickedRow=None
                app.clickedCol=None
                app.whiteInCheck=whiteInCheck(app)
                app.blackInCheck=blackInCheck(app)
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
    elif app.turn%2==1 and 'White' in app.clicked:
        return False

    # conditions for pieces to be able to move

    if (app.clicked == 'WhiteKing' and ((app.clickedCol-col<2
        and app.clickedCol-col>-2 and app.clickedRow-row<2
        and app.clickedRow-row>-2
        and nothingInWayDiagonally(app,row,col)
        and nothingInWayVerHornally(app,row,col)) or castle(app,row,col))
         and ifWhiteInCheck(app,row,col)):
        app.whiteKingMoved=True
        return True
    elif (app.clicked == 'WhiteQueen' and ((app.clickedRow==row or app.clickedCol==col)
                                          or (((app.clickedCol-col)/(app.clickedRow-row)==1)
                                               or ((app.clickedCol-col)/(app.clickedRow-row)==-1)))
                                               and nothingInWayDiagonally(app,row,col)
                                               and nothingInWayVerHornally(app,row,col)
                                                and ifWhiteInCheck(app,row,col)):
        return True
    elif (app.clicked == 'WhiteBishop' and app.clickedCol!=col
         and app.clickedRow!=row and (((app.clickedCol-col)/(app.clickedRow-row)==1)
                                       or ((app.clickedCol-col)/(app.clickedRow-row)==-1))
                                       and nothingInWayDiagonally(app,row,col)
                                        and ifWhiteInCheck(app,row,col)):
        return True
    elif (app.clicked == 'WhiteKnight' and ((app.clickedRow-row==1 
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
                                          and app.clickedRow-row==-2))
                                          and knightHelper(app,row,col)
                                          and ifWhiteInCheck(app,row,col)):
        return True
    elif (app.clicked == 'WhiteRook' and (app.clickedRow==row or app.clickedCol==col)
        and nothingInWayVerHornally(app,row,col) and ifWhiteInCheck(app,row,col)):
        if app.clickedRow==7 and app.clickedCol==7:
            app.whiteRook1Moved=True
        if app.clickedRow==7 and app.clickedCol==0:
            app.whiteRook2Moved=True
        return True
    elif (app.clicked == 'WhitePawn' and nothingInWayVerHornally(app,row,col)
        and pawnMoves(app,row,col) and ifWhiteInCheck(app,row,col)):
        pawnPromoting(app,row,col)
        return True
    elif (app.clicked == 'BlackKing' and ((app.clickedCol-col<2
        and app.clickedCol-col>-2 and app.clickedRow-row<2
        and app.clickedRow-row>-2
        and nothingInWayDiagonally(app,row,col)
        and nothingInWayVerHornally(app,row,col)) or castle(app,row,col))
        and ifBlackInCheck(app,row,col)):
        app.blackKingMoved=True
        return True
    elif (app.clicked == 'BlackQueen' and ((app.clickedRow==row or app.clickedCol==col)
                                          or (((app.clickedCol-col)/(app.clickedRow-row)==1)
                                               or ((app.clickedCol-col)/(app.clickedRow-row)==-1)))
                                               and nothingInWayDiagonally(app,row,col)
                                               and nothingInWayVerHornally(app,row,col)
                                               and ifBlackInCheck(app,row,col)):
        return True
    elif (app.clicked == 'BlackBishop' and app.clickedCol!=col
         and app.clickedRow!=row and (((app.clickedCol-col)/(app.clickedRow-row)==1)
                                       or ((app.clickedCol-col)/(app.clickedRow-row)==-1))
                                       and nothingInWayDiagonally(app,row,col)
                                       and ifBlackInCheck(app,row,col)):
        return True
    elif (app.clicked == 'BlackKnight' and ((app.clickedRow-row==1 
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
                                          and app.clickedRow-row==-2))
                                          and knightHelper(app,row,col)
                                          and ifBlackInCheck(app,row,col)):
        return True
    elif (app.clicked == 'BlackRook' and (app.clickedRow==row or app.clickedCol==col)
        and nothingInWayVerHornally(app,row,col) and ifBlackInCheck(app,row,col)):
        if app.clickedRow==0 and app.clickedCol==7:
            app.blackRook1Moved=True
        if app.clickedRow==0 and app.clickedCol==0:
            app.blackRook2Moved=True
        return True
    elif (app.clicked == 'BlackPawn' and nothingInWayVerHornally(app,row,col)
        and pawnMoves(app,row,col) and ifBlackInCheck(app,row,col)):
        pawnPromoting(app,row,col)
        return True
    return False

def nothingInWayDiagonally(app,row,col):

    # checks for any pieces in the way of pieces moving diagonally so that the piece knows not to go

    verticalMovement= app.clickedRow-row
    horizontalMovement= col-app.clickedCol

    # checks if there is a same side piece on the spot that were moving to

    if app.board[row][col] != None and app.clicked!=None and 'Black' in app.clicked and 'Black' in app.board[row][col]:
        return False
    if app.board[row][col] != None and app.clicked!=None and 'White' in app.clicked and 'White' in app.board[row][col]:
        return False
    
    # for loop checking every block the piece would have to traverse in order to know
    # if it has a piece there and returning False if it does
    
    for i in range(1,abs(verticalMovement)):
        if verticalMovement>0 and horizontalMovement>0:
            if (app.board[app.clickedRow-i][app.clickedCol+i]!=None
                and app.board[app.clickedRow-i][app.clickedCol+i]!='BlackEnpassant'
                and app.board[app.clickedRow-i][app.clickedCol+i]!='WhiteEnpassant'):
                return False
        elif verticalMovement<0 and horizontalMovement>0:
            if (app.board[app.clickedRow+i][app.clickedCol+i]!=None
                and app.board[app.clickedRow+i][app.clickedCol+i]!='BlackEnpassant'
                and app.board[app.clickedRow+i][app.clickedCol+i]!='WhiteEnpassant'):
                return False
        elif verticalMovement>0 and horizontalMovement<0:
            if (app.board[app.clickedRow-i][app.clickedCol-i]!=None
                and app.board[app.clickedRow-i][app.clickedCol-i]!='BlackEnpassant'
                and app.board[app.clickedRow-i][app.clickedCol-i]!='WhiteEnpassant'):
                return False
        elif verticalMovement<0 and horizontalMovement<0:
            if (app.board[app.clickedRow+i][app.clickedCol-i]!=None
                and app.board[app.clickedRow+i][app.clickedCol-i]!='BlackEnpassant'
                and app.board[app.clickedRow+i][app.clickedCol-i]!='WhiteEnpassant'):
                return False
    return True

def nothingInWayVerHornally(app,row,col):

    #checks if there are any pieces in the way of a verically/horizontally moving piece

    verticalMovement= app.clickedRow-row
    horizontalMovement= col-app.clickedCol

    # checks if there is a same side piece on the spot that were moving to

    if app.board[row][col] != None and app.clicked!=None and 'Black' in app.clicked and 'Black' in app.board[row][col]:
        return False
    if app.board[row][col] != None and app.clicked!=None and 'White' in app.clicked and 'White' in app.board[row][col]:
        return False
    
    # for loop checking every block the piece would have to traverse in order to know
    # if it has a piece there and returning False if it does
    
    if verticalMovement==0 and horizontalMovement>0:
        for i in range(1,abs(horizontalMovement)):
            if (app.board[app.clickedRow][app.clickedCol+i]!=None
                and app.board[app.clickedRow][app.clickedCol+i]!='BlackEnpassant'
                and app.board[app.clickedRow][app.clickedCol+i]!='WhiteEnpassant'):
                return False
    elif verticalMovement==0 and horizontalMovement<0:
        for i in range(1,abs(horizontalMovement)):
            if (app.board[app.clickedRow][app.clickedCol-i]!=None
                and app.board[app.clickedRow][app.clickedCol-i]!='BlackEnpassant'
                and app.board[app.clickedRow][app.clickedCol-i]!='WhiteEnpassant'):
                return False
    elif horizontalMovement==0 and verticalMovement>0:
        for i in range(1,abs(verticalMovement)):
            if (app.board[app.clickedRow-i][app.clickedCol]!=None
                and app.board[app.clickedRow-i][app.clickedCol]!='BlackEnpassant'
                and app.board[app.clickedRow-i][app.clickedCol]!='WhiteEnpassant'):
                return False
    elif horizontalMovement==0 and verticalMovement<0:
        for i in range(1,abs(verticalMovement)):
            if (app.board[app.clickedRow+i][app.clickedCol]!=None
                and app.board[app.clickedRow+i][app.clickedCol]!='BlackEnpassant'
                and app.board[app.clickedRow+i][app.clickedCol]!='WhiteEnpassant'):
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
        if app.board[row][col]=='BlackEnpassant':
            app.board[row+1][col]=None
        return True
    elif (verticalMovement==-1 and horizontalMovement==0 and
    'BlackPawn'==app.clicked and app.board[row][col]==None):
        return True
    elif (verticalMovement==-1 and abs(horizontalMovement)==1 and 'BlackPawn' == app.clicked
          and app.board[row][col]!=None):
        if app.board[row][col]=='WhiteEnpassant':
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

def castle(app,row,col):
    if (app.board[row][col]=='WhiteRook' and row==7 and col==7
        and app.board[7][6]==None and app.board[7][5]==None
        and app.clickedRow==7 and app.clickedCol==4 and not app.whiteKingMoved 
        and not app.whiteRook1Moved and not app.whiteInCheck):
        app.whiteKingMoved=True
        app.board[7][5]='WhiteRook'
        app.board[7][6]='WhiteKing'
        app.board[row][col]=None
        app.board[app.clickedRow][app.clickedCol]=None
        clicked=app.clicked
        clickedRow=app.clickedRow
        clickedCol=app.clickedCol
        app.clicked=None
        app.clickedRow=None
        app.clickedCol=None
        if whiteInCheck(app):
            app.clicked=clicked
            app.clickedRow=clickedRow
            app.clickedCol=clickedCol
            app.board[app.clickedRow][app.clickedCol]='WhiteKing'
            app.board[row][col]='WhiteRook'
            app.board[7][5]=None
            app.board[7][6]=None
            return False
        app.turn+=1
        return False
    elif (app.board[row][col]=='WhiteRook' and row==7 and col==0
        and app.board[7][1]==None and app.board[7][2]==None and app.board[7][3]==None
        and app.clickedRow==7 and app.clickedCol==4 and not app.whiteKingMoved
        and not app.whiteRook2Moved and not app.whiteInCheck):
        app.whiteKingMoved=True
        app.board[7][3]='WhiteRook'
        app.board[7][2]='WhiteKing'
        app.board[row][col]=None
        app.board[app.clickedRow][app.clickedCol]=None
        clicked=app.clicked
        clickedRow=app.clickedRow
        clickedCol=app.clickedCol
        app.clicked=None
        app.clickedRow=None
        app.clickedCol=None
        if whiteInCheck(app):
            app.clicked=clicked
            app.clickedRow=clickedRow
            app.clickedCol=clickedCol
            app.board[app.clickedRow][app.clickedCol]='WhiteKing'
            app.board[row][col]='WhiteRook'
            app.board[7][3]=None
            app.board[7][2]=None
            return False
        app.turn+=1
        return False
    elif (app.board[row][col]=='BlackRook' and row==0 and col==7
        and app.board[0][6]==None and app.board[0][5]==None
        and app.clickedRow==0 and app.clickedCol==4 and not app.blackKingMoved
        and not app.blackRook1Moved and not app.blackInCheck):
        app.blackKingMoved=True
        app.board[0][5]='BlackRook'
        app.board[0][6]='BlackKing'
        app.board[row][col]=None
        app.board[app.clickedRow][app.clickedCol]=None
        clicked=app.clicked
        clickedRow=app.clickedRow
        clickedCol=app.clickedCol
        app.clicked=None
        app.clickedRow=None
        app.clickedCol=None
        if blackInCheck(app):
            app.clicked=clicked
            app.clickedRow=clickedRow
            app.clickedCol=clickedCol
            app.board[app.clickedRow][app.clickedCol]='BlackKing'
            app.board[row][col]='BlackRook'
            app.board[0][6]=None
            app.board[0][5]=None
            return False
        app.turn+=1
        return False
    elif (app.board[row][col]=='BlackRook' and row==0 and col==0
        and app.board[0][1]==None and app.board[0][2]==None and app.board[0][3]==None
        and app.clickedRow==0 and app.clickedCol==4 and not app.blackKingMoved
        and not app.blackRook2Moved and not app.blackInCheck):
        app.blackKingMoved=True
        app.board[0][3]='BlackRook'
        app.board[0][2]='BlackKing'
        app.board[row][col]=None
        app.board[app.clickedRow][app.clickedCol]=None
        clicked=app.clicked
        clickedRow=app.clickedRow
        clickedCol=app.clickedCol
        app.clicked=None
        app.clickedRow=None
        app.clickedCol=None
        if blackInCheck(app):
            app.clicked=clicked
            app.clickedRow=clickedRow
            app.clickedCol=clickedCol
            app.board[app.clickedRow][app.clickedCol]='BlackKing'
            app.board[row][col]='BlackRook'
            app.board[0][3]=None
            app.board[0][2]=None
            return False
        app.turn+=1
        return False
    return False

def knightHelper(app,row,col):
    if app.board[row][col] != None and 'Black' in app.clicked and 'Black' in app.board[row][col]:
        return False
    if app.board[row][col] != None and 'White' in app.clicked and 'White' in app.board[row][col]:
        return False
    return True

def pawnPromoting(app,row,col):
    if app.board[app.clickedRow][app.clickedCol]=='WhitePawn' and row==0:
        promotePawn(app)
    elif app.board[app.clickedRow][app.clickedCol]=='BlackPawn' and row==7:
        promotePawn(app)

def promotePawn(app):
    if app.board[app.clickedRow][app.clickedCol]=='WhitePawn':
        app.whitePawnIsPromoting=True
    if app.board[app.clickedRow][app.clickedCol]=='BlackPawn':
        app.blackPawnIsPromoting=True

def pawnPromotionClicks(app,mouseX,mouseY):
    if (app.whitePawnIsPromoting and mouseX>app.width-75 and mouseX<app.width-25
        and mouseY>550 and mouseY<600):
        for i in range(len(app.board[0])):
            if app.board[0][i]=='WhitePawn':
                app.board[0][i]='WhiteBishop'
                app.whitePawnIsPromoting=False
    if (app.whitePawnIsPromoting and mouseX>app.width-75 and mouseX<app.width-25
        and mouseY>600 and mouseY<650):
        for i in range(len(app.board[0])):
            if app.board[0][i]=='WhitePawn':
                app.board[0][i]='WhiteRook'
                app.whitePawnIsPromoting=False
    if (app.whitePawnIsPromoting and mouseX>app.width-75 and mouseX<app.width-25
        and mouseY>650 and mouseY<700):
        for i in range(len(app.board[0])):
            if app.board[0][i]=='WhitePawn':
                app.board[0][i]='WhiteKnight'
                app.whitePawnIsPromoting=False
    if (app.whitePawnIsPromoting and mouseX>app.width-75 and mouseX<app.width-25
        and mouseY>700 and mouseY<750):
        for i in range(len(app.board[0])):
            if app.board[0][i]=='WhitePawn':
                app.board[0][i]='WhiteQueen'
                app.whitePawnIsPromoting=False
    if (app.blackPawnIsPromoting and mouseX>app.width-75 and mouseX<app.width-25
        and mouseY>200 and mouseY<250):
        for i in range(len(app.board[0])):
            if app.board[7][i]=='BlackPawn':
                app.board[7][i]='BlackBishop'
                app.blackPawnIsPromoting=False
    if (app.blackPawnIsPromoting and mouseX>app.width-75 and mouseX<app.width-25
        and mouseY>150 and mouseY<200):
        for i in range(len(app.board[0])):
            if app.board[7][i]=='BlackPawn':
                app.board[7][i]='BlackRook'
                app.blackPawnIsPromoting=False
    if (app.blackPawnIsPromoting and mouseX>app.width-75 and mouseX<app.width-25
        and mouseY>100 and mouseY<150):
        for i in range(len(app.board[0])):
            if app.board[7][i]=='BlackPawn':
                app.board[7][i]='BlackKnight'
                app.blackPawnIsPromoting=False
    if (app.blackPawnIsPromoting and mouseX>app.width-75 and mouseX<app.width-25
        and mouseY>50 and mouseY<100):
        for i in range(len(app.board[0])):
            if app.board[7][i]=='BlackPawn':
                app.board[7][i]='BlackQueen'
                app.blackPawnIsPromoting=False

def whiteInCheck(app):
    for row in range(len(app.board)):
        for col in range(len(app.board[0])):
            if app.board[row][col]=='WhiteKing':
                whiteKingRow=row
                whiteKingCol=col
    for row in range(len(app.board)):
        for col in range(len(app.board[0])):
            if (app.board[row][col]!=None and 'Black' in app.board[row][col]
                and 'Enpassant' not in app.board[row][col]):
                if isInCheck(app,row,col,whiteKingRow,whiteKingCol):
                    return True
                else:
                    continue
    return False

def blackInCheck(app):
    for row in range(len(app.board)):
        for col in range(len(app.board[0])):
            if app.board[row][col]=='BlackKing':
                blackKingRow=row
                blackKingCol=col
    for row in range(len(app.board)):
        for col in range(len(app.board[0])):
            if (app.board[row][col]!=None and 'White' in app.board[row][col]
                and 'Enpassant' not in app.board[row][col]):
                if isInCheck(app,row,col,blackKingRow,blackKingCol):
                    return True
                else:
                    continue
    return False

# helper function for checking if the king is in check
def isInCheck(app,row,col,kingRow,kingCol):
    if (app.board[row][col] == 'WhiteKing' and ((col-kingCol<2
        and col-kingCol>-2 and row-kingRow<2
        and row-kingRow>-2
        and nothingInWayDiagonallyCheck(app,row,col,kingRow,kingCol)
        and nothingInWayVerHornallyCheck(app,row,col,kingRow,kingCol)) or castle(app,kingRow,kingCol))):
        return True
    elif (app.board[row][col] == 'WhiteQueen' and ((row==kingRow or col==kingCol)
                                          or (((col-kingCol)/(row-kingRow)==1)
                                               or ((col-kingCol)/(row-kingRow)==-1)))
                                               and nothingInWayDiagonallyCheck(app,row,col,kingRow,kingCol)
                                               and nothingInWayVerHornallyCheck(app,row,col,kingRow,kingCol)):
        return True
    elif (app.board[row][col] == 'WhiteBishop' and col!=kingCol
         and row!=kingRow and (((col-kingCol)/(row-kingRow)==1)
                                       or ((col-kingCol)/(row-kingRow)==-1))
                                       and nothingInWayDiagonallyCheck(app,row,col,kingRow,kingCol)):
        return True
    elif (app.board[row][col] == 'WhiteKnight' and ((row-kingRow==1 
                                          and col-kingCol==2) 
                                          or (row-kingRow==-1 
                                          and col-kingCol==-2) 
                                          or (row-kingRow==1 
                                          and col-kingCol==-2) 
                                          or (row-kingRow==-1 
                                          and col-kingCol==2)
                                          or (col-kingCol==1
                                          and row-kingRow==2)
                                          or (col-kingCol==-1
                                          and row-kingRow==-2)
                                          or (col-kingCol==-1
                                          and row-kingRow==2)
                                          or (col-kingCol==1
                                          and row-kingRow==-2))
                                          and knightHelperCheck(app,row,col,kingRow,kingCol)):
        return True
    elif (app.board[row][col] == 'WhiteRook' and (row==kingRow or col==kingCol)
        and nothingInWayVerHornallyCheck(app,row,col,kingRow,kingCol)):
        return True
    elif (app.board[row][col] == 'WhitePawn' and nothingInWayVerHornallyCheck(app,row,col,kingRow,kingCol)
        and pawnMovesCheck(app,row,col,kingRow,kingCol)):
        pawnPromoting(app,kingRow,kingCol)
        return True
    elif (app.board[row][col] == 'BlackKing' and ((col-kingCol<2
        and col-kingCol>-2 and row-kingRow<2
        and row-kingRow>-2
        and nothingInWayDiagonallyCheck(app,row,col,kingRow,kingCol)
        and nothingInWayVerHornallyCheck(app,row,col,kingRow,kingCol)) or castle(app,kingRow,kingCol))):
        return True
    elif (app.board[row][col] == 'BlackQueen' and ((row==kingRow or col==kingCol)
                                          or (((col-kingCol)/(row-kingRow)==1)
                                               or ((col-kingCol)/(row-kingRow)==-1)))
                                               and nothingInWayDiagonallyCheck(app,row,col,kingRow,kingCol)
                                               and nothingInWayVerHornallyCheck(app,row,col,kingRow,kingCol)):
        return True
    elif (app.board[row][col] == 'BlackBishop' and col!=kingCol
         and row!=kingRow and (((col-kingCol)/(row-kingRow)==1)
                                       or ((col-kingCol)/(row-kingRow)==-1))
                                       and nothingInWayDiagonallyCheck(app,row,col,kingRow,kingCol)):
        return True
    elif (app.board[row][col] == 'BlackKnight' and ((row-kingRow==1 
                                          and col-kingCol==2) 
                                          or (row-kingRow==-1 
                                          and col-kingCol==-2) 
                                          or (row-kingRow==1 
                                          and col-kingCol==-2) 
                                          or (row-kingRow==-1 
                                          and col-kingCol==2)
                                          or (col-kingCol==1
                                          and row-kingRow==2)
                                          or (col-kingCol==-1
                                          and row-kingRow==-2)
                                          or (col-kingCol==-1
                                          and row-kingRow==2)
                                          or (col-kingCol==1
                                          and row-kingRow==-2))
                                          and knightHelperCheck(app,row,col,kingRow,kingCol)):
        return True
    elif (app.board[row][col] == 'BlackRook' and (row==kingRow or col==kingCol)
        and nothingInWayVerHornallyCheck(app,row,col,kingRow,kingCol)):
        return True
    elif (app.board[row][col] == 'BlackPawn' and nothingInWayVerHornallyCheck(app,row,col,kingRow,kingCol)
        and pawnMovesCheck(app,row,col,kingRow,kingCol)):
        pawnPromoting(app,kingRow,kingCol)
        return True
    return False

def nothingInWayVerHornallyCheck(app,row,col,kingRow,kingCol):
     #checks if there are any pieces in the way of a verically/horizontally moving piece

    verticalMovement= row-kingRow
    horizontalMovement= kingCol-col

    # checks if there is a same side piece on the spot that were moving to

    if (app.board[kingRow][kingCol] != None and app.board[row][col]!=None 
    and 'Black' in app.board[row][col] and 'Black' in app.board[kingRow][kingCol]):
        return False
    if (app.board[kingRow][kingCol] != None and app.board[row][col]!=None 
        and 'White' in app.board[row][col] and 'White' in app.board[kingRow][kingCol]):
        return False
    
    # for loop checking every block the piece would have to traverse in order to know
    # if it has a piece there and returning False if it does
    
    if verticalMovement==0 and horizontalMovement>0:
        for i in range(1,abs(horizontalMovement)):
            if (app.board[row][col+i]!=None
                and app.board[row][col+i]!='BlackEnpassant'
                and app.board[row][col+i]!='WhiteEnpassant'):
                return False
    elif verticalMovement==0 and horizontalMovement<0:
        for i in range(1,abs(horizontalMovement)):
            if (app.board[row][col-i]!=None
                and app.board[row][col-i]!='BlackEnpassant'
                and app.board[row][col-i]!='WhiteEnpassant'):
                return False
    elif horizontalMovement==0 and verticalMovement>0:
        for i in range(1,abs(verticalMovement)):
            if (app.board[row-i][col]!=None
                and app.board[row-i][col]!='BlackEnpassant'
                and app.board[row-i][col]!='WhiteEnpassant'):
                return False
    elif horizontalMovement==0 and verticalMovement<0:
        for i in range(1,abs(verticalMovement)):
            if (app.board[row+i][col]!=None
                and app.board[row+i][col]!='BlackEnpassant'
                and app.board[row+i][col]!='WhiteEnpassant'):
                return False
    return True

def nothingInWayDiagonallyCheck(app,row,col,kingRow,kingCol):
    
    # checks for any pieces in the way of pieces moving diagonally so that the piece knows not to go

    verticalMovement= row-kingRow
    horizontalMovement= kingCol-col

    # checks if there is a same side piece on the spot that were moving to

    if app.board[kingRow][kingCol] != None and app.clicked!=None and 'Black' in app.clicked and 'Black' in app.board[kingRow][kingCol]:
        return False
    if app.board[kingRow][kingCol] != None and app.clicked!=None and 'White' in app.clicked and 'White' in app.board[kingRow][kingCol]:
        return False
    
    # for loop checking every block the piece would have to traverse in order to know
    # if it has a piece there and returning False if it does
    
    for i in range(1,abs(verticalMovement)):
        if verticalMovement>0 and horizontalMovement>0:
            if (app.board[row-i][col+i]!=None
                and app.board[row-i][col+i]!='BlackEnpassant'
                and app.board[row-i][col+i]!='WhiteEnpassant'):
                return False
        elif verticalMovement<0 and horizontalMovement>0:
            if (app.board[row+i][col+i]!=None
                and app.board[row+i][col+i]!='BlackEnpassant'
                and app.board[row+i][col+i]!='WhiteEnpassant'):
                return False
        elif verticalMovement>0 and horizontalMovement<0:
            if (app.board[row-i][col-i]!=None
                and app.board[row-i][col-i]!='BlackEnpassant'
                and app.board[row-i][col-i]!='WhiteEnpassant'):
                return False
        elif verticalMovement<0 and horizontalMovement<0:
            if (app.board[row+i][col-i]!=None
                and app.board[row+i][col-i]!='BlackEnpassant'
                and app.board[row+i][col-i]!='WhiteEnpassant'):
                return False
    return True

def knightHelperCheck(app,row,col,kingRow,kingCol):
    if app.board[kingRow][kingCol] != None and 'Black' in app.board[row][col] and 'Black' in app.board[kingRow][kingCol]:
        return False
    if app.board[kingRow][kingCol] != None and 'White' in app.board[row][col] and 'White' in app.board[kingRow][kingCol]:
        return False
    return True

def pawnMovesCheck(app,row,col,kingRow,kingCol):
      #checks if there are any pieces in the way of a verically/horizontally moving piece

    verticalMovement= row-kingRow
    horizontalMovement= kingCol-col

    if verticalMovement==2 and row==6 and col==kingCol:
        app.board[kingRow+1][kingCol]='WhiteEnpassant'
        return True
    elif verticalMovement==-2 and row==1 and col==kingCol:
        app.board[kingRow-1][kingCol]='BlackEnpassant'
        return True
    elif abs(verticalMovement)>1:
        return False
    elif (verticalMovement==1 and horizontalMovement==0 and
    'WhitePawn'==app.board[row][col]) and app.board[kingRow][kingCol]==None:
        return True
    elif (verticalMovement==1 and abs(horizontalMovement)==1 and 'WhitePawn' == app.board[row][col]
          and app.board[kingRow][kingCol]!=None):
        if app.board[kingRow][kingCol]=='BlackEnpassant':
            app.board[kingRow+1][kingCol]=None
        return True
    elif (verticalMovement==-1 and horizontalMovement==0 and
    'BlackPawn'==app.board[row][col] and app.board[kingRow][kingCol]==None):
        return True
    elif (verticalMovement==-1 and abs(horizontalMovement)==1 and 'BlackPawn' == app.board[row][col]
          and app.board[kingRow][kingCol]!=None):
        if app.board[kingRow][kingCol]=='WhiteEnpassant':
            app.board[kingRow-1][kingCol]=None
        return True

# If white in check is used in the islegal function to see if a move will make the king not be defended
# from check anymore if the clicked piece moves
def ifWhiteInCheck(app,row,col):
    temp=app.board[row][col]
    app.board[row][col]=app.clicked
    app.board[app.clickedRow][app.clickedCol]=None
    clicked=app.clicked
    clickedRow=app.clickedRow
    clickedCol=app.clickedCol
    app.clicked=None
    app.clickedRow=None
    app.clickedCol=None
    if whiteInCheck(app):
        app.board[row][col]=temp
        app.board[clickedRow][clickedCol]=clicked
        app.clicked=clicked
        app.clickedRow=clickedRow
        app.clickedCol=clickedCol
        return False
    app.clicked=clicked
    app.clickedRow=clickedRow
    app.clickedCol=clickedCol
    app.board[row][col]=temp
    app.board[app.clickedRow][app.clickedCol]=app.clicked
    return True

def ifBlackInCheck(app,row,col):
    temp=app.board[row][col]
    app.board[row][col]=app.clicked
    app.board[app.clickedRow][app.clickedCol]=None
    clicked=app.clicked
    clickedRow=app.clickedRow
    clickedCol=app.clickedCol
    app.clicked=None
    app.clickedRow=None
    app.clickedCol=None
    if blackInCheck(app):
        app.board[row][col]=temp
        app.board[clickedRow][clickedCol]=clicked
        app.clicked=clicked
        app.clickedRow=clickedRow
        app.clickedCol=clickedCol
        return False
    app.clicked=clicked
    app.clickedRow=clickedRow
    app.clickedCol=clickedCol
    app.board[row][col]=temp
    app.board[app.clickedRow][app.clickedCol]=app.clicked
    return True

def whiteInCheckmate(app):
    moves=[(1,1),(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(1,-1),(-1,1)]
    for row in range(len(app.board)):
        for col in range(len(app.board[0])):
            if app.board[row][col]=="WhiteKing":
                whiteKingRow=row
                whiteKingCol=col
    for move in moves:
        if (whiteKingRow+move[0]>=0 and whiteKingCol+move[1]>=0 and whiteKingRow+move[0]<8 and 
            whiteKingCol+move[1]<8 and (app.board[whiteKingRow+move[0]][whiteKingCol+move[1]]==None
        or 'Enpassant' in app.board[whiteKingRow+move[0]][whiteKingCol+move[1]])):
            app.board[whiteKingRow][whiteKingCol]=None
            app.board[whiteKingRow+move[0]][whiteKingCol+move[1]]='WhiteKing'
            if whiteInCheck(app):
                app.board[whiteKingRow][whiteKingCol]='WhiteKing'
                app.board[whiteKingRow+move[0]][whiteKingCol+move[1]]=None
                continue
            else:
                return False
    app.board[whiteKingRow][whiteKingCol]='WhiteKing'
    app.board[whiteKingRow+move[0]][whiteKingCol+move[1]]=None
    return True

def blackInCheckmate(app):
    moves=[(1,1),(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(1,-1),(-1,1)]
    for row in range(len(app.board)):
        for col in range(len(app.board[0])):
            if app.board[row][col]=="BlackKing":
                blackKingRow=row
                blackKingCol=col
    for move in moves:
        if (blackKingRow+move[0]>=0 and blackKingCol+move[1]>=0 and blackKingRow+move[0]<8 and 
            blackKingCol+move[1]<8 and (app.board[blackKingRow+move[0]][blackKingCol+move[1]]==None
        or 'Enpassant' in app.board[blackKingRow+move[0]][blackKingCol+move[1]])):
            app.board[blackKingRow][blackKingCol]=None
            app.board[blackKingRow+move[0]][blackKingCol+move[1]]='BlackKing'
            if blackInCheck(app):
                app.board[blackKingRow][blackKingCol]='BlackKing'
                app.board[blackKingRow+move[0]][blackKingCol+move[1]]=None
                continue
            else:
                return False
    app.board[blackKingRow][blackKingCol]='BlackKing'
    app.board[blackKingRow+move[0]][blackKingCol+move[1]]=None
    return True

# def onStep(app):
#     app.whiteInCheck=whiteInCheck(app)
#     app.blackInCheck=blackInCheck(app)

def main():
    runApp(800,800)

main()