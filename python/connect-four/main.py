from sys import exit
import time
from tkinter import EventType
import pygame
import numpy # numpy arrays are indexed like [vertical][horizontal]

class UnknownPieceError(Exception):
    """
    Raised when the program does not recognise a piece in
    the pieces array
    """
    pass


class ConnectFourGame:
    """
    Connect Four game class
    """
    def __init__(self):
        """
        Initialise variables
        """
        # Colours
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.YELLOW = (255, 255, 0)
        self.BLUE = (0, 0, 255)
        self.BLACK = (0, 0, 0)

        # Window dimensions
        self.WIDTH = 500
        self.HEIGHT = 500
        self.TOP_MARGIN = 100   # Blank space at the top for UI

        # Piece/Board dimensions
        self.PIECES_WIDTH = 7
        self.PIECES_HEIGHT = 6
        self.board_height = self.HEIGHT - self.TOP_MARGIN
        self.piece_diameter = 50
        self.piece_radius = self.piece_diameter / 2

        # Current player
        self.current_player = 1 # default to red
        self.winner = 0

        # Find the horizontal gap between the pieces holes
        self.horizontal_gap_width = (
                                        self.WIDTH
                                      - (
                                            self.PIECES_WIDTH 
                                          * self.piece_diameter
                                        )
                                    ) / (self.PIECES_WIDTH + 1) 
        
        # Find the vertical gap between the pieces holes
        self.vertical_gap_width = (
                                      self.board_height
                                    - (
                                          self.PIECES_HEIGHT 
                                        * self.piece_diameter
                                      )
                                  ) / (self.PIECES_HEIGHT + 1)

        # Get a numpy zeros array for the board
        self.board = numpy.zeros(
                                 (self.PIECES_HEIGHT, self.PIECES_WIDTH),
                                 dtype=int
        )
        # 0 = white, 1 = red, 2 = yellow

        # Initialise Pygame
        pygame.init()

        # Initialise font
        pygame.font.init()
        self.FONT = pygame.font.SysFont("Comic Sans MS", 40)

        # Initialise pygame clock
        self.CLOCK = pygame.time.Clock()

        # Initialise window instance
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        """---Main Loop Begin---"""
        running = True
        while running:
            self.WIN.fill(self.WHITE)
            self.draw_board()
            self.draw_pieces()
            
            # Win checks
            self.win_check_horizontal()
            self.win_check_vertical()
            self.win_check_diagonal()
            self.display_winner()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Exiting...")
                    pygame.quit()
                    exit()  # sys
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    buttons = pygame.mouse.get_pressed()
                    for button in buttons:
                        if button == 1:
                            (mouse_x, mouse_y) = pygame.mouse.get_pos()
                            column = self.get_column(mouse_x)
                            self.place_piece(column, self.current_player)
                            if self.winner != 0:
                                time.sleep(1)
                                pygame.quit()
                                exit()  # sys

            pygame.display.flip()
            self.CLOCK.tick(30)

    def draw_board(self):
        """
        Draw a blue rect representing the board
        """
        board_rect = pygame.rect.Rect(
            0,
            self.TOP_MARGIN,
            self.WIDTH,
            self.board_height
        )
        pygame.draw.rect(self.WIN, self.BLUE, board_rect)

    def draw_pieces(self):
        """
        Draw the pieces to the screen over the board rect
        """
        # Cursed maths magic that I forgot to keep the notes for
        for (y, x), piece in numpy.ndenumerate(self.board):
            piece_x = (
                         (x * self.piece_diameter)
                       + (self.horizontal_gap_width * (x + 1))
            )
            piece_y = (
                         (y * self.piece_diameter)
                       + (self.vertical_gap_width * (y + 1))
                       + self.TOP_MARGIN
            )

            # Get center coords of the circle
            piece_centerx = piece_x + self.piece_radius
            piece_centery = piece_y + self.piece_radius

            if piece == 0:  # Blank / White
                pygame.draw.circle(
                    self.WIN,
                    self.WHITE,
                    (piece_centerx, piece_centery),
                    radius=self.piece_radius,
                )
            elif piece == 1:    # Red
                pygame.draw.circle(
                    self.WIN,
                    self.RED,
                    (piece_centerx, piece_centery),
                    radius=self.piece_radius,
                )
            elif piece == 2:    # Yellow
                pygame.draw.circle(
                    self.WIN,
                    self.YELLOW,
                    (piece_centerx, piece_centery),
                    radius=self.piece_radius,
                )
            else:
                raise UnknownPieceError("Unknown piece")
    
    def get_column(self, mouse_x):
        """
        Returns the index of the column that the mouse is in
        """
        colwidth = self.WIDTH / self.PIECES_WIDTH
        index = 0
        for i in range(self.PIECES_WIDTH):
            col = i * colwidth
            if (mouse_x > col) and (mouse_x < (col + colwidth)):
                index = i
        return index

    def rindex(self, lst, value):
        """
        Gets the reverse index for a value in a list.
        i.e. the last index where an item appears in a list
        """
        l = [i for i in lst]    # Make list copy
        l.reverse()             # Reverse the list
        i = l.index(value)      # Find the reverse index
        return len(l) - i - 1

    def place_piece(self, columnindex: int, piece: int):
        col = list(numpy.take(self.board, columnindex, axis=1))
        full = 0 not in col
        if not full:
            free_index = self.rindex(col, 0)
            col[free_index] = piece
            for i, row in enumerate(range(self.PIECES_HEIGHT)):
                self.board[row][columnindex] = col[i]
            self.change_player()
            

    def change_player(self):
        """
        changes the active player depending on who went last
        """
        if self.current_player == 1:
            self.current_player = 2
        elif self.current_player == 2:
            self.current_player = 1
        else:
            print("Unknown player")

    def win_check_horizontal(self):
        """
        Checks all horizontal lines for wins
        """
        for i in range(self.PIECES_HEIGHT):
            row = list(numpy.take(self.board, i, axis=0))   # get row
            rowstr = ""                         # convert row to str
            for item in row:                    # by adding each item
                rowstr += str(item)             # to a blank str

            if "1111" in rowstr:                # check for red win
                self.winner = 1
            elif "2222" in rowstr:              # check for yellow win
                self.winner = 2

    def win_check_vertical(self):
        """
        Checks all vertical lines for wins
        """
        for i in range(self.PIECES_WIDTH):
            col = list(numpy.take(self.board, i, axis=1))   # get col
            colstr = ""                         # convert col to str
            for item in col:                    # by adding each item
                colstr += str(item)             # to a blank str

            if "1111" in colstr:                # check for red win
                self.winner = 1
            elif "2222" in colstr:              # check for yellow win
                self.winner = 2

    def win_check_diagonal(self):
        """
        Checks all diagonal lines y = x for wins

        Getting all diagonals from 
        https://stackoverflow.com/questions/6313308/
        get-all-the-diagonals-in-a-matrix-list-of-lists-in-python
        """
        x, y = self.PIECES_WIDTH, self.PIECES_HEIGHT

        # create a default array of specified dimensions
        a = self.board
        
        # stack overflow magic
        diags = [a[::-1,:].diagonal(i) for i in range(-a.shape[0]+1,a.shape[1])]
        diags.extend(a.diagonal(i) for i in range(a.shape[1]-1,-a.shape[0],-1))
        diaglist = [list(n) for n in diags] 
        
        # iterate over all diagonals
        for diagonal in diaglist:
            diagstr = ""                        # convert diag to str
            for i in diagonal:
                diagstr += str(i)
            if "1111" in diagstr:               # check for red win
                self.winner = 1
            elif "2222" in diagstr:             # check for yellow win
                self.winner = 2

    def display_winner(self):
        text = ""
        if self.winner == 1:
            text = "Red wins! Click to exit..."
        elif self.winner == 2:
            text = "Yellow wins! Click to exit..."
        else:
            pass
        text_surface = self.FONT.render(text, True, self.BLACK)
        self.WIN.blit(text_surface, (0, 0))


ConnectFourGame()