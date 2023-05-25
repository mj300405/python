import time
from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board=[' ' for _ in range(9)]
        self.currentWinner = None
    
    def printBoard(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| '+ ' | '.join(row)+ ' |')

    @staticmethod
    def printBoardNumbers():
        numberBoard=[[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in numberBoard:
            print('| '+ ' | '.join(row)+ ' |')

    
    def availableMoves(self):
        moves=[]
        for (i, spot) in enumerate(self.board):
            if spot==' ':
                moves.append(i)
        return moves

    def emptySquares(self):
        return ' ' in self.board

    def numberOfEmpty(self):
        return self.board.count(' ')
    
    def makeMove(self, square, letter):
        if self.board[square]==' ':
            self.board[square]=letter
            if self.winner(square, letter):
                self.currentWinner=letter
            return True
        return False

    def winner(self, square, letter):
        rowInd=square//3
        row=self.board[rowInd*3:(rowInd+1)*3]
        if all([spot==letter for spot in row]):
            return True
        
        colInd=square%3
        column=[self.board[colInd+i*3] for i in range(3)]
        if all([spot==letter for spot in column]):
            return True
    
        if square%2==0:
            diag1=[self.board[i] for i in [0,4,8]]
            diag2=[self.board[i] for i in [2,4,6]]
            if all([spot==letter for spot in diag1]): 
                return True
            if all([spot==letter for spot in diag2]): 
                return True

        return False

def play(game, xp, op, printGame=True):
    if printGame:
        game.printBoardNumbers()
    
    letter='X'

    while game.emptySquares():
        if letter=='O':
            square=op.getMove(game)
        else:
            square=xp.getMove(game)
        
        if game.makeMove(square, letter):
            if printGame:
                print(letter + f' makes a move to square {square}')
                game.printBoard()
                print('')
            if game.currentWinner:
                if printGame:
                    print(letter + ' wins!')
                return letter 
            letter='O' if letter=='X' else 'X'
        
        time.sleep(0.5)

    if printGame:
        print('It is a tie')



if __name__=='__main__':
    xPlayer=HumanPlayer('X')
    oPlayer=GeniusComputerPlayer('O')
    t=TicTacToe()
    play(t, xPlayer, oPlayer, printGame=True)