import random

def game():
    user=input("'r' for rock, 'p' for paper, 's' for scissors\nYour choice:")
    computer=random.choice(['r','p','s'])
    print(f'computer choice: {computer}\n')
    if user==computer:
        return 'It is a tie!'
    elif isWin(user, computer):
        return 'You won!'
    
    return 'You lost!'
    

def isWin(player1, player2):
    if (player1=='r' and player2=='s') or (player1=='p' and player2=='r') or (player1=='s' and player2=='p'):
        return True


print(game())