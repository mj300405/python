import random

def game(upperBound):
    randomNumber=random.randint(1, upperBound)
    guess=int(input(f'Guess a number between 1 and {upperBound}\nWhat is your guess?   '))
    while True:
        if guess>randomNumber:
            print(f'Number is smaller than {guess}  ')
        elif guess<randomNumber:
            print(f'Number is bigger than {guess}   ')
        else:
            print(f'Congratulation! It was {guess}  ')
            break
        guess=int(input('Give it another try! What is your next guess?'))
        
        
game(100)