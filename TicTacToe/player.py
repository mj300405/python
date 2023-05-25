import math
from numpy import random

class Player:
    def __init__(self, letter):
        self.letter=letter
    
    def getMove(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def getMove(self, game):
        square=random.choice(game.availableMoves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def getMove(self, game):
        validSquare=False
        val=None
        while not validSquare:
            square=input(self.letter + '\'s turn. Input move (0-9): ')
            try:
                val=int(square)
                if val not in game.availableMoves():
                    raise ValueError
                validSquare=True
            except ValueError:
                print('Invalid input. Try again.')
        return val

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def getMove(self, game):
        if len(game.availableMoves())==9:
            square=random.choice(game.availableMoves())
        else:
            square=self.minmax(game, self.letter)['position']
        return square
    
    def minmax(self, state, player):
        maxPlayer=self.letter
        otherPlayer='O' if player=='X' else 'X'

        if state.currentWinner==otherPlayer:
            return {'position': None, 'score': 1*(state.numberOfEmpty()+1) if otherPlayer==maxPlayer else -1* (state.numberOfEmpty()+1)}
        elif not state.emptySquares():
            return {'position': None, 'score': 0}

        if player==maxPlayer:
            best={'position': None, 'score': -math.inf}
        else:
            best={'position': None, 'score': math.inf}

        for possibleMove in state.availableMoves():
            state.makeMove(possibleMove, player)
            simulateScore=self.minmax(state, otherPlayer)
        
            state.board[possibleMove]=' '
            state.currentWinner=None
            simulateScore['position']=possibleMove

            if player==maxPlayer:
                if simulateScore['score']>best['score']:
                    best=simulateScore
            else:
                if simulateScore['score']<best['score']:
                    best=simulateScore

        return best