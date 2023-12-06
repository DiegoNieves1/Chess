class Board():
    def __init__(self,app):
        self.turn=0
        self.board=[['BlackRook','BlackKnight','BlackBishop','BlackQueen','BlackKing','BlackBishop','BlackKnight','BlackRook'],
                ['BlackPawn','BlackPawn','BlackPawn','BlackPawn','BlackPawn','BlackPawn','BlackPawn','BlackPawn'],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                ['WhitePawn','WhitePawn','WhitePawn','WhitePawn','WhitePawn','WhitePawn','WhitePawn','WhitePawn'],
                ['WhiteRook','WhiteKnight','WhiteBishop','WhiteQueen','WhiteKing','WhiteBishop','WhiteKnight','WhiteRook']]
        self.width=app.width
        self.height=app.height
        self.boardWidthPixels=(app.width-200)
        self.rows=len(self.board)
        self.boardHeightPixels=(app.height-200)
        self.cols=len(self.board[0])
        self.clicked=None
        self.clickedRow=None
        self.clickedCol=None
        self.whiteKingMoved=False
        self.blackKingMoved=False
        self.whiteRook1Moved=False
        self.whiteRook2Moved=False
        self.blackRook1Moved=False
        self.blackRook2Moved=False
        self.whitePawnIsPromoting=False
        self.blackPawnIsPromoting=False
        self.whiteInCheck=False
        self.blackInCheck=False
        self.whiteInCheckmate=False
        self.blackInCheckmate=False
        self.pieceCheckingWhite=None
        self.pieceCheckingWhiteRow=None
        self.pieceCheckingWhiteCol=None
        self.pieceCheckingBlack=None
        self.pieceCheckingBlackRow=None
        self.pieceCheckingBlackCol=None
        self.stepsPerSecond=5
        self.whitePawnPromotionBoard=['WhiteQueen','WhiteKnight','WhiteRook','WhiteBishop']
        self.blackPawnPromotionBoard=['BlackQueen','BlackKnight','BlackRook','BlackBishop']
        self.possibleMoves={ 'WhiteKing':[(1,0),(0,1),(1,1),(-1,-1),(-1,1),(1,-1),(-1,0),(0,-1)],
                            'WhiteBishop':[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),
                                    (-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),
                                    (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),
                                    (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8)],
                            'WhiteRook':[(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
                                    (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7),(0,-8),
                                    (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                                    (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),(-8,0)],
                            'WhiteQueen':[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),
                                    (-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),
                                    (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),
                                    (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8),
                                    (0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
                                    (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7),(0,-8),
                                    (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                                    (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),(-8,0)],
                            'WhiteKnight':[(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)],
                            'WhitePawn':[(2,0),(-2,0),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)],
                            'BlackKing':[(1,0),(0,1),(1,1),(-1,-1),(-1,1),(1,-1),(-1,0),(0,-1)],
                            'BlackBishop':[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),
                                    (-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),
                                    (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),
                                    (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8)],
                            'BlackRook':[(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
                                    (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7),(0,-8),
                                    (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                                    (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),(-8,0)],
                            'BlackQueen':[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),
                                    (-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),
                                    (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),
                                    (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8),
                                    (0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
                                    (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7),(0,-8),
                                    (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                                    (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),(-8,0)],
                            'BlackKnight':[(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)],
                            'BlackPawn':[(2,0),(-2,0),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]}
        
    # This function is for moving the pieces
    def movePiece(self,app,mouseX,mouseY):
        for row in range(self.rows):
            for col in range(self.cols):
                # setting up which piece was clicked if one is not already clicked
                # the if statement is checking whether the click is on a piece and if it is
                # sets up the pieces that got clicked so that it can be moved on the next click
                if ((mouseX>(100+(self.boardWidthPixels/self.cols)*col)
                and mouseX<((100+(self.boardWidthPixels/self.cols)*col)+self.boardWidthPixels/self.rows))
                and(mouseY>(100+(self.boardHeightPixels/self.rows)*row)
                and mouseY<((100+(self.boardHeightPixels/self.rows)*row)+self.boardHeightPixels/self.cols))
                and self.clicked==None):
                    self.clicked=self.board[row][col]
                    self.clickedRow=row
                    self.clickedCol=col
                # switching positions of piece and adding one to the turn
                # the if statement is checking whether the click is on a legal move
                # also adding a sound depending on the situation of the board
                elif ((mouseX>(100+(self.boardWidthPixels/self.cols)*col)
                and mouseX<((100+(self.boardWidthPixels/self.cols)*col)+self.boardWidthPixels/self.rows))
                and(mouseY>(100+(self.boardHeightPixels/self.rows)*row)
                and mouseY<((100+(self.boardHeightPixels/self.rows)*row)+self.boardHeightPixels/self.cols))
                and self.clicked!=None and self.isLegal(row,col)):
                    #playing capture sound if capturing
                    if self.board[row][col]!=None:
                        app.capture.play(restart=True)
                    self.board[self.clickedRow][self.clickedCol]=None
                    self.board[row][col]=self.clicked
                    self.turn+=1
                    self.clicked=None
                    self.clickedRow=None
                    self.clickedCol=None
                    self.whiteInCheck=self.isWhiteInCheck()
                    self.blackInCheck=self.isBlackInCheck()
                    if self.whiteInCheck==True:
                        self.whiteInCheckmate=self.isWhiteInCheckmate()
                    if self.blackInCheck==True:
                        self.blackInCheckmate=self.isBlackInCheckmate()
                    self.removeEnpassants()
                    #deciding which sound to play depending on what conditionals are met
                    if self.whiteInCheckmate or self.blackInCheckmate:
                        app.checkmate.play(restart = True)
                    elif self.whiteInCheck or self.blackInCheck:
                        app.check.play(restart = True)
                    else:
                        app.move.play(restart = True)
                
                # this if statement checks whether the player clicked on an empty non legal square after 
                # clicking some object and if unclicks the piece so that the player can pick new piece
                # to move
                elif ((mouseX>(100+(self.boardWidthPixels/self.cols)*col)
                and mouseX<((100+(self.boardWidthPixels/self.cols)*col)+self.boardWidthPixels/self.rows))
                and(mouseY>(100+(self.boardHeightPixels/self.rows)*row)
                and mouseY<((100+(self.boardHeightPixels/self.rows)*row)+self.boardHeightPixels/self.cols))
                and self.clicked!=None):
                    self.clicked=None
                    self.clickedRow=None
                    self.clickedCol=None

    def isLegal(self,row,col):

        # checking which colors turn it is and making sure the right one is the one playing a move
        if self.turn%2==0 and 'Black' in self.clicked:
            return False
        elif self.turn%2==1 and 'White' in self.clicked:
            return False

        # conditions for the white king to be able to move
        if (self.clicked == 'WhiteKing' and ((self.clickedCol-col<2
            and self.clickedCol-col>-2 and self.clickedRow-row<2
            and self.clickedRow-row>-2
            and self.nothingInWayDiagonally(row,col)
            and self.nothingInWayVerHornally(row,col)) or self.castle(row,col))
            and self.ifWhiteInCheck(row,col)):
            self.whiteKingMoved=True
            return True

        # conditions for the white queen to be able to move
        elif (self.clicked == 'WhiteQueen' and ((self.clickedRow==row or self.clickedCol==col)
                                            or (((self.clickedCol-col)/(self.clickedRow-row)==1)
                                                or ((self.clickedCol-col)/(self.clickedRow-row)==-1)))
                                                and self.nothingInWayDiagonally(row,col)
                                                and self.nothingInWayVerHornally(row,col)
                                                    and self.ifWhiteInCheck(row,col)):
            return True
        
        # conditions for the white bishop to be able to move
        elif (self.clicked == 'WhiteBishop' and self.clickedCol!=col
            and self.clickedRow!=row and (((self.clickedCol-col)/(self.clickedRow-row)==1)
                                        or ((self.clickedCol-col)/(self.clickedRow-row)==-1))
                                        and self.nothingInWayDiagonally(row,col)
                                            and self.ifWhiteInCheck(row,col)):
            return True
        
        # conditions for the white knight to be able to move
        elif (self.clicked == 'WhiteKnight' and ((self.clickedRow-row==1 
                                            and self.clickedCol-col==2) 
                                            or (self.clickedRow-row==-1 
                                            and self.clickedCol-col==-2) 
                                            or (self.clickedRow-row==1 
                                            and self.clickedCol-col==-2) 
                                            or (self.clickedRow-row==-1 
                                            and self.clickedCol-col==2)
                                            or (self.clickedCol-col==1
                                            and self.clickedRow-row==2)
                                            or (self.clickedCol-col==-1
                                            and self.clickedRow-row==-2)
                                            or (self.clickedCol-col==-1
                                            and self.clickedRow-row==2)
                                            or (self.clickedCol-col==1
                                            and self.clickedRow-row==-2))
                                            and self.knightHelper(row,col)
                                            and self.ifWhiteInCheck(row,col)):
            return True
        
        # conditions for the white rook to be able to move
        elif (self.clicked == 'WhiteRook' and (self.clickedRow==row or self.clickedCol==col)
            and self.nothingInWayVerHornally(row,col) and self.ifWhiteInCheck(row,col)):
            if self.clickedRow==7 and self.clickedCol==7:
                self.whiteRook1Moved=True
            if self.clickedRow==7 and self.clickedCol==0:
                self.whiteRook2Moved=True
            return True
        
        # conditions for the white pawn to be able to move
        elif (self.clicked == 'WhitePawn' and self.nothingInWayVerHornally(row,col)
            and self.pawnMoves(row,col) and self.ifWhiteInCheck(row,col)):
            self.pawnPromoting(row,col)
            return True
        
        # conditions for the black king to be able to move
        elif (self.clicked == 'BlackKing' and ((self.clickedCol-col<2
            and self.clickedCol-col>-2 and self.clickedRow-row<2
            and self.clickedRow-row>-2
            and self.nothingInWayDiagonally(row,col)
            and self.nothingInWayVerHornally(row,col)) or self.castle(row,col))
            and self.ifBlackInCheck(row,col)):
            self.blackKingMoved=True
            return True
        
        # conditions for the black queen to be able to move
        elif (self.clicked == 'BlackQueen' and ((self.clickedRow==row or self.clickedCol==col)
                                            or (((self.clickedCol-col)/(self.clickedRow-row)==1)
                                                or ((self.clickedCol-col)/(self.clickedRow-row)==-1)))
                                                and self.nothingInWayDiagonally(row,col)
                                                and self.nothingInWayVerHornally(row,col)
                                                and self.ifBlackInCheck(row,col)):
            return True
        
        # conditions for the black bishop to be able to move
        elif (self.clicked == 'BlackBishop' and self.clickedCol!=col
            and self.clickedRow!=row and (((self.clickedCol-col)/(self.clickedRow-row)==1)
                                        or ((self.clickedCol-col)/(self.clickedRow-row)==-1))
                                        and self.nothingInWayDiagonally(row,col)
                                        and self.ifBlackInCheck(row,col)):
            return True
        
        # conditions for the black knight to be able to move
        elif (self.clicked == 'BlackKnight' and ((self.clickedRow-row==1 
                                            and self.clickedCol-col==2) 
                                            or (self.clickedRow-row==-1 
                                            and self.clickedCol-col==-2) 
                                            or (self.clickedRow-row==1 
                                            and self.clickedCol-col==-2) 
                                            or (self.clickedRow-row==-1 
                                            and self.clickedCol-col==2)
                                            or (self.clickedCol-col==1
                                            and self.clickedRow-row==2)
                                            or (self.clickedCol-col==-1
                                            and self.clickedRow-row==-2)
                                            or (self.clickedCol-col==-1
                                            and self.clickedRow-row==2)
                                            or (self.clickedCol-col==1
                                            and self.clickedRow-row==-2))
                                            and self.knightHelper(row,col)
                                            and self.ifBlackInCheck(row,col)):
            return True
        
        # conditions for the black rook to be able to move
        elif (self.clicked == 'BlackRook' and (self.clickedRow==row or self.clickedCol==col)
            and self.nothingInWayVerHornally(row,col) and self.ifBlackInCheck(row,col)):
            if self.clickedRow==0 and self.clickedCol==7:
                self.blackRook1Moved=True
            if self.clickedRow==0 and self.clickedCol==0:
                self.blackRook2Moved=True
            return True
        
        # conditions for the black pawn to be able to move
        elif (self.clicked == 'BlackPawn' and self.nothingInWayVerHornally(row,col)
            and self.pawnMoves(row,col) and self.ifBlackInCheck(row,col)):
            self.pawnPromoting(row,col)
            return True
        return False
    
    def nothingInWayDiagonally(self,row,col):

        # checks for any pieces in the way of pieces moving diagonally 
        # so that the piece knows not to go

        verticalMovement= self.clickedRow-row
        horizontalMovement= col-self.clickedCol

        # checks if there is a same side piece on the spot that were moving to

        if (self.board[row][col] != None and self.clicked!=None 
            and 'Black' in self.clicked and 'Black' in self.board[row][col]):
            return False
        if (self.board[row][col] != None and self.clicked!=None 
            and 'White' in self.clicked and 'White' in self.board[row][col]):
            return False
        
        # this for loop is being used to check every block the piece
        # will have to traverse in order to know
        # if it has a piece there and returning False if it does 
        for i in range(1,abs(verticalMovement)):
            if verticalMovement>0 and horizontalMovement>0:
                if (self.board[self.clickedRow-i][self.clickedCol+i]!=None
                    and self.board[self.clickedRow-i][self.clickedCol+i]!='BlackEnpassant'
                    and self.board[self.clickedRow-i][self.clickedCol+i]!='WhiteEnpassant'):
                    return False
            elif verticalMovement<0 and horizontalMovement>0:
                if (self.board[self.clickedRow+i][self.clickedCol+i]!=None
                    and self.board[self.clickedRow+i][self.clickedCol+i]!='BlackEnpassant'
                    and self.board[self.clickedRow+i][self.clickedCol+i]!='WhiteEnpassant'):
                    return False
            elif verticalMovement>0 and horizontalMovement<0:
                if (self.board[self.clickedRow-i][self.clickedCol-i]!=None
                    and self.board[self.clickedRow-i][self.clickedCol-i]!='BlackEnpassant'
                    and self.board[self.clickedRow-i][self.clickedCol-i]!='WhiteEnpassant'):
                    return False
            elif verticalMovement<0 and horizontalMovement<0:
                if (self.board[self.clickedRow+i][self.clickedCol-i]!=None
                    and self.board[self.clickedRow+i][self.clickedCol-i]!='BlackEnpassant'
                    and self.board[self.clickedRow+i][self.clickedCol-i]!='WhiteEnpassant'):
                    return False
        return True
    
    def nothingInWayVerHornally(self,row,col):

        # This function checks if there are any pieces in the way of a verically/horizontally moving piece

        # verticalMovement gets set to the amount of spots that the piece is trying to move vertically
        # horizontalMovement gets set to the amount of spots that the piece is 
        # trying to move horizontally
        verticalMovement= self.clickedRow-row
        horizontalMovement= col-self.clickedCol

        # checks if there is a same side piece on the spot that were moving to

        if self.board[row][col] != None and self.clicked!=None and 'Black' in self.clicked and 'Black' in self.board[row][col]:
            return False
        if self.board[row][col] != None and self.clicked!=None and 'White' in self.clicked and 'White' in self.board[row][col]:
            return False
        
        if verticalMovement==0 and horizontalMovement>0:
            for i in range(1,abs(horizontalMovement)):
                # for loop checking every block the piece is trying to move over rightwards
                # in order to know if it has a piece there in the way and returning False if it 
                # trys to move over a piece
                if (self.board[self.clickedRow][self.clickedCol+i]!=None
                    and self.board[self.clickedRow][self.clickedCol+i]!='BlackEnpassant'
                    and self.board[self.clickedRow][self.clickedCol+i]!='WhiteEnpassant'):
                    return False
        elif verticalMovement==0 and horizontalMovement<0:
            for i in range(1,abs(horizontalMovement)):
                # for loop checking every block the piece is trying to move over leftwards
                # in order to know if it has a piece there in the way and returning False if it 
                # trys to move over a piece
                if (self.board[self.clickedRow][self.clickedCol-i]!=None
                    and self.board[self.clickedRow][self.clickedCol-i]!='BlackEnpassant'
                    and self.board[self.clickedRow][self.clickedCol-i]!='WhiteEnpassant'):
                    return False
        elif horizontalMovement==0 and verticalMovement>0:
            for i in range(1,abs(verticalMovement)):
                # for loop checking every block the piece is trying to move over upwards
                # in order to know if it has a piece there in the way and returning False if it 
                # trys to move over a piece
                if (self.board[self.clickedRow-i][self.clickedCol]!=None
                    and self.board[self.clickedRow-i][self.clickedCol]!='BlackEnpassant'
                    and self.board[self.clickedRow-i][self.clickedCol]!='WhiteEnpassant'):
                    return False
        elif horizontalMovement==0 and verticalMovement<0:
            for i in range(1,abs(verticalMovement)):
                # for loop checking every block the piece is trying to move over downwards
                # in order to know if it has a piece there in the way and returning False if it 
                # trys to move over a piece
                if (self.board[self.clickedRow+i][self.clickedCol]!=None
                    and self.board[self.clickedRow+i][self.clickedCol]!='BlackEnpassant'
                    and self.board[self.clickedRow+i][self.clickedCol]!='WhiteEnpassant'):
                    return False
        return True
    
    def pawnMoves(self,row,col):
        
        # checks if there are any pieces in the way of a verically/horizontally moving piece

        verticalMovement= self.clickedRow-row
        horizontalMovement= col-self.clickedCol

        # checks if the pawn can move 2 spaces and if it can it setsup an enpassant
        # behind the pawn
        if verticalMovement==2 and self.clickedRow==6 and self.clickedCol==col:
            self.board[row+1][col]='WhiteEnpassant'
            return True
        # checks if the pawn can move 2 spaces and if it can it setsup an enpassant
        # behind the pawn
        elif verticalMovement==-2 and self.clickedRow==1 and self.clickedCol==col:
            self.board[row-1][col]='BlackEnpassant'
            return True
        # checks if the pawn is moving more than 1 spot after checking that it
        # isnt doing one of the legal 2 spots moves so that it can return false
        # and confirm that it is an illegal move 
        elif abs(verticalMovement)>1:
            return False
        # checks to see if pawn is only moving one row in the right direction
        # and there is nothing in its way
        elif (verticalMovement==1 and horizontalMovement==0 and
        'WhitePawn'==self.clicked) and self.board[row][col]==None:
            return True
        # checks if pawn is trying to eat an enpassant so that it can remove
        # the pawn in aswell
        elif (verticalMovement==1 and abs(horizontalMovement)==1 and 'WhitePawn' == self.clicked
            and self.board[row][col]!=None):
            if self.board[row][col]=='BlackEnpassant':
                self.board[row+1][col]=None
            return True
        # checks to see if pawn is only moving one row in the right direction
        # and there is nothing in its way
        elif (verticalMovement==-1 and horizontalMovement==0 and
        'BlackPawn'==self.clicked and self.board[row][col]==None):
            return True
        # checks if pawn is trying to eat an enpassant so that it can remove
        # the pawn in aswell
        elif (verticalMovement==-1 and abs(horizontalMovement)==1 and 'BlackPawn' == self.clicked
            and self.board[row][col]!=None):
            if self.board[row][col]=='WhiteEnpassant':
                self.board[row-1][col]=None
            return True

    # This function is used to remove the enpassants that are not eaten
    # by a pawn after their creation
    def removeEnpassants(self):
        # removing white enpassants if it's white's turn again
        if self.turn%2==0:
            for row in range(len(self.board)):
                for col in range(len(self.board[0])):
                    if self.board[row][col]=='WhiteEnpassant':
                        self.board[row][col]=None
        # removing black enpassants if it's black's turn again
        elif self.turn%2==1:
            for row in range(len(self.board)):
                for col in range(len(self.board[0])):
                    if self.board[row][col]=='BlackEnpassant':
                        self.board[row][col]=None

    # checking if the player is making a valid castle
    def castle(self,row,col):

        # the conditional is checking if the player is making a valid castle
        # makes sure that they have not moved the king or rook
        # and makes sure that there is no pieces in between them
        # this for loop is for when white king castles king side
        if (self.board[7][7]=='WhiteRook' and ((row==7 and col==7)or(row==7 and col==6))
            and self.board[7][6]==None and self.board[7][5]==None
            and self.clickedRow==7 and self.clickedCol==4 and not self.whiteKingMoved 
            and not self.whiteRook1Moved and not self.whiteInCheck):
            self.whiteKingMoved=True
            self.board[7][5]='WhiteRook'
            self.board[7][6]='WhiteKing'
            self.board[7][7]=None
            self.board[self.clickedRow][self.clickedCol]=None
            clicked=self.clicked
            clickedRow=self.clickedRow
            clickedCol=self.clickedCol
            self.clicked=None
            self.clickedRow=None
            self.clickedCol=None

            # This conditional checks that the king will not go into check after the castle
            # if it does it doesnt allow the player to castle
            if self.isWhiteInCheck():
                self.clicked=clicked
                self.clickedRow=clickedRow
                self.clickedCol=clickedCol
                self.board[self.clickedRow][self.clickedCol]='WhiteKing'
                self.board[7][7]='WhiteRook'
                self.board[7][5]=None
                self.board[7][6]=None
                return False
            self.turn+=1
            return False
        
        # the conditional is checking if the player is making a valid castle
        # makes sure that they have not moved the king or rook
        # and makes sure that there is no pieces in between
        # this for loop is for when white king castles queen side
        elif (self.board[7][0]=='WhiteRook' and ((row==7 and col==0)or(row==7 and col==2))
            and self.board[7][1]==None and self.board[7][2]==None and self.board[7][3]==None
            and self.clickedRow==7 and self.clickedCol==4 and not self.whiteKingMoved
            and not self.whiteRook2Moved and not self.whiteInCheck):
            self.whiteKingMoved=True
            self.board[7][3]='WhiteRook'
            self.board[7][2]='WhiteKing'
            self.board[7][0]=None
            self.board[self.clickedRow][self.clickedCol]=None
            clicked=self.clicked
            clickedRow=self.clickedRow
            clickedCol=self.clickedCol
            self.clicked=None
            self.clickedRow=None
            self.clickedCol=None

            # This conditional checks that the king will not go into check after the castle
            # if it does it doesnt allow the player to castle
            if self.isWhiteInCheck():
                self.clicked=clicked
                self.clickedRow=clickedRow
                self.clickedCol=clickedCol
                self.board[self.clickedRow][self.clickedCol]='WhiteKing'
                self.board[7][0]='WhiteRook'
                self.board[7][3]=None
                self.board[7][2]=None
                return False
            self.turn+=1
            return False
        
        # the conditional is checking if the player is making a valid castle
        # makes sure that they have not moved the king or rook
        # and makes sure that there is no pieces in between
        # this for loop is for when black king castles king side
        elif (self.board[0][7]=='BlackRook' and ((row==0 and col==7)or(row==0 and col==6))
            and self.board[0][6]==None and self.board[0][5]==None
            and self.clickedRow==0 and self.clickedCol==4 and not self.blackKingMoved
            and not self.blackRook1Moved and not self.blackInCheck):
            self.blackKingMoved=True
            self.board[0][5]='BlackRook'
            self.board[0][6]='BlackKing'
            self.board[0][7]=None
            self.board[self.clickedRow][self.clickedCol]=None
            clicked=self.clicked
            clickedRow=self.clickedRow
            clickedCol=self.clickedCol
            self.clicked=None
            self.clickedRow=None
            self.clickedCol=None

            # This conditional checks that the king will not go into check after the castle
            # if it does it doesnt allow the player to castle
            if self.isBlackInCheck():
                self.clicked=clicked
                self.clickedRow=clickedRow
                self.clickedCol=clickedCol
                self.board[self.clickedRow][self.clickedCol]='BlackKing'
                self.board[0][7]='BlackRook'
                self.board[0][6]=None
                self.board[0][5]=None
                return False
            self.turn+=1
            return False
        
        # the conditional is checking if the player is making a valid castle
        # makes sure that they have not moved the king or rook
        # and makes sure that there is no pieces in between
        # this for loop is for when black castles queen side
        elif (self.board[0][0]=='BlackRook' and ((row==0 and col==0)or(row==0 and col==2))
            and self.board[0][1]==None and self.board[0][2]==None and self.board[0][3]==None
            and self.clickedRow==0 and self.clickedCol==4 and not self.blackKingMoved
            and not self.blackRook2Moved and not self.blackInCheck):
            self.blackKingMoved=True
            self.board[0][3]='BlackRook'
            self.board[0][2]='BlackKing'
            self.board[0][0]=None
            self.board[self.clickedRow][self.clickedCol]=None
            clicked=self.clicked
            clickedRow=self.clickedRow
            clickedCol=self.clickedCol
            self.clicked=None
            self.clickedRow=None
            self.clickedCol=None

            # This conditional checks that the king will not go into check after the castle
            # if it does it doesnt allow the player to castle
            if self.isBlackInCheck():
                self.clicked=clicked
                self.clickedRow=clickedRow
                self.clickedCol=clickedCol
                self.board[self.clickedRow][self.clickedCol]='BlackKing'
                self.board[0][0]='BlackRook'
                self.board[0][3]=None
                self.board[0][2]=None
                return False
            self.turn+=1
            return False
        return False
    
    # This function is used to check that the knight is not moving into a piece of it's own color
    # I made it seperate from the conditional to make the code more readable
    def knightHelper(self,row,col):
        if self.board[row][col] != None and 'Black' in self.clicked and 'Black' in self.board[row][col]:
            return False
        if self.board[row][col] != None and 'White' in self.clicked and 'White' in self.board[row][col]:
            return False
        return True
    
    # checks if the pawn can promote
    # essentially checks if it is moving to the opposite end of the board
    def pawnPromoting(self,row,col):
        if not(row>=0 and col>=0 and row<8 and col<8):
            return
        elif self.clickedRow==None or self.clickedCol==None:
            return
        if self.board[self.clickedRow][self.clickedCol]=='WhitePawn' and row==0:
            self.promotePawn()
        elif self.board[self.clickedRow][self.clickedCol]=='BlackPawn' and row==7:
            self.promotePawn()

    # sets the variable in charge of calling the pawn promotion function to true
    # so that it gets called and the player can pick a piece to upgrade it to
    def promotePawn(self):
        if self.board[self.clickedRow][self.clickedCol]=='WhitePawn':
            self.whitePawnIsPromoting=True
        if self.board[self.clickedRow][self.clickedCol]=='BlackPawn':
            self.blackPawnIsPromoting=True
    
    # manages where the player has to click on the board to make a piece promote
    def pawnPromotionClicks(self,mouseX,mouseY):

        #conditional for where to click to turn pawn into a bishop
        if (self.whitePawnIsPromoting and mouseX>self.width-75 and mouseX<self.width-25
            and mouseY>550 and mouseY<600):
            for i in range(len(self.board[0])):
                if self.board[0][i]=='WhitePawn':
                    self.board[0][i]='WhiteBishop'
                    self.whitePawnIsPromoting=False

        #conditional for where to click to turn pawn into a rook
        if (self.whitePawnIsPromoting and mouseX>self.width-75 and mouseX<self.width-25
            and mouseY>600 and mouseY<650):
            for i in range(len(self.board[0])):
                if self.board[0][i]=='WhitePawn':
                    self.board[0][i]='WhiteRook'
                    self.whitePawnIsPromoting=False
        
        #conditional for where to click to turn pawn into a knight
        if (self.whitePawnIsPromoting and mouseX>self.width-75 and mouseX<self.width-25
            and mouseY>650 and mouseY<700):
            for i in range(len(self.board[0])):
                if self.board[0][i]=='WhitePawn':
                    self.board[0][i]='WhiteKnight'
                    self.whitePawnIsPromoting=False
        
        #conditional for where to click to turn pawn into a queen
        if (self.whitePawnIsPromoting and mouseX>self.width-75 and mouseX<self.width-25
            and mouseY>700 and mouseY<750):
            for i in range(len(self.board[0])):
                if self.board[0][i]=='WhitePawn':
                    self.board[0][i]='WhiteQueen'
                    self.whitePawnIsPromoting=False
        
        #conditional for where to click to turn pawn into a bishop
        if (self.blackPawnIsPromoting and mouseX>self.width-75 and mouseX<self.width-25
            and mouseY>200 and mouseY<250):
            for i in range(len(self.board[0])):
                if self.board[7][i]=='BlackPawn':
                    self.board[7][i]='BlackBishop'
                    self.blackPawnIsPromoting=False
        
        #conditional for where to click to turn pawn into a rook
        if (self.blackPawnIsPromoting and mouseX>self.width-75 and mouseX<self.width-25
            and mouseY>150 and mouseY<200):
            for i in range(len(self.board[0])):
                if self.board[7][i]=='BlackPawn':
                    self.board[7][i]='BlackRook'
                    self.blackPawnIsPromoting=False
        
        #conditional for where to click to turn pawn into a knight
        if (self.blackPawnIsPromoting and mouseX>self.width-75 and mouseX<self.width-25
            and mouseY>100 and mouseY<150):
            for i in range(len(self.board[0])):
                if self.board[7][i]=='BlackPawn':
                    self.board[7][i]='BlackKnight'
                    self.blackPawnIsPromoting=False

            #conditional for where to click to turn pawn into a queen
        if (self.blackPawnIsPromoting and mouseX>self.width-75 and mouseX<self.width-25
            and mouseY>50 and mouseY<100):
            for i in range(len(self.board[0])):
                if self.board[7][i]=='BlackPawn':
                    self.board[7][i]='BlackQueen'
                    self.blackPawnIsPromoting=False
    
    # returns true if white is in check and false if not
    def isWhiteInCheck(self):
        # this loop finds the white kings position
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col]=='WhiteKing':
                    whiteKingRow=row
                    whiteKingCol=col
        # this loop finds all the black pieces
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if (self.board[row][col]!=None and 'Black' in self.board[row][col]
                    and 'Enpassant' not in self.board[row][col]):
                    # this conditional checks if it is a legal move for the black piece that
                    # the loop is currently looking at to move to where the king is
                    # because if the piece can move to the king then the king is in danger
                    # and it is in check
                    if self.isInCheck(row,col,whiteKingRow,whiteKingCol):
                        self.pieceCheckingWhite=self.board[row][col]
                        self.pieceCheckingWhiteRow=row
                        self.pieceCheckingWhiteCol=col
                        return True
                    else:
                        continue
        return False
    
    # returns true if black is in check and false if not
    def isBlackInCheck(self):
        # this loop finds the black kings position
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col]=='BlackKing':
                    blackKingRow=row
                    blackKingCol=col
        # this loop finds all the black pieces
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if (self.board[row][col]!=None and 'White' in self.board[row][col]
                    and 'Enpassant' not in self.board[row][col]):
                    # this conditional checks if it is a legal move for the white piece that
                    # the loop is currently looking at to move to where the king is
                    # because if the piece can move to the king then the king is in danger
                    # and it is in check
                    if self.isInCheck(row,col,blackKingRow,blackKingCol):
                        self.pieceCheckingBlack=self.board[row][col]
                        self.pieceCheckingBlackRow=row
                        self.pieceCheckingBlackCol=col
                        return True
                    else:
                        continue
        return False
    
    # helper function for checking if the king is in check
    # it takes in the kings position and the row and col of the
    # piece that we are checking, with these parameters it checks
    # if the king is in danger
    def isInCheck(self,row,col,kingRow,kingCol):

        # checking if the white king can move to where the black king is
        if (self.board[row][col] == 'WhiteKing' and ((col-kingCol<2
            and col-kingCol>-2 and row-kingRow<2
            and row-kingRow>-2
            and self.nothingInWayDiagonallyCheck(row,col,kingRow,kingCol)
            and self.nothingInWayVerHornallyCheck(row,col,kingRow,kingCol))
            or self.castle(kingRow,kingCol))):
            return True
        
        # checking if the white queen can move to where the black king is
        elif (self.board[row][col] == 'WhiteQueen' and ((row==kingRow or col==kingCol)
                                            or (((col-kingCol)/(row-kingRow)==1)
                                            or ((col-kingCol)/(row-kingRow)==-1)))
                                    and self.nothingInWayDiagonallyCheck(row,col,kingRow,kingCol)
                                    and self.nothingInWayVerHornallyCheck(row,col,kingRow,kingCol)):
            return True
        
        # checking if the white bishop can move to where the black king is
        elif (self.board[row][col] == 'WhiteBishop' and col!=kingCol
            and row!=kingRow and (((col-kingCol)/(row-kingRow)==1)
                                    or ((col-kingCol)/(row-kingRow)==-1))
                                    and self.nothingInWayDiagonallyCheck(row,col,kingRow,kingCol)):
            return True
        
        # checking if the white knight can move to where the black king is
        elif (self.board[row][col] == 'WhiteKnight' and ((row-kingRow==1 
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
                                            and self.knightHelperCheck(row,col,kingRow,kingCol)):
            return True
        
        # checking if the white rook can move to where the black king is
        elif (self.board[row][col] == 'WhiteRook' and (row==kingRow or col==kingCol)
            and self.nothingInWayVerHornallyCheck(row,col,kingRow,kingCol)):
            return True
        
        # checking if the white pawn can move to where the black king is
        elif (self.board[row][col] == 'WhitePawn' and 
            self.nothingInWayVerHornallyCheck(row,col,kingRow,kingCol)
            and self.pawnMovesCheck(row,col,kingRow,kingCol)):
            return True
        
        # checking if the black king can move to where the black king is
        elif (self.board[row][col] == 'BlackKing' and ((col-kingCol<2
            and col-kingCol>-2 and row-kingRow<2
            and row-kingRow>-2
            and self.nothingInWayDiagonallyCheck(row,col,kingRow,kingCol)
            and self.nothingInWayVerHornallyCheck(row,col,kingRow,kingCol))
            or self.castle(kingRow,kingCol))):
            return True
        
        # checking if the black queen can move to where the black king is
        elif (self.board[row][col] == 'BlackQueen' and ((row==kingRow or col==kingCol)
                                            or (((col-kingCol)/(row-kingRow)==1)
                                            or ((col-kingCol)/(row-kingRow)==-1)))
                                    and self.nothingInWayDiagonallyCheck(row,col,kingRow,kingCol)
                                    and self.nothingInWayVerHornallyCheck(row,col,kingRow,kingCol)):
            return True
        
        # checking if the black bishop can move to where the black king is
        elif (self.board[row][col] == 'BlackBishop' and col!=kingCol
            and row!=kingRow and (((col-kingCol)/(row-kingRow)==1)
                                    or ((col-kingCol)/(row-kingRow)==-1))
                                    and self.nothingInWayDiagonallyCheck(row,col,kingRow,kingCol)):
            return True
        
        # checking if the black knight can move to where the black king is
        elif (self.board[row][col] == 'BlackKnight' and ((row-kingRow==1 
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
                                            and self.knightHelperCheck(row,col,kingRow,kingCol)):
            return True
        
        # checking if the black rook can move to where the black king is
        elif (self.board[row][col] == 'BlackRook' and (row==kingRow or col==kingCol)
            and self.nothingInWayVerHornallyCheck(row,col,kingRow,kingCol)):
            return True
        
        # checking if the black pawn can move to where the black king is
        elif (self.board[row][col] == 'BlackPawn'
              and self.nothingInWayVerHornallyCheck(row,col,kingRow,kingCol)
            and self.pawnMovesCheck(row,col,kingRow,kingCol)):
            return True
        return False

    # this is a helper function for the check function that checks whether 
    # the piece inputed can move to where it is trying to
    # if the piece is moving vertically or horizontally
    def nothingInWayVerHornallyCheck(self,row,col,kingRow,kingCol):

        # This function checks if there are any pieces in the way
        # of a verically/horizontally moving piece

        #making sure that the rows and cols inputed are in the board
        if kingRow<0 or kingCol<0 or kingRow>=8 or kingCol>=8:
            return False
        elif row<0 or col<0 or row>=8 or col>=8:
            return False

        # verticalMovement gets set to the amount of spots that the piece is trying to move vertically
        # horizontalMovement gets set to the amount of spots that the piece is 
        # trying to move horizontally

        verticalMovement= row-kingRow
        horizontalMovement= kingCol-col

        # checks if there is a same side piece on the spot that were moving to

        if (self.board[kingRow][kingCol] != None and self.board[row][col]!=None 
        and 'Black' in self.board[row][col] and 'Black' in self.board[kingRow][kingCol]):
            return False
        if (self.board[kingRow][kingCol] != None and self.board[row][col]!=None 
            and 'White' in self.board[row][col] and 'White' in self.board[kingRow][kingCol]):
            return False
        
        # for loop checking every block the piece is trying to move over rightwards
        # in order to know if it has a piece there in the way and returning False if it 
        # trys to move over a piece
        if verticalMovement==0 and horizontalMovement>0:
            for i in range(1,abs(horizontalMovement)):
                if (self.board[row][col+i]!=None
                    and self.board[row][col+i]!='BlackEnpassant'
                    and self.board[row][col+i]!='WhiteEnpassant'):
                    return False
        # for loop checking every block the piece is trying to move over leftwards
        # in order to know if it has a piece there in the way and returning False if it 
        # trys to move over a piece
        elif verticalMovement==0 and horizontalMovement<0:
            for i in range(1,abs(horizontalMovement)):
                if (self.board[row][col-i]!=None
                    and self.board[row][col-i]!='BlackEnpassant'
                    and self.board[row][col-i]!='WhiteEnpassant'):
                    return False
        # for loop checking every block the piece is trying to move over upwards
        # in order to know if it has a piece there in the way and returning False if it 
        # trys to move over a piece
        elif horizontalMovement==0 and verticalMovement>0:
            for i in range(1,abs(verticalMovement)):
                if (self.board[row-i][col]!=None
                    and self.board[row-i][col]!='BlackEnpassant'
                    and self.board[row-i][col]!='WhiteEnpassant'):
                    return False
        # for loop checking every block the piece is trying to move over downwards
        # in order to know if it has a piece there in the way and returning False if it 
        # trys to move over a piece
        elif horizontalMovement==0 and verticalMovement<0:
            for i in range(1,abs(verticalMovement)):
                if (self.board[row+i][col]!=None
                    and self.board[row+i][col]!='BlackEnpassant'
                    and self.board[row+i][col]!='WhiteEnpassant'):
                    return False
        return True
    
    def nothingInWayDiagonallyCheck(self,row,col,kingRow,kingCol):
        
        if kingRow<0 or kingCol<0 or kingRow>=8 or kingCol>=8:
            return False
        elif row<0 or col<0 or row>=8 or col>=8:
            return False

        # checks for any pieces in the way of pieces moving 
        # diagonally so that the piece knows not to go

        verticalMovement= row-kingRow
        horizontalMovement= kingCol-col

        # checks if there is a same side piece on the spot that were moving to

        if (self.board[kingRow][kingCol] != None and self.board[row][col]!=None
        and 'Black' in self.board[row][col] and 'Black' in self.board[kingRow][kingCol]):
            return False
        if (self.board[kingRow][kingCol] != None and self.board[row][col]!=None
            and 'White' in self.board[row][col] and 'White' in self.board[kingRow][kingCol]):
            return False
        
        # this for loop is being used to check every block the piece
        # will have to traverse in order to know
        # if it has a piece there and returning False if it does 
        for i in range(1,abs(verticalMovement)):
            if verticalMovement>0 and horizontalMovement>0:
                if (self.board[row-i][col+i]!=None
                    and self.board[row-i][col+i]!='BlackEnpassant'
                    and self.board[row-i][col+i]!='WhiteEnpassant'):
                    return False
            elif verticalMovement<0 and horizontalMovement>0:
                if (self.board[row+i][col+i]!=None
                    and self.board[row+i][col+i]!='BlackEnpassant'
                    and self.board[row+i][col+i]!='WhiteEnpassant'):
                    return False
            elif verticalMovement>0 and horizontalMovement<0:
                if (self.board[row-i][col-i]!=None
                    and self.board[row-i][col-i]!='BlackEnpassant'
                    and self.board[row-i][col-i]!='WhiteEnpassant'):
                    return False
            elif verticalMovement<0 and horizontalMovement<0:
                if (self.board[row+i][col-i]!=None
                    and self.board[row+i][col-i]!='BlackEnpassant'
                    and self.board[row+i][col-i]!='WhiteEnpassant'):
                    return False
        return True
    
    # checks if the position that the knight is moving to doesnt have a same color piece on it
    def knightHelperCheck(self,row,col,kingRow,kingCol):

        if kingRow<0 or kingCol<0 or kingRow>=8 or kingCol>=8:
            return False
        elif row<0 or col<0 or row>=8 or col>=8:
            return False

        if self.board[kingRow][kingCol] != None and 'Black' in self.board[row][col] and 'Black' in self.board[kingRow][kingCol]:
            return False
        if self.board[kingRow][kingCol] != None and 'White' in self.board[row][col] and 'White' in self.board[kingRow][kingCol]:
            return False
        return True
    
    # checks if a legal move is being done by the pawn
    def pawnMovesCheck(self,row,col,kingRow,kingCol):
        
        # vertical movement is the amount of spaces vertically the pawn is moving
        # and horizontal movement is the amount of spaces horizontally the pawn is moving
        verticalMovement= row-kingRow
        horizontalMovement= kingCol-col

        # checks if the pawn can move 2 spaces and if it can it setsup an enpassant
        # behind the pawn
        if verticalMovement==2 and row==6 and col==kingCol:
            self.board[kingRow+1][kingCol]='WhiteEnpassant'
            return True
        # checks if the pawn can move 2 spaces and if it can it setsup an enpassant
        # behind the pawn
        elif verticalMovement==-2 and row==1 and col==kingCol:
            self.board[kingRow-1][kingCol]='BlackEnpassant'
            return True
        # checks if the pawn is moving more than 1 spot after checking that it
        # isnt doing one of the legal 2 spots moves so that it can return false
        # and confirm that it is an illegal move 
        elif abs(verticalMovement)>1:
            return False
        # checks to see if pawn is only moving one row in the right direction
        # and there is nothing in its way
        elif (verticalMovement==1 and horizontalMovement==0 and
        'WhitePawn'==self.board[row][col]) and self.board[kingRow][kingCol]==None:
            return True
        # checks if pawn is trying to eat an enpassant so that it can remove
        # the pawn in aswell
        elif (verticalMovement==1 and abs(horizontalMovement)==1 and 'WhitePawn' == self.board[row][col]
            and self.board[kingRow][kingCol]!=None):
            if self.board[kingRow][kingCol]=='BlackEnpassant':
                self.board[kingRow+1][kingCol]=None
            return True
        # checks to see if pawn is only moving one row in the right direction
        # and there is nothing in its way
        elif (verticalMovement==-1 and horizontalMovement==0 and
        'BlackPawn'==self.board[row][col] and self.board[kingRow][kingCol]==None):
            return True
        # checks if pawn is trying to eat an enpassant so that it can remove
        # the pawn in aswell
        elif (verticalMovement==-1 and abs(horizontalMovement)==1 and 'BlackPawn' == self.board[row][col]
            and self.board[kingRow][kingCol]!=None):
            if self.board[kingRow][kingCol]=='WhiteEnpassant':
                self.board[kingRow-1][kingCol]=None
            return True
    
    # If white in check is used in the islegal function to see 
    # if a move will make the king not be defended
    # from check anymore assuming the clicked piece moves
    def ifWhiteInCheck(self,row,col):
        # has value is used to make sure we only change self.clicked if it is not none
        # because isWhiteInCheck only works when self.clicked is none so if it's already none we dont
        # need to change anything but if it is we have to change it to self.
        hasValue=self.clickedCol!=None and self.clickedRow!=None and self.clicked!=None
        if hasValue and (row>=0 and col>=0 and row<8 and col<8):
            temp=self.board[row][col]
            self.board[row][col]=self.clicked
            self.board[self.clickedRow][self.clickedCol]=None
            clicked=self.clicked
            clickedRow=self.clickedRow
            clickedCol=self.clickedCol
            self.clicked=None
            self.clickedRow=None
            self.clickedCol=None
            #checking the move make the king be in check
            if self.isWhiteInCheck():
                if hasValue:
                    self.board[row][col]=temp
                    self.board[clickedRow][clickedCol]=clicked
                    self.clicked=clicked
                    self.clickedRow=clickedRow
                    self.clickedCol=clickedCol
                return False
            # this checks if the values were changed so that
            # if they were the values are turned back
            if hasValue:
                self.clicked=clicked
                self.clickedRow=clickedRow
                self.clickedCol=clickedCol
                self.board[row][col]=temp
                self.board[self.clickedRow][self.clickedCol]=self.clicked
            return True
        return False

    # If black in check is used in the islegal function to see 
    # if a move will make the king not be defended
    # from check anymore assuming the clicked piece moves
    def ifBlackInCheck(self,row,col):
        # has value is used to make sure we only change self.clicked if it is not none
        # because isBlackInCheck only works when self.clicked is none so if it's already none we dont
        # need to change anything but if it is we have to change it to self.
        hasValue=self.clickedCol!=None and self.clickedRow!=None and self.clicked!=None
        if hasValue and (row>=0 and col>=0 and row<8 and col<8):
            temp=self.board[row][col]
            self.board[row][col]=self.clicked
            self.board[self.clickedRow][self.clickedCol]=None
            clicked=self.clicked
            clickedRow=self.clickedRow
            clickedCol=self.clickedCol
            self.clicked=None
            self.clickedRow=None
            self.clickedCol=None
        #checking the move make the king be in check
        if self.isBlackInCheck():
            if hasValue:
                self.board[row][col]=temp
                self.board[clickedRow][clickedCol]=clicked
                self.clicked=clicked
                self.clickedRow=clickedRow
                self.clickedCol=clickedCol
            return False
        # this checks if the values were changed so that
        # if they were the values are turned back
        if hasValue:
            self.clicked=clicked
            self.clickedRow=clickedRow
            self.clickedCol=clickedCol
            self.board[row][col]=temp
            self.board[self.clickedRow][self.clickedCol]=self.clicked
        return True

    # returns whether the white king is in checkmate
    def isWhiteInCheckmate(self):
        # this for loop is used to find the position of the king
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col]=="WhiteKing":
                    whiteKingRow=row
                    whiteKingCol=col
        # this for loop checks that the king cannot move out of the check
        for move in self.possibleMoves['WhiteKing']:
            if (whiteKingRow+move[0]>=0 and whiteKingCol+move[1]>=0 and whiteKingRow+move[0]<8 and 
            whiteKingCol+move[1]<8 and (self.board[whiteKingRow+move[0]][whiteKingCol+move[1]]==None
            or 'Enpassant' in self.board[whiteKingRow+move[0]][whiteKingCol+move[1]]
            or 'Black' in self.board[whiteKingRow+move[0]][whiteKingCol+move[1]])):
                temp=self.board[whiteKingRow+move[0]][whiteKingCol+move[1]]
                self.board[whiteKingRow][whiteKingCol]=None
                self.board[whiteKingRow+move[0]][whiteKingCol+move[1]]='WhiteKing'
                if self.isWhiteInCheck():
                    self.board[whiteKingRow][whiteKingCol]='WhiteKing'
                    self.board[whiteKingRow+move[0]][whiteKingCol+move[1]]=temp
                    continue
                else:
                    self.board[whiteKingRow][whiteKingCol]='WhiteKing'
                    self.board[whiteKingRow+move[0]][whiteKingCol+move[1]]=temp
                    return False
        # this for loop checks if there are any pieces that can be moved in the
        # way of the check
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                temp=self.clicked
                tempRow=self.clickedRow
                tempCol=self.clickedCol
                self.clicked=self.board[row][col]
                self.clickedRow=row
                self.clickedCol=col
                #checking if the row and col that are being looked has a white piece
                if (self.board[row][col]!=None and 'White' in self.board[row][col]
                    and 'Enpassant' not in self.board[row][col]):
                    print(self.isInCheckmate(row,col,self.pieceCheckingWhiteRow,self.pieceCheckingWhiteCol))
                    if self.isInCheckmate(row,col,self.pieceCheckingWhiteRow,self.pieceCheckingWhiteCol):
                        self.clicked=temp
                        self.clickedRow=tempRow
                        self.clickedCol=tempCol
                        return False
                    # checking all the moves that the piece cheking the king can make
                    for move in self.possibleMoves[self.pieceCheckingWhite]:
                        print(self.isInCheckmate(row,col,self.pieceCheckingWhiteRow+move[0]
                                                 ,self.pieceCheckingWhiteCol+move[1]))
                        if self.isInCheckmate(row,col,self.pieceCheckingWhiteRow+move[0]
                                        ,self.pieceCheckingWhiteCol+move[1]):
                            self.clicked=temp
                            self.clickedRow=tempRow
                            self.clickedCol=tempCol
                            return False
        self.clicked=temp
        self.clickedRow=tempRow
        self.clickedCol=tempCol
        return True
    
    def isBlackInCheckmate(self):
        # this for loop is used to find the position of the king
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col]=="BlackKing":
                    blackKingRow=row
                    blackKingCol=col
        # this for loop checks that the king cannot move out of the check
        for move in self.possibleMoves['BlackKing']:
            if (blackKingRow+move[0]>=0 and blackKingCol+move[1]>=0 and blackKingRow+move[0]<8 and 
            blackKingCol+move[1]<8 and (self.board[blackKingRow+move[0]][blackKingCol+move[1]]==None
            or 'Enpassant' in self.board[blackKingRow+move[0]][blackKingCol+move[1]]
            or 'White' in self.board[blackKingRow+move[0]][blackKingCol+move[1]])):
                temp=self.board[blackKingRow+move[0]][blackKingCol+move[1]]
                self.board[blackKingRow][blackKingCol]=None
                self.board[blackKingRow+move[0]][blackKingCol+move[1]]='BlackKing'
                if self.isBlackInCheck():
                    self.board[blackKingRow][blackKingCol]='BlackKing'
                    self.board[blackKingRow+move[0]][blackKingCol+move[1]]=temp
                    continue
                else:
                    self.board[blackKingRow][blackKingCol]='BlackKing'
                    self.board[blackKingRow+move[0]][blackKingCol+move[1]]=temp
                    return False
        # this for loop checks if there are any pieces that can be moved in the
        # way of the check
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                temp=self.clicked
                tempRow=self.clickedRow
                tempCol=self.clickedCol
                self.clicked=self.board[row][col]
                self.clickedRow=row
                self.clickedCol=col
                #checking if the row and col that are being looked has a black piece
                if (self.board[row][col]!=None and 'Black' in self.board[row][col]
                    and 'Enpassant' not in self.board[row][col]):
                    print(self.isInCheckmate(row,col,self.pieceCheckingBlackRow,self.pieceCheckingBlackCol))
                    if self.isInCheckmate(row,col,self.pieceCheckingBlackRow,self.pieceCheckingBlackCol):
                        self.clicked=temp
                        self.clickedRow=tempRow
                        self.clickedCol=tempCol
                        return False
                    # checking all the moves that the piece cheking the king can make
                    for move in self.possibleMoves[self.pieceCheckingBlack]:
                        print(self.isInCheckmate(row,col,self.pieceCheckingBlackRow+move[0]
                                                 ,self.pieceCheckingBlackCol+move[1]))
                        if self.isInCheckmate(row,col,self.pieceCheckingBlackRow+move[0]
                                        ,self.pieceCheckingBlackCol+move[1]):
                            self.clicked=temp
                            self.clickedRow=tempRow
                            self.clickedCol=tempCol
                            return False
        self.clicked=temp
        self.clickedRow=tempRow
        self.clickedCol=tempCol
        return True

    def isInCheckmate(self,row,col,moveRow,moveCol):

        # checking if the king can move
        if (row>=0 and col>=0 and row<8 and col<8 
            and self.board[row][col] == 'WhiteKing' and (col-moveCol<2
            and col-moveCol>-2 and row-moveRow<2
            and row-moveRow>-2
            and self.nothingInWayDiagonallyCheck(row,col,moveRow,moveCol)
            and self.nothingInWayVerHornallyCheck(row,col,moveRow,moveCol))
            and self.ifWhiteInCheck(moveRow,moveCol)):
            return True
        
        # checking if the queen can move
        elif (self.board[row][col] == 'WhiteQueen' and row>=0 and col>=0 and row<8 and col<8
                                                    and ((row==moveRow or col==moveCol)
                                            or (((col-moveCol)/(row-moveRow)==1)
                                                or ((col-moveCol)/(row-moveRow)==-1)))
                                                and self.nothingInWayDiagonallyCheck(row,col,moveRow,moveCol)
                                                and self.nothingInWayVerHornallyCheck(row,col,moveRow,moveCol)
                                                and self.ifWhiteInCheck(moveRow,moveCol)):
            return True
        
        # checking if the bishop can move
        elif (self.board[row][col] == 'WhiteBishop' and row>=0 and col>=0 and row<8 and col<8
                                            and col!=moveCol
                                            and row!=moveRow and (((col-moveCol)/(row-moveRow)==1)
                                            or ((col-moveCol)/(row-moveRow)==-1))
                                            and self.nothingInWayDiagonallyCheck(row,col,moveRow,moveCol)
                                            and self.ifWhiteInCheck(moveRow,moveCol)):
            return True
        
        # checking if the knight can move
        elif (self.board[row][col] == 'WhiteKnight' and row>=0 and col>=0 and row<8 and col<8
                                            and ((row-moveRow==1 
                                            and col-moveCol==2) 
                                            or (row-moveRow==-1 
                                            and col-moveCol==-2) 
                                            or (row-moveRow==1 
                                            and col-moveCol==-2) 
                                            or (row-moveRow==-1 
                                            and col-moveCol==2)
                                            or (col-moveCol==1
                                            and row-moveRow==2)
                                            or (col-moveCol==-1
                                            and row-moveRow==-2)
                                            or (col-moveCol==-1
                                            and row-moveRow==2)
                                            or (col-moveCol==1
                                            and row-moveRow==-2))
                                            and self.knightHelperCheck(row,col,moveRow,moveCol)
                                            and self.ifWhiteInCheck(moveRow,moveCol)):
            return True
        
        # checking if the rook can move
        elif (self.board[row][col] == 'WhiteRook' and row>=0 and col>=0 and row<8 and col<8
            and (row==moveRow or col==moveCol)
            and self.nothingInWayVerHornallyCheck(row,col,moveRow,moveCol)
            and self.ifWhiteInCheck(moveRow,moveCol)):
            return True
        
        # checking if the pawn can move
        elif (self.board[row][col] == 'WhitePawn' and row>=0 and col>=0 and row<8 and col<8
            and self.nothingInWayVerHornallyCheck(row,col,moveRow,moveCol)
            and self.pawnMovesCheck(row,col,moveRow,moveCol) and self.ifWhiteInCheck(moveRow,moveCol)):
            self.pawnPromoting(moveRow,moveCol)
            return True
        
        # checking if the king can move
        elif (self.board[row][col] == 'BlackKing' and row>=0 and col>=0 and row<8 and col<8
            and (col-moveCol<2
            and col-moveCol>-2 and row-moveRow<2
            and row-moveRow>-2
            and self.nothingInWayDiagonallyCheck(row,col,moveRow,moveCol)
            and self.nothingInWayVerHornallyCheck(row,col,moveRow,moveCol)) 
            and self.ifBlackInCheck(moveRow,moveCol)):
            return True
        
        # checking if the queen can move
        elif (self.board[row][col] == 'BlackQueen' and row>=0 and col>=0 and row<8 and col<8 
                                                and ((row==moveRow or col==moveCol)
                                                or (((col-moveCol)/(row-moveRow)==1)
                                                or ((col-moveCol)/(row-moveRow)==-1)))
                                    and self.nothingInWayDiagonallyCheck(row,col,moveRow,moveCol)
                                    and self.nothingInWayVerHornallyCheck(row,col,moveRow,moveCol)
                                    and self.ifBlackInCheck(moveRow,moveCol)):
            return True
        
        # checking if the bishop can move
        elif (self.board[row][col] == 'BlackBishop' and row>=0 and col>=0 and row<8 and col<8
                                        and col!=moveCol
                                        and row!=moveRow and (((col-moveCol)/(row-moveRow)==1)
                                        or ((col-moveCol)/(row-moveRow)==-1))
                                    and self.nothingInWayDiagonallyCheck(row,col,moveRow,moveCol)
                                    and self.ifBlackInCheck(moveRow,moveCol)):
            return True
        
        # checking if the knight can move
        elif (self.board[row][col] == 'BlackKnight' and row>=0 and col>=0 and row<8 and col<8
                                            and ((row-moveRow==1 
                                            and col-moveCol==2) 
                                            or (row-moveRow==-1 
                                            and col-moveCol==-2) 
                                            or (row-moveRow==1 
                                            and col-moveCol==-2) 
                                            or (row-moveRow==-1 
                                            and col-moveCol==2)
                                            or (col-moveCol==1
                                            and row-moveRow==2)
                                            or (col-moveCol==-1
                                            and row-moveRow==-2)
                                            or (col-moveCol==-1
                                            and row-moveRow==2)
                                            or (col-moveCol==1
                                            and row-moveRow==-2))
                                            and self.knightHelperCheck(row,col,moveRow,moveCol)
                                            and self.ifBlackInCheck(moveRow,moveCol)):
            return True
        
        # checking if the rook can move
        elif (self.board[row][col] == 'BlackRook' and row>=0 and col>=0 and row<8 and col<8
            and (row==moveRow or col==moveCol)
            and self.nothingInWayVerHornallyCheck(row,col,moveRow,moveCol)
            and self.ifBlackInCheck(moveRow,moveCol)):
            return True
        
        # checking if the pawn can move
        elif (self.board[row][col] == 'BlackPawn' and row>=0 and col>=0 and row<8 and col<8
            and self.nothingInWayVerHornallyCheck(row,col,moveRow,moveCol)
            and self.pawnMovesCheck(row,col,moveRow,moveCol)
            and self.ifBlackInCheck(moveRow,moveCol)):
            self.pawnPromoting(moveRow,moveCol)
            return True
        return False

    # this function will just set the board to its initial position if r is pressed
    def reset(self):
        self.turn=0
        self.board=[['BlackRook','BlackKnight','BlackBishop','BlackQueen','BlackKing','BlackBishop','BlackKnight','BlackRook'],
                ['BlackPawn','BlackPawn','BlackPawn','BlackPawn','BlackPawn','BlackPawn','BlackPawn','BlackPawn'],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                ['WhitePawn','WhitePawn','WhitePawn','WhitePawn','WhitePawn','WhitePawn','WhitePawn','WhitePawn'],
                ['WhiteRook','WhiteKnight','WhiteBishop','WhiteQueen','WhiteKing','WhiteBishop','WhiteKnight','WhiteRook']]
        self.boardWidthPixels=(self.width-200)
        self.rows=len(self.board)
        self.boardHeightPixels=(self.height-200)
        self.cols=len(self.board[0])
        self.clicked=None
        self.clickedRow=None
        self.clickedCol=None
        self.whiteKingMoved=False
        self.blackKingMoved=False
        self.whiteRook1Moved=False
        self.whiteRook2Moved=False
        self.blackRook1Moved=False
        self.blackRook2Moved=False
        self.whitePawnIsPromoting=False
        self.blackPawnIsPromoting=False
        self.whiteInCheck=False
        self.blackInCheck=False
        self.whiteInCheckmate=False
        self.blackInCheckmate=False
        self.pieceCheckingWhite=None
        self.pieceCheckingWhiteRow=None
        self.pieceCheckingWhiteCol=None
        self.pieceCheckingBlack=None
        self.pieceCheckingBlackRow=None
        self.pieceCheckingBlackCol=None
        self.stepsPerSecond=5
        self.whitePawnPromotionBoard=['WhiteQueen','WhiteKnight','WhiteRook','WhiteBishop']
        self.blackPawnPromotionBoard=['BlackQueen','BlackKnight','BlackRook','BlackBishop']
        self.possibleMoves={ 'WhiteKing':[(1,0),(0,1),(1,1),(-1,-1),(-1,1),(1,-1),(-1,0),(0,-1)],
                            'WhiteBishop':[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),
                                    (-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),
                                    (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),
                                    (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8)],
                            'WhiteRook':[(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
                                    (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7),(0,-8),
                                    (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                                    (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),(-8,0)],
                            'WhiteQueen':[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),
                                    (-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),
                                    (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),
                                    (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8),
                                    (0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
                                    (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7),(0,-8),
                                    (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                                    (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),(-8,0)],
                            'WhiteKnight':[(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)],
                            'WhitePawn':[(2,0),(-2,0),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)],
                            'BlackKing':[(1,0),(0,1),(1,1),(-1,-1),(-1,1),(1,-1),(-1,0),(0,-1)],
                            'BlackBishop':[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),
                                    (-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),
                                    (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),
                                    (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8)],
                            'BlackRook':[(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
                                    (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7),(0,-8),
                                    (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                                    (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),(-8,0)],
                            'BlackQueen':[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),
                                    (-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),
                                    (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),
                                    (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8),
                                    (0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
                                    (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7),(0,-8),
                                    (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                                    (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),(-8,0)],
                            'BlackKnight':[(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)],
                            'BlackPawn':[(2,0),(-2,0),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]}
    
    # this function will set the board to test castling if c is pressed
    def castleTest(self):
        self.turn=0
        self.board=[['BlackRook','BlackKnight','BlackBishop','BlackQueen','BlackKing','BlackBishop','BlackKnight','BlackRook'],
                ['BlackPawn','BlackPawn','BlackPawn','BlackPawn','BlackPawn','BlackPawn','BlackPawn','BlackPawn'],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                ['WhitePawn','WhitePawn','WhitePawn','WhitePawn','WhitePawn','WhitePawn','WhitePawn','WhitePawn'],
                ['WhiteRook','WhiteKnight','WhiteBishop','WhiteQueen','WhiteKing',None,None,'WhiteRook']]
        self.clicked=None
        self.clickedRow=None
        self.clickedCol=None
        self.whiteKingMoved=False
        self.blackKingMoved=False
        self.whiteRook1Moved=False
        self.whiteRook2Moved=False
        self.blackRook1Moved=False
        self.blackRook2Moved=False
        self.whitePawnIsPromoting=False
        self.blackPawnIsPromoting=False
        self.whiteInCheck=False
        self.blackInCheck=False
        self.whiteInCheckmate=False
        self.blackInCheckmate=False
        self.pieceCheckingWhite=None
        self.pieceCheckingWhiteRow=None
        self.pieceCheckingWhiteCol=None
        self.pieceCheckingBlack=None
        self.pieceCheckingBlackRow=None
        self.pieceCheckingBlackCol=None
        self.stepsPerSecond=5
        self.whitePawnPromotionBoard=['WhiteQueen','WhiteKnight','WhiteRook','WhiteBishop']
        self.blackPawnPromotionBoard=['BlackQueen','BlackKnight','BlackRook','BlackBishop']
        self.possibleMoves={ 'WhiteKing':[(1,0),(0,1),(1,1),(-1,-1),(-1,1),(1,-1),(-1,0),(0,-1)],
                            'WhiteBishop':[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),
                                    (-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),
                                    (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),
                                    (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8)],
                            'WhiteRook':[(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
                                    (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7),(0,-8),
                                    (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                                    (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),(-8,0)],
                            'WhiteQueen':[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),
                                    (-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),
                                    (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),
                                    (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8),
                                    (0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
                                    (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7),(0,-8),
                                    (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                                    (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),(-8,0)],
                            'WhiteKnight':[(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)],
                            'WhitePawn':[(2,0),(-2,0),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)],
                            'BlackKing':[(1,0),(0,1),(1,1),(-1,-1),(-1,1),(1,-1),(-1,0),(0,-1)],
                            'BlackBishop':[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),
                                    (-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),
                                    (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),
                                    (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8)],
                            'BlackRook':[(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
                                    (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7),(0,-8),
                                    (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                                    (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),(-8,0)],
                            'BlackQueen':[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),
                                    (-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),
                                    (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),
                                    (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8),
                                    (0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
                                    (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7),(0,-8),
                                    (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                                    (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),(-8,0)],
                            'BlackKnight':[(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)],
                            'BlackPawn':[(2,0),(-2,0),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]}
        
    # this function will set the board to show you cannot castle if the king already moved
    # after pressing d
    def castleTestAfterKingMoved(self):
        self.turn=0
        self.board=[['BlackRook','BlackKnight','BlackBishop','BlackQueen','BlackKing','BlackBishop','BlackKnight','BlackRook'],
                ['BlackPawn','BlackPawn','BlackPawn','BlackPawn','BlackPawn','BlackPawn','BlackPawn','BlackPawn'],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                ['WhiteRook','WhiteKnight','WhiteBishop','WhiteQueen','WhiteKing',None,None,'WhiteRook']]
        self.clicked=None
        self.clickedRow=None
        self.clickedCol=None
        self.whiteKingMoved=True
        self.blackKingMoved=False
        self.whiteRook1Moved=False
        self.whiteRook2Moved=False
        self.blackRook1Moved=False
        self.blackRook2Moved=False
        self.whitePawnIsPromoting=False
        self.blackPawnIsPromoting=False
        self.whiteInCheck=False
        self.blackInCheck=False
        self.whiteInCheckmate=False
        self.blackInCheckmate=False
        self.pieceCheckingWhite=None
        self.pieceCheckingWhiteRow=None
        self.pieceCheckingWhiteCol=None
        self.pieceCheckingBlack=None
        self.pieceCheckingBlackRow=None
        self.pieceCheckingBlackCol=None
        self.stepsPerSecond=5
        self.whitePawnPromotionBoard=['WhiteQueen','WhiteKnight','WhiteRook','WhiteBishop']
        self.blackPawnPromotionBoard=['BlackQueen','BlackKnight','BlackRook','BlackBishop']
        self.possibleMoves={ 'WhiteKing':[(1,0),(0,1),(1,1),(-1,-1),(-1,1),(1,-1),(-1,0),(0,-1)],
                            'WhiteBishop':[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),
                                    (-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),
                                    (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),
                                    (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8)],
                            'WhiteRook':[(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
                                    (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7),(0,-8),
                                    (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                                    (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),(-8,0)],
                            'WhiteQueen':[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),
                                    (-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),
                                    (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),
                                    (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8),
                                    (0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
                                    (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7),(0,-8),
                                    (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                                    (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),(-8,0)],
                            'WhiteKnight':[(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)],
                            'WhitePawn':[(2,0),(-2,0),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)],
                            'BlackKing':[(1,0),(0,1),(1,1),(-1,-1),(-1,1),(1,-1),(-1,0),(0,-1)],
                            'BlackBishop':[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),
                                    (-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),
                                    (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),
                                    (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8)],
                            'BlackRook':[(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
                                    (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7),(0,-8),
                                    (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                                    (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),(-8,0)],
                            'BlackQueen':[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),
                                    (-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),
                                    (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),
                                    (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8),
                                    (0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
                                    (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7),(0,-8),
                                    (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                                    (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),(-8,0)],
                            'BlackKnight':[(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)],
                            'BlackPawn':[(2,0),(-2,0),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]}
    
    # this function will just set the board to be one move away from check if f is pressed
    def checkPosition(self):
        self.turn=1
        self.board=[['BlackRook','BlackKnight','BlackBishop','BlackQueen','BlackKing',None,'BlackKnight','BlackRook'],
                ['BlackPawn','BlackPawn','BlackPawn','BlackPawn','BlackPawn','BlackPawn','BlackPawn','BlackPawn'],
                [None,None,None,None,None,None,None,None],
                [None,None,'BlackBishop',None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                ['WhiteRook','WhiteKnight','WhiteBishop','WhiteQueen','WhiteKing',None,None,'WhiteRook']]
        self.clicked=None
        self.clickedRow=None
        self.clickedCol=None
        self.whiteKingMoved=False
        self.blackKingMoved=False
        self.whiteRook1Moved=False
        self.whiteRook2Moved=False
        self.blackRook1Moved=False
        self.blackRook2Moved=False
        self.whitePawnIsPromoting=False
        self.blackPawnIsPromoting=False
        self.whiteInCheck=False
        self.blackInCheck=False
        self.whiteInCheckmate=False
        self.blackInCheckmate=False
        self.pieceCheckingWhite=None
        self.pieceCheckingWhiteRow=None
        self.pieceCheckingWhiteCol=None
        self.pieceCheckingBlack=None
        self.pieceCheckingBlackRow=None
        self.pieceCheckingBlackCol=None
        self.stepsPerSecond=5
        self.whitePawnPromotionBoard=['WhiteQueen','WhiteKnight','WhiteRook','WhiteBishop']
        self.blackPawnPromotionBoard=['BlackQueen','BlackKnight','BlackRook','BlackBishop']
        self.possibleMoves={ 'WhiteKing':[(1,0),(0,1),(1,1),(-1,-1),(-1,1),(1,-1),(-1,0),(0,-1)],
                            'WhiteBishop':[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),
                                    (-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),
                                    (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),
                                    (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8)],
                            'WhiteRook':[(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
                                    (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7),(0,-8),
                                    (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                                    (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),(-8,0)],
                            'WhiteQueen':[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),
                                    (-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),
                                    (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),
                                    (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8),
                                    (0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
                                    (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7),(0,-8),
                                    (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                                    (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),(-8,0)],
                            'WhiteKnight':[(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)],
                            'WhitePawn':[(2,0),(-2,0),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)],
                            'BlackKing':[(1,0),(0,1),(1,1),(-1,-1),(-1,1),(1,-1),(-1,0),(0,-1)],
                            'BlackBishop':[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),
                                    (-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),
                                    (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),
                                    (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8)],
                            'BlackRook':[(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
                                    (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7),(0,-8),
                                    (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                                    (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),(-8,0)],
                            'BlackQueen':[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),
                                    (-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),
                                    (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),
                                    (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8),
                                    (0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
                                    (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7),(0,-8),
                                    (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                                    (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),(-8,0)],
                            'BlackKnight':[(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)],
                            'BlackPawn':[(2,0),(-2,0),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]}
    
    # this function will set the board to be one move away from checkmate if g is pressed
    def mateInOnePos(self):
        self.turn=1
        self.board=[[None,None,'BlackKing','BlackRook',None,'BlackRook',None,None],
                [None,None,None,None,None,'BlackRook',None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                ['WhiteRook','WhiteKnight',None,None,'WhiteKing',None,None,'WhiteRook']]
        self.clicked=None
        self.clickedRow=None
        self.clickedCol=None
        self.whiteKingMoved=False
        self.blackKingMoved=False
        self.whiteRook1Moved=False
        self.whiteRook2Moved=False
        self.blackRook1Moved=False
        self.blackRook2Moved=False
        self.whitePawnIsPromoting=False
        self.blackPawnIsPromoting=False
        self.whiteInCheck=False
        self.blackInCheck=False
        self.whiteInCheckmate=False
        self.blackInCheckmate=False
        self.pieceCheckingWhite=None
        self.pieceCheckingWhiteRow=None
        self.pieceCheckingWhiteCol=None
        self.pieceCheckingBlack=None
        self.pieceCheckingBlackRow=None
        self.pieceCheckingBlackCol=None
        self.stepsPerSecond=5
        self.whitePawnPromotionBoard=['WhiteQueen','WhiteKnight','WhiteRook','WhiteBishop']
        self.blackPawnPromotionBoard=['BlackQueen','BlackKnight','BlackRook','BlackBishop']
        self.possibleMoves={ 'WhiteKing':[(1,0),(0,1),(1,1),(-1,-1),(-1,1),(1,-1),(-1,0),(0,-1)],
                            'WhiteBishop':[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),
                                    (-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),
                                    (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),
                                    (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8)],
                            'WhiteRook':[(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
                                    (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7),(0,-8),
                                    (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                                    (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),(-8,0)],
                            'WhiteQueen':[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),
                                    (-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),
                                    (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),
                                    (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8),
                                    (0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
                                    (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7),(0,-8),
                                    (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                                    (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),(-8,0)],
                            'WhiteKnight':[(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)],
                            'WhitePawn':[(2,0),(-2,0),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)],
                            'BlackKing':[(1,0),(0,1),(1,1),(-1,-1),(-1,1),(1,-1),(-1,0),(0,-1)],
                            'BlackBishop':[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),
                                    (-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),
                                    (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),
                                    (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8)],
                            'BlackRook':[(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
                                    (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7),(0,-8),
                                    (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                                    (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),(-8,0)],
                            'BlackQueen':[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),
                                    (-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),
                                    (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),
                                    (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8),
                                    (0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
                                    (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7),(0,-8),
                                    (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                                    (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),(-8,0)],
                            'BlackKnight':[(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)],
                            'BlackPawn':[(2,0),(-2,0),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]}
    
    # this function will set the board to be in a position that shows you cannot castle
    # into check, it will be triggered when y is pressed
    def cantCastleIntoCheck(self):
        self.turn=0
        self.board=[[None,None,'BlackKing',None,None,None,'BlackRook',None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                ['WhiteRook','WhiteKnight',None,None,'WhiteKing',None,None,'WhiteRook']]
        self.clicked=None
        self.clickedRow=None
        self.clickedCol=None
        self.whiteKingMoved=False
        self.blackKingMoved=False
        self.whiteRook1Moved=False
        self.whiteRook2Moved=False
        self.blackRook1Moved=False
        self.blackRook2Moved=False
        self.whitePawnIsPromoting=False
        self.blackPawnIsPromoting=False
        self.whiteInCheck=False
        self.blackInCheck=False
        self.whiteInCheckmate=False
        self.blackInCheckmate=False
        self.pieceCheckingWhite=None
        self.pieceCheckingWhiteRow=None
        self.pieceCheckingWhiteCol=None
        self.pieceCheckingBlack=None
        self.pieceCheckingBlackRow=None
        self.pieceCheckingBlackCol=None
        self.stepsPerSecond=5
        self.whitePawnPromotionBoard=['WhiteQueen','WhiteKnight','WhiteRook','WhiteBishop']
        self.blackPawnPromotionBoard=['BlackQueen','BlackKnight','BlackRook','BlackBishop']
        self.possibleMoves={ 'WhiteKing':[(1,0),(0,1),(1,1),(-1,-1),(-1,1),(1,-1),(-1,0),(0,-1)],
                            'WhiteBishop':[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),
                                    (-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),
                                    (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),
                                    (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8)],
                            'WhiteRook':[(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
                                    (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7),(0,-8),
                                    (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                                    (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),(-8,0)],
                            'WhiteQueen':[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),
                                    (-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),
                                    (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),
                                    (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8),
                                    (0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
                                    (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7),(0,-8),
                                    (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                                    (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),(-8,0)],
                            'WhiteKnight':[(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)],
                            'WhitePawn':[(2,0),(-2,0),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)],
                            'BlackKing':[(1,0),(0,1),(1,1),(-1,-1),(-1,1),(1,-1),(-1,0),(0,-1)],
                            'BlackBishop':[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),
                                    (-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),
                                    (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),
                                    (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8)],
                            'BlackRook':[(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
                                    (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7),(0,-8),
                                    (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                                    (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),(-8,0)],
                            'BlackQueen':[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),
                                    (-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),
                                    (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),
                                    (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8),
                                    (0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
                                    (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7),(0,-8),
                                    (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                                    (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),(-8,0)],
                            'BlackKnight':[(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)],
                            'BlackPawn':[(2,0),(-2,0),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]}
    
    # this function will set the board to be in a position that shows you can promote pawns,
    # it will be triggered when y is pressed
    def pawnPromotePos(self):
        self.turn=0
        self.board=[[None,'BlackKing','BlackKnight',None,None,None,None,None],
                [None,None,None,None,'WhitePawn',None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,'WhiteKing',None,None,None,None]]
        self.clicked=None
        self.clickedRow=None
        self.clickedCol=None
        self.whiteKingMoved=False
        self.blackKingMoved=False
        self.whiteRook1Moved=False
        self.whiteRook2Moved=False
        self.blackRook1Moved=False
        self.blackRook2Moved=False
        self.whitePawnIsPromoting=False
        self.blackPawnIsPromoting=False
        self.whiteInCheck=False
        self.blackInCheck=False
        self.whiteInCheckmate=False
        self.blackInCheckmate=False
        self.pieceCheckingWhite=None
        self.pieceCheckingWhiteRow=None
        self.pieceCheckingWhiteCol=None
        self.pieceCheckingBlack=None
        self.pieceCheckingBlackRow=None
        self.pieceCheckingBlackCol=None
        self.stepsPerSecond=5
        self.whitePawnPromotionBoard=['WhiteQueen','WhiteKnight','WhiteRook','WhiteBishop']
        self.blackPawnPromotionBoard=['BlackQueen','BlackKnight','BlackRook','BlackBishop']
        self.possibleMoves={ 'WhiteKing':[(1,0),(0,1),(1,1),(-1,-1),(-1,1),(1,-1),(-1,0),(0,-1)],
                            'WhiteBishop':[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),
                                    (-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),
                                    (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),
                                    (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8)],
                            'WhiteRook':[(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
                                    (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7),(0,-8),
                                    (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                                    (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),(-8,0)],
                            'WhiteQueen':[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),
                                    (-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),
                                    (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),
                                    (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8),
                                    (0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
                                    (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7),(0,-8),
                                    (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                                    (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),(-8,0)],
                            'WhiteKnight':[(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)],
                            'WhitePawn':[(2,0),(-2,0),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)],
                            'BlackKing':[(1,0),(0,1),(1,1),(-1,-1),(-1,1),(1,-1),(-1,0),(0,-1)],
                            'BlackBishop':[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),
                                    (-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),
                                    (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),
                                    (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8)],
                            'BlackRook':[(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
                                    (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7),(0,-8),
                                    (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                                    (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),(-8,0)],
                            'BlackQueen':[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),
                                    (-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),
                                    (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),
                                    (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8),
                                    (0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
                                    (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7),(0,-8),
                                    (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                                    (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),(-8,0)],
                            'BlackKnight':[(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)],
                            'BlackPawn':[(2,0),(-2,0),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]}