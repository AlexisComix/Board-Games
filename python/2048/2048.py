import pygame
import random
import numpy as np

WIN_WIDTH = 500
WIN_HEIGHT = 500

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Helvetica Neue',70)

#Making the window
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
color = (187, 173, 160)
win.fill(color)
pygame.display.set_caption("2048")

#Setting colors of all the numbers
COLOR2 = (238, 228, 218)
COLOR4 = (238,225,201)
COLOR8 = (243,178,122)
COLOR16 = (246,150,100)
COLOR32 = (247,124,95)
COLOR64 = (247,95,59)
COLOR128 = (237,208,115)
COLOR256 = (237,204,98)
COLOR512 = (252, 197, 20)
COLOR1024 = (255, 195, 0)
COLOR2048 = (255, 230, 0)
N = 4

class Grid:

    ANIMATION_TIME = 5

    def __init__(self):
        #Basic Grid attributes
        self.grid = np.zeros((N, N), dtype=int)
        self.width = 150
        self.height = 150
        self.value = 2
        self.score = 0
        self.gap = 25

    def __str__(self):
        return str(self.grid)

    def new_number(self, k=1):
        """
        Creating new Number on the Grid.
        """
        freeposs = list(zip(*np.where(self.grid == 0)))   #Position of the empty spaces
        for pos in random.sample(freeposs, k):
            if random.random() < .1:
                self.grid[pos] = 4
            else:
                self.grid[pos] = 2

    @staticmethod
    def move_sumnumber(grid):
        """
        Adding the number on each move
        """
        grid_n = grid[grid != 0]
        grid_sum = []
        skip = False
        for i in range(len(grid_n)):
            if skip:
                skip = False
                continue
            if i < len(grid_n)-1 and grid_n[i] == grid_n[i+1]:
                new_n = grid_n[i] * 2
                skip = True
            else:
                new_n = grid_n[i]

            grid_sum.append(new_n)

        return np.array(grid_sum)

    def move_number(self, move):
        """
        All 4 possible moves performed
        """
        if move == 'l':
            for i in range(N):
                temp = self.grid[i, :]

                temp_n = Grid.move_sumnumber(temp)

                new_temp = np.zeros_like(temp)

                new_temp[:len(temp_n)] = temp_n

                self.grid[i, :] = new_temp
        elif move == 'u':
            for i in range(N):
                temp = self.grid[:, i]

                temp_n = Grid.move_sumnumber(temp)

                new_temp = np.zeros_like(temp)

                new_temp[:len(temp_n)] = temp_n

                self.grid[:, i] = new_temp
        elif move == 'r':

            for i in range(N):
                temp = self.grid[i, :]
                temp = temp[::-1]
                temp_n = Grid.move_sumnumber(temp)

                new_temp = np.zeros_like(temp)

                new_temp[:len(temp_n)] = temp_n

                new_temp = new_temp[::-1]
                self.grid[i, :] = new_temp

        elif move == 'd':

            for i in range(N):
                temp = self.grid[:, i]
                temp = temp[::-1]
                temp_n = Grid.move_sumnumber(temp)

                new_temp = np.zeros_like(temp)

                new_temp[:len(temp_n)] = temp_n
                new_temp = new_temp[::-1]
                self.grid[:, i] = new_temp

    def isfilled(self):
        """
        Game Over case
        """
        old_grid = self.grid.copy()
        
        for move in 'lrdu':
            self.move_number(move)
            if not all((old_grid == self.grid).flatten()):
                self.grid = old_grid
                return False
        return True    

    def CLI_play(self):
        """
        To play in Command Line
        """
        self.new_number(k=2)
        while True:

            print(self.grid)

            old_grid = self.grid.copy()

            player = input("Enter Move : ")

            if(player == 'q'):
                break
            elif(player == 'l'):
                self.move_number('l')
            elif(player == 'r'):
                self.move_number('r')
            elif(player == 'u'):
                self.move_number('u')
            elif(player == 'd'):
                self.move_number('d')

            if all((old_grid == self.grid).flatten()):
                continue
            self.new_number()

    def createRect(self):
        """
        Creating the rectangles of each member of Grid
        """
        x = 25
        y = 25
        rect = np.zeros((4,4),dtype=pygame.Rect)
        rectwidth = 100
        rectheight = 100
        rectgap = 20
        
        text = np.zeros((4,4),dtype=pygame.Surface)
        
        for i in range(4):
            x = 15
            for j in range(4):
                if(self.grid[i][j] != 0):
                    rect[i][j] = pygame.Rect((x, y, rectwidth, rectheight))
                    text[i][j] = myfont.render(str(self.grid[i][j]), True, (0,0,0))
                                          
                x = x + rectwidth+rectgap
            y = y + rectheight+rectgap
        return rect,text

    def draw(self):
        """
        Drawing the Grid
        """
        rect,text = self.createRect()
        win.fill(color)

        for i in range(4):
            for j in range(4):
                if(rect[i][j] != 0):
                    r = rect[i][j]
                    if(self.grid[i][j] == 2):
                        pygame.draw.rect(win, COLOR2, r)
                    elif(self.grid[i][j] == 4):
                        pygame.draw.rect(win, COLOR4, r)
                    elif(self.grid[i][j] == 8):
                        pygame.draw.rect(win, COLOR8, r)
                    elif(self.grid[i][j] == 16):
                        pygame.draw.rect(win, COLOR16, r)
                    elif(self.grid[i][j] == 32):
                        pygame.draw.rect(win, COLOR32, r)
                    elif(self.grid[i][j] == 64):
                        pygame.draw.rect(win, COLOR64, r)
                    elif(self.grid[i][j] == 128):
                        pygame.draw.rect(win, COLOR128, r)
                    elif(self.grid[i][j] == 256):
                        pygame.draw.rect(win, COLOR256, r)
                    elif(self.grid[i][j] == 512):
                        pygame.draw.rect(win, COLOR512, r)
                    elif(self.grid[i][j] == 1024):
                        pygame.draw.rect(win, COLOR1024, r)
                    elif(self.grid[i][j] == 2048):
                        pygame.draw.rect(win, COLOR2048, r)            
                    else:
                        pygame.draw.rect(win, COLOR2048, r)  
                    text_rect = text[i][j].get_rect(center=((r.left + r.width / 2, r.top + r.height / 2)))
                    win.blit(text[i][j], text_rect)
        self.drawscore()            
    def drawscore(self):
        """
        Drawing the score
        """
        sum = 0
        for i in range(N):
            for j in range(N):
                sum += self.grid[i][j]

        myfont = pygame.font.SysFont('Helvetica Neue',20)
        text = myfont.render("Score = " + str(sum), True, (0,0,0)) 
        win.blit(text,(400,20))
        self.score = sum

    def drawGameOver(self):
        """
        Drawing GameOver
        """
        myfont = pygame.font.SysFont('Helvetica Neue',80)
        sfont = pygame.font.SysFont('Helvetica Neue',40)
        text = myfont.render("Game Over",True,(255, 255, 255),(187, 173, 160))
        stext = sfont.render("Press E to play again or Q to quit",True,(255, 255, 255),(187, 173, 160))
        win.blit(text,((WIN_WIDTH//2)-160,(WIN_HEIGHT//2)-50))
        win.blit(stext,((WIN_WIDTH//2)-210,(WIN_HEIGHT//2)+10))

    def main(self):
        """
        Main Game
        """
        running = True
        self.new_number(2)

        redraw = True   
        GameOver = False       
        while running:

            old_grid = self.grid.copy()
            if redraw:
                self.draw()
                redraw = False
            if not GameOver:
                
                keys = pygame.key.get_pressed()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False   
                    elif keys[pygame.K_LEFT]:

                        self.move_number('l')
                        self.draw()
                    elif keys[pygame.K_RIGHT]:

                        self.move_number('r')
                        self.draw()
                    elif keys[pygame.K_UP]:

                        self.move_number('u')
                        self.draw()
                    elif keys[pygame.K_DOWN]:

                        self.move_number('d')  
                        self.draw() 
                    
                if self.isfilled():
                    print('Game Over')    
                    GameOver = True
                    self.drawGameOver()
                
                pygame.display.flip()
                
                if all((old_grid == self.grid).flatten()):
                    continue
                
                self.new_number()
            else:
                keys = pygame.key.get_pressed()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif keys[pygame.K_e]:
                        self.grid = np.zeros((N, N), dtype=int)   
                        self.new_number(2)
                        GameOver = False
                        redraw = True
                    elif keys[pygame.K_q]: 
                        running = False 

if __name__ == '__main__':
   game = Grid()
   game.main()

    