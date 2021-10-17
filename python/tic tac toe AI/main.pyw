# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 18:35:34 2020

@author: Nabeel
"""
# writing comments on everyline is difficult so 
# read doc strings...
# importing modules for use...
import sys, random
from PyQt5.QtWidgets import QApplication, QMainWindow
from Layout import Ui_MainWindow

class MyTicTacToe(QMainWindow):
    """Main class for the application."""
    def __init__(self):
        """Initializes the game."""
        super().__init__()  #initializing super class which is QMainWindow
        self.ui = Ui_MainWindow()#Making an instance of the layout Ui_MainWindow
        self.ui.setupUi(self)#this sets up the ui
        self.show()#shows all the widgets
        self.ui.start.setEnabled(False)#this disables the restart button
        #this connects the button with restartGame method
        self.ui.start.clicked.connect(self.restartGame)
        # the bellow connects all check boxes to markX method...
        self.ui.tl.clicked.connect(self.markX)
        self.ui.tm.clicked.connect(self.markX)
        self.ui.tr.clicked.connect(self.markX)
        self.ui.ml.clicked.connect(self.markX)
        self.ui.mm.clicked.connect(self.markX)
        self.ui.mr.clicked.connect(self.markX)
        self.ui.bl.clicked.connect(self.markX)
        self.ui.bm.clicked.connect(self.markX)
        self.ui.br.clicked.connect(self.markX)
        
        #this dictionary maps all the block with the corresponding checkboxes
        self.board = {self.ui.b1:self.ui.tl,
                      self.ui.b2:self.ui.tm,
                      self.ui.b3:self.ui.tr,
                      self.ui.b4:self.ui.ml,
                      self.ui.b5:self.ui.mm,
                      self.ui.b6:self.ui.mr,
                      self.ui.b7:self.ui.bl,
                      self.ui.b8:self.ui.bm,
                      self.ui.b9:self.ui.br}
        # counting the win count
        self.Xcount = 0
        self.Ocount = 0
        # check if the game is running
        self.run = True
        
    def markX(self):
        """Marks an X depending on the checked box."""
        if len(self.availableMoves()) != 0 and self.run:
            if self.ui.tl.isChecked():
                self.ui.tl.setEnabled(False)
                self.ui.b1.setText("X")
            if self.ui.tm.isChecked():
                self.ui.tm.setEnabled(False)
                self.ui.b2.setText("X")
            if self.ui.tr.isChecked():
                self.ui.tr.setEnabled(False)
                self.ui.b3.setText("X")
            if self.ui.ml.isChecked():
                self.ui.ml.setEnabled(False)
                self.ui.b4.setText("X")
            if self.ui.mm.isChecked():
                self.ui.mm.setEnabled(False)
                self.ui.b5.setText("X")
            if self.ui.mr.isChecked():
                self.ui.mr.setEnabled(False)
                self.ui.b6.setText("X")
            if self.ui.bl.isChecked():
                self.ui.bl.setEnabled(False)
                self.ui.b7.setText("X")
            if self.ui.bm.isChecked():
                self.ui.bm.setEnabled(False)
                self.ui.b8.setText("X")
            if self.ui.br.isChecked():
                self.ui.br.setEnabled(False)
                self.ui.b9.setText("X")
            if self.checkEnd() == "X":
                self.disableAll()
                self.ui.start.setEnabled(True)
                self.run = False
                self.Xcount += 1
                self.ui.result.setText("X won!")
                self.ui.score.setText(f"X:{self.Xcount},O:{self.Ocount}")
            else:
                self.botMove()
                if self.checkEnd() == "O":
                    self.disableAll()
                    self.ui.start.setEnabled(True)
                    self.run = False
                    self.Ocount += 1
                    self.ui.result.setText("O won!")
                    self.ui.score.setText(f"X:{self.Xcount},O:{self.Ocount}")
        else:
            self.ui.result.setText("Tied!")
            self.ui.start.setEnabled(True)
            self.run = False
            return None
    
    def checkEnd(self):
        """Returns if X or O wins."""
        #horizontal check
        if self.ui.b1.text() == "X" and self.ui.b2.text() == "X" \
            and self.ui.b3.text() == "X":
            return "X"
        if self.ui.b4.text() == "X" and self.ui.b5.text() == "X" \
            and self.ui.b6.text() == "X":
            return "X"
        if self.ui.b7.text() == "X" and self.ui.b8.text() == "X" \
            and self.ui.b9.text() == "X":
            return "X"
        #diagonal check
        if self.ui.b1.text() == "X" and self.ui.b5.text() == "X" \
            and self.ui.b9.text() == "X":
            return "X"
        if self.ui.b3.text() == "X" and self.ui.b5.text() == "X" \
            and self.ui.b7.text() == "X":
            return "X"
        #vertical check
        if self.ui.b1.text() == "X" and self.ui.b4.text() == "X" \
            and self.ui.b7.text() == "X":
            return "X"
        if self.ui.b2.text() == "X" and self.ui.b5.text() == "X" \
            and self.ui.b8.text() == "X":
            return "X"
        if self.ui.b3.text() == "X" and self.ui.b6.text() == "X" \
            and self.ui.b9.text() == "X":
            return "X"
        # check for o
        #horizontal check
        if self.ui.b1.text() == "O" and self.ui.b2.text() == "O" \
            and self.ui.b3.text() == "O":
            return "O"
        if self.ui.b4.text() == "O" and self.ui.b5.text() == "O" \
            and self.ui.b6.text() == "O":
            return "O"
        if self.ui.b7.text() == "O" and self.ui.b8.text() == "O" \
            and self.ui.b9.text() == "O":
            return "O"
        #diagonal check
        if self.ui.b1.text() == "O" and self.ui.b5.text() == "O" \
            and self.ui.b9.text() == "O":
            return "O"
        if self.ui.b3.text() == "O" and self.ui.b5.text() == "O" \
            and self.ui.b7.text() == "O":
            return "O"
        #vertical check
        if self.ui.b1.text() == "O" and self.ui.b4.text() == "O" \
        and self.ui.b7.text() == "O":
            return "O"
        if self.ui.b2.text() == "O" and self.ui.b5.text() == "O" \
            and self.ui.b8.text() == "O":
            return "O"
        if self.ui.b3.text() == "O" and self.ui.b6.text() == "O" \
            and self.ui.b9.text() == "O":
            return "O"
        
        
    def botMove(self):
        """Makes a move for O intelligently depending on the board.
        Moves to the mid if empty, otherwise the corners if any of them
        is empty else moves into the sides."""
        
        moves = self.availableMoves()
        if self.ui.b5 in moves and self.run:
            self.ui.b5.setText("O")
            self.board[self.ui.b5].setEnabled(False)
            return None
        else:
            Xwin = self.winningMove("X")
            Owin = self.winningMove("O")
        if Owin != None and self.run:
            if Owin[-1].text() != "X":
                Owin[-1].setText("O")
                self.board[Owin[0]].setEnabled(False)
                return None
            else:
                pass
        else:
            pass
        if Xwin != None and self.run:
            if Xwin[0].text() != "X":
                Xwin[-1].setText("O")
                self.board[Xwin[-1]].setEnabled(False)
                return None
            else:
                pass
        else:
            pass
        if len(moves) != 0 and self.run:
            corner_moves = []
            corners = [self.ui.b1, self.ui.b3, self.ui.b7, self.ui.b9]
            for i in corners:
                if i in moves:
                    corner_moves.append(i)
            sides_moves = []
            sides = [self.ui.b2, self.ui.b4, self.ui.b6, self.ui.b8]
            for i in sides:
                if i in moves:
                    sides_moves.append(i)
            if len(corner_moves) != 0:
                x = random.choice(corner_moves)
                x.setText("O")
                self.board[x].setEnabled(False)
            elif len(sides_moves) != 0:
                x = random.choice(sides_moves)
                x.setText("O")
                self.board[x].setEnabled(False)
            else:
                x = random.choice(moves)
                x.setText("O")
                self.board[x].setEnabled(False)
        else:
            self.ui.result.setText("Tied!")
            self.ui.start.setEnabled(True)
            self.run = False
            
    def winningMove(self, player):
        """Checks if the player X or O can win with a move."""
        #right wale moves
        if self.ui.b1.text() == player and self.ui.b2.text() == player:
            if self.ui.b3.text() == "_":
                return [self.ui.b3]
        if self.ui.b4.text() == player and self.ui.b5.text() == player:
            if self.ui.b6.text() == "_":
                return [self.ui.b6]
        if self.ui.b7.text() == player and self.ui.b8.text() == player:
            if self.ui.b9.text() == "_":
                return [self.ui.b9]
        #bottom wale moves
        if self.ui.b1.text() == player and self.ui.b4.text() == player:
            if self.ui.b7.text() == "_":
                return [self.ui.b7]
        if self.ui.b2.text() == player and self.ui.b5.text() == player:
            if self.ui.b8.text() == "_":
                return [self.ui.b8]
        if self.ui.b3.text() == player and self.ui.b6.text() == player:
            if self.ui.b9.text() == "_":
                return [self.ui.b9]
        #mid-vertical wale moves
        if self.ui.b1.text() == player and self.ui.b3.text() == player:
            if self.ui.b2.text() == "_":
                return [self.ui.b2]
        if self.ui.b4.text() == player and self.ui.b6.text() == player:
            if self.ui.b5.text() == "_":
                return [self.ui.b5]
        if self.ui.b7.text() == player and self.ui.b9.text() == player:
            if self.ui.b8.text() == "_":
                return [self.ui.b8]
        #mid-horizontal wale moves
        if self.ui.b1.text() == player and self.ui.b7.text() == player:
            if self.ui.b4.text() == "_":
                return [self.ui.b4]
        if self.ui.b2.text() == player and self.ui.b8.text() == player:
            if self.ui.b5.text() == "_":
                return [self.ui.b5]
        if self.ui.b3.text() == player and self.ui.b9.text() == player:
            if self.ui.b6.text() == "_":
                return [self.ui.b6]
        #left wale moves
        if self.ui.b2.text() == player and self.ui.b3.text() == player:
            if self.ui.b1.text() == "_":
                return [self.ui.b1]
        if self.ui.b5.text() == player and self.ui.b6.text() == player:
            if self.ui.b4.text() == "_":
                return [self.ui.b4]
        if self.ui.b8.text() == player and self.ui.b9.text() == player:
            if self.ui.b7.text() == "_":
                return [self.ui.b7]
        #top wale moves
        if self.ui.b4.text() == player and self.ui.b7.text() == player:
            if self.ui.b1.text() == "_":
                return [self.ui.b1]
        if self.ui.b5.text() == player and self.ui.b8.text() == player:
            if self.ui.b2.text() == "_":
                return [self.ui.b2]
        if self.ui.b6.text() == player and self.ui.b9.text() == player:
            if self.ui.b3.text() == "_":
                return [self.ui.b3]
        #diagonal bottom move
        if self.ui.b1.text() == player and self.ui.b5.text() == player:
            if self.ui.b9.text() == "_":
                return [self.ui.b9]
        if self.ui.b3.text() == player and self.ui.b5.text() == player:
            if self.ui.b7.text() == "_":
                return [self.ui.b7]
        #diagonal mid move
        if self.ui.b1.text() == player and self.ui.b9.text() == player:
            if self.ui.b5.text() == "_":
                return [self.ui.b5]
        if self.ui.b3.text() == player and self.ui.b7.text() == player:
            if self.ui.b5.text() == "_":
                return [self.ui.b5]
        #diagonal top move
        if self.ui.b5.text() == player and self.ui.b9.text() == player:
            if self.ui.b1.text() == "_":
                return [self.ui.b1]
        if self.ui.b5.text() == player and self.ui.b7.text() == player:
            if self.ui.b3.text() == "_":
                return [self.ui.b3]
            
    def availableMoves(self):
        """Returns a list of all available moves."""
        moves = []
        if not (self.ui.b1.text() == "X" or self.ui.b1.text() == "O"):
            moves.append(self.ui.b1)
        if not (self.ui.b2.text() == "X" or self.ui.b2.text() == "O"):
            moves.append(self.ui.b2)
        if not (self.ui.b3.text() == "X" or self.ui.b3.text() == "O"):
            moves.append(self.ui.b3)
        if not (self.ui.b4.text() == "X" or self.ui.b4.text() == "O"):
            moves.append(self.ui.b4)
        if not (self.ui.b5.text() == "X" or self.ui.b5.text() == "O"):
            moves.append(self.ui.b5)
        if not (self.ui.b6.text() == "X" or self.ui.b6.text() == "O"):
            moves.append(self.ui.b6)
        if not (self.ui.b7.text() == "X" or self.ui.b7.text() == "O"):
            moves.append(self.ui.b7)
        if not (self.ui.b8.text() == "X" or self.ui.b8.text() == "O"):
            moves.append(self.ui.b8)
        if not (self.ui.b9.text() == "X" or self.ui.b9.text() == "O"):
            moves.append(self.ui.b9)
        return moves
    
    def disableAll(self):
        """Disables all the checkboxes."""
        self.ui.tl.setEnabled(False)
        self.ui.tm.setEnabled(False)
        self.ui.tr.setEnabled(False)
        self.ui.ml.setEnabled(False)
        self.ui.mm.setEnabled(False)
        self.ui.mr.setEnabled(False)
        self.ui.bl.setEnabled(False)
        self.ui.bm.setEnabled(False)
        self.ui.br.setEnabled(False)
        
    def enableAll(self):
        """Enables all the checkboxes."""
        self.ui.tl.setEnabled(True)
        self.ui.tm.setEnabled(True)
        self.ui.tr.setEnabled(True)
        self.ui.ml.setEnabled(True)
        self.ui.mm.setEnabled(True)
        self.ui.mr.setEnabled(True)
        self.ui.bl.setEnabled(True)
        self.ui.bm.setEnabled(True)
        self.ui.br.setEnabled(True)
        
    def restartGame(self):
        """Starts the game when the start button is pressed."""
        self.run = True
        self.ui.start.setEnabled(False)
        #above statemen, after restarting, again disables the button
        #below loop iterates over all the keys and values and changes their state
        for i,j in self.board.items():
            i.setText("_")
            j.setChecked(False)
        self.enableAll()    #enables all the checkboxes
        self.ui.result.setText("")  #resets the result label
        
    
if __name__ == "__main__":# this is a tradition of python programmers
    app = QApplication(sys.argv)# makes an app instance
    w = MyTicTacToe()   # a window instance of MyTicTacToe
    w.show()            # displays all the widgets
    sys.exit(app.exec_())   #ensures that the program data is erased after ending
