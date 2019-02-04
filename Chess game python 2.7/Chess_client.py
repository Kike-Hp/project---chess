#!/usr/bin/env python

#importy
#----------------------------------------------
import Tkinter as tk
from chess import start as St
from chess import chessboard
from chess.chessboard_gui import display
# #----------------------------------------------
# Start = St.Start()
# Start.start()


game = chessboard.Board()
display(game)
