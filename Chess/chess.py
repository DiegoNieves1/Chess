from cmu_graphics import *
from imageManager import *
from board import Board

def onAppStart(app):
    loadImages(app)
    app.board=Board(app)
    pass
def redrawAll(app):
    drawBoard(app)
    if app.board.whitePawnIsPromoting or app.board.blackPawnIsPromoting:
        drawPawnPromotionOptions(app)
    if app.board.whiteInCheck and app.board.whiteInCheckmate==False:
        drawLabel('White In Check!!!',app.width/2,50,size=40,fill='white', bold=True)
    if app.board.blackInCheck and app.board.blackInCheckmate==False:
        drawLabel('Black In Check!!!',app.width/2,50,size=40,fill='white', bold=True)
    if app.board.whiteInCheckmate==True:
        drawLabel('Black Wins!!!',app.width/2,50,size=40,fill='white',bold=True)
    if app.board.blackInCheckmate==True:
        drawLabel('White Wins!!!',app.width/2,50,size=40,fill='white',bold=True)
    pass

def drawBoard(app):

    #drawing background

    drawRect(0,0,app.width,app.height,fill=rgb(48,46,43))

    #drawing the turns on the board

    drawLabel(f'Move:{app.board.turn+1}',60,50,fill='white',size=30, bold=True)

    #these nested loops draw the colored squares in the same format as chess.com

    for row in range(app.board.rows):
        for col in range(app.board.cols):
            if (row%2==0 and col%2==1) or (col%2==0 and row%2==1):
                drawRect(100+(app.board.boardWidthPixels/app.board.rows)*row,
                        100+(app.board.boardHeightPixels/app.board.cols)*col,
                        (app.board.boardWidthPixels/app.board.rows),
                        (app.board.boardHeightPixels/app.board.cols),fill=rgb(115,148,90))
            else:
                drawRect(100+(app.board.boardWidthPixels/app.board.rows)*row,
                        100+(app.board.boardHeightPixels/app.board.cols)*col,
                        (app.board.boardWidthPixels/app.board.rows),
                        (app.board.boardHeightPixels/app.board.cols),fill=rgb(235,236,210))
    #these nested loops draw the pieces which are all copied from chess.com
    #images are from chess.com but I got them from https://github.com/lichess-org/lila/issues/3411
    #the background of the images were removed with https://www.remove.bg/
    for row in range(app.board.rows):
        for col in range(app.board.cols):
            if app.board.board[row][col]=='BlackKing':
                drawImage(app.imageDict['BlackKing'],
                          100+(app.board.boardWidthPixels/app.board.cols)*col,
                          100+(app.board.boardHeightPixels/app.board.rows)*row,
                    width=(app.board.boardWidthPixels/app.board.rows),
                    height=(app.board.boardHeightPixels/app.board.cols))
            elif app.board.board[row][col]=='BlackQueen':
                drawImage(app.imageDict['BlackQueen'],
                          100+(app.board.boardWidthPixels/app.board.cols)*col,
                          100+(app.board.boardHeightPixels/app.board.rows)*row,
                    width=(app.board.boardWidthPixels/app.board.rows),
                    height=(app.board.boardHeightPixels/app.board.cols))
            elif app.board.board[row][col]=='BlackBishop':
                drawImage(app.imageDict['BlackBishop'],
                          100+(app.board.boardWidthPixels/app.board.cols)*col,
                          100+(app.board.boardHeightPixels/app.board.rows)*row,
                    width=(app.board.boardWidthPixels/app.board.rows),
                    height=(app.board.boardHeightPixels/app.board.cols))
            elif app.board.board[row][col]=='BlackKnight':
                drawImage(app.imageDict['BlackKnight'],
                          100+(app.board.boardWidthPixels/app.board.cols)*col,
                          100+(app.board.boardHeightPixels/app.board.rows)*row,
                    width=(app.board.boardWidthPixels/app.board.rows),
                    height=(app.board.boardHeightPixels/app.board.cols))
            elif app.board.board[row][col]=='BlackRook':
                drawImage(app.imageDict['BlackRook'],
                          100+(app.board.boardWidthPixels/app.board.cols)*col,
                          100+(app.board.boardHeightPixels/app.board.rows)*row,
                    width=(app.board.boardWidthPixels/app.board.rows),
                    height=(app.board.boardHeightPixels/app.board.cols))
            elif app.board.board[row][col]=='BlackPawn':
                drawImage(app.imageDict['BlackPawn'],
                          100+(app.board.boardWidthPixels/app.board.cols)*col,
                          100+(app.board.boardHeightPixels/app.board.rows)*row,
                    width=(app.board.boardWidthPixels/app.board.rows),
                    height=(app.board.boardHeightPixels/app.board.cols))
            elif app.board.board[row][col]=='WhiteKing':
                drawImage(app.imageDict['WhiteKing'],
                          100+(app.board.boardWidthPixels/app.board.cols)*col,
                          100+(app.board.boardHeightPixels/app.board.rows)*row,
                    width=(app.board.boardWidthPixels/app.board.rows),
                    height=(app.board.boardHeightPixels/app.board.cols))
            elif app.board.board[row][col]=='WhiteQueen':
                drawImage(app.imageDict['WhiteQueen'],
                          100+(app.board.boardWidthPixels/app.board.cols)*col,
                          100+(app.board.boardHeightPixels/app.board.rows)*row,
                    width=(app.board.boardWidthPixels/app.board.rows),
                    height=(app.board.boardHeightPixels/app.board.cols))
            elif app.board.board[row][col]=='WhiteBishop':
                drawImage(app.imageDict['WhiteBishop'],
                          100+(app.board.boardWidthPixels/app.board.cols)*col,
                          100+(app.board.boardHeightPixels/app.board.rows)*row,
                    width=(app.board.boardWidthPixels/app.board.rows),
                    height=(app.board.boardHeightPixels/app.board.cols))
            elif app.board.board[row][col]=='WhiteKnight':
                drawImage(app.imageDict['WhiteKnight'],
                          100+(app.board.boardWidthPixels/app.board.cols)*col,
                          100+(app.board.boardHeightPixels/app.board.rows)*row,
                    width=(app.board.boardWidthPixels/app.board.rows),
                    height=(app.board.boardHeightPixels/app.board.cols))
            elif app.board.board[row][col]=='WhiteRook':
                drawImage(app.imageDict['WhiteRook'],
                          100+(app.board.boardWidthPixels/app.board.cols)*col,
                          100+(app.board.boardHeightPixels/app.board.rows)*row,
                    width=(app.board.boardWidthPixels/app.board.rows),
                    height=(app.board.boardHeightPixels/app.board.cols))
            elif app.board.board[row][col]=='WhitePawn':
                drawImage(app.imageDict['WhitePawn'],
                          100+(app.board.boardWidthPixels/app.board.cols)*col,
                          100+(app.board.boardHeightPixels/app.board.rows)*row,
                    width=(app.board.boardWidthPixels/app.board.rows),
                    height=(app.board.boardHeightPixels/app.board.cols))

def drawPawnPromotionOptions(app):
    if app.board.whitePawnIsPromoting:
        for i in range(len(app.board.whitePawnPromotionBoard)):
            drawImage(app.imageDict[app.board.whitePawnPromotionBoard[i]],
                            app.width-75,
                            app.height-50-(app.board.height-200)/(12/(i+1)),
                        width=(50),
                        height=(50))
    if app.board.blackPawnIsPromoting:
        for i in range(len(app.board.blackPawnPromotionBoard)):
            drawImage(app.imageDict[app.board.blackPawnPromotionBoard[i]],
                            app.width-75,
                            (app.height-200)/(12/(i+1)),
                        width=(50),
                        height=(50))

def onMousePress(app,mouseX,mouseY):
    if app.board.whitePawnIsPromoting or app.board.blackPawnIsPromoting:
        app.board.pawnPromotionClicks(mouseX,mouseY)
    else:
        app.board.movePiece(mouseX,mouseY)
    pass

def main():
    runApp(800,800)

main()