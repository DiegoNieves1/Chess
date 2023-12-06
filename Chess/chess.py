from cmu_graphics import *
from imageManager import *
from board import Board
import os, pathlib

def onAppStart(app):
    loadImages(app)
    app.board=Board(app)
    # declaring and instantiating sounds that were gotten from
    # chess.com (https://images.chesscomfiles.com/chess-themes/sounds/_MP3_/default/move-check.mp3)
    # (https://images.chesscomfiles.com/chess-themes/sounds/_MP3_/default/capture.mp3)
    # (https://images.chesscomfiles.com/chess-themes/sounds/_MP3_/default/move-self.mp3)
    # (https://images.chesscomfiles.com/chess-themes/sounds/_WEBM_/default/game-end.webm)
    # i had to convert the game end file to mp3 with (https://pixabay.com/sound-effects/search/chess/)
    app.capture = loadSound("chessSounds/capture.mp3")
    app.check = loadSound("chessSounds/move-check.mp3")
    app.move = loadSound("chessSounds/move-self.mp3")
    app.checkmate = loadSound("chessSounds/game-end.mp3")
    app.playing = False
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
                
    # This if statement will create the square that shows up when white pieces are clicked
    # The color is straight from Chess.com
    if (app.board.clicked!=None and not ((app.board.clickedRow%2==0 and app.board.clickedCol%2==1) 
        or (app.board.clickedCol%2==0 and app.board.clickedRow%2==1)) and app.board.clickedRow!=None 
        and app.board.clickedCol!=None):
        drawRect(100+(app.board.boardWidthPixels/app.board.cols)*app.board.clickedCol,
                 100+(app.board.boardHeightPixels/app.board.rows)*app.board.clickedRow,
                 (app.board.boardHeightPixels/app.board.rows),(app.board.boardHeightPixels/app.board.cols),
                 fill=rgb(244,245,143))
    # This if statement will create the square that shows up when black pieces are clicked
    # The color is straight from Chess.com
    if (app.board.clicked!=None and ((app.board.clickedRow%2==0 and app.board.clickedCol%2==1) 
        or (app.board.clickedCol%2==0 and app.board.clickedRow%2==1)) and app.board.clickedRow!=None
        and app.board.clickedCol!=None):
        drawRect(100+(app.board.boardWidthPixels/app.board.cols)*app.board.clickedCol,
                 100+(app.board.boardHeightPixels/app.board.rows)*app.board.clickedRow,
                 (app.board.boardHeightPixels/app.board.rows),(app.board.boardHeightPixels/app.board.cols),
                 fill=rgb(185,203,84))

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
        app.board.movePiece(app,mouseX,mouseY)
    pass

def onKeyPress(app,key):
    # this is used to setup the shortcuts in the readme file
    if key=='r':
        app.board.reset()
    if key=='c':
        app.board.castleTest()
    if key=='d':
        app.board.castleTestAfterKingMoved()
    if key=='f':
        app.board.checkPosition()
    if key=='g':
        app.board.mateInOnePos()
    if key=='y':
        app.board.cantCastleIntoCheck()
    if key=='p':
        app.board.pawnPromotePos()

#this was gotten from the tech demo
#NOT MY CODE
def loadSound(relativePath):
    # Convert to absolute path (because pathlib.Path only takes absolute paths)
    absolutePath = os.path.abspath(relativePath)
    # Get local file URL
    url = pathlib.Path(absolutePath).as_uri()
    # Load Sound file from local URL
    return Sound(url)

def main():
    runApp(800,800)

main()