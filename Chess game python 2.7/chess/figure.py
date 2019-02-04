#!/usr/bin/env python

#importy
#----------------------------------------------




class Figure():
    
    King = 'k'
    Queen = 'q'
    Rook = 'r'
    Bishop = 'b'
    Knight = 'n'
    Pawn = 'p'
    chessboard = []
    fig = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
    
    def __init__(self):
        self.chessboard = [self.fig]
        self.chessboard.append(['p'] * 8)
        for i in range(4):
            self.chessboard.append([''] * 8)
        self.chessboard.append(['P'] * 8)
        self.chessboard.append([i.upper() for i in self.fig])
        print self.chessboard
    
    def image(self):
        for i in self.chess
            
            
            
f = Figure()
f