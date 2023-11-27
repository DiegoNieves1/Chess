from cmu_graphics import *
from PIL import Image


def loadImages(app):
    # Load the PIL image
    app.imageDict = {
        "BlackKing": "Piecesimages/BlackKing.png",
        "BlackQueen": "Piecesimages/BlackQueen.png",
        "BlackBishop": "Piecesimages/BlackBishop.png",
        "BlackKnight": "Piecesimages/BlackKnight.png",
        "BlackRook": "Piecesimages/BlackRook.png",
        "BlackPawn": "Piecesimages/BlackPawn.png",
        "WhiteKing": "Piecesimages/WhiteKing.png",
        "WhiteQueen": "Piecesimages/WhiteQueen.png",
        "WhiteBishop": "Piecesimages/WhiteBishop.png",
        "WhiteKnight": "Piecesimages/WhiteKnight.png",
        "WhiteRook": "Piecesimages/WhiteRook.png",
        "WhitePawn": "Piecesimages/WhitePawn.png"
    }

    for imgName in app.imageDict:
        fileName = app.imageDict[imgName]
        app.imageDict[imgName] = CMUImage(Image.open(fileName))
