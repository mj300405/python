import random

def computerGuess(upperBound):
    print(f'I will try to guess your number between 1 and {upperBound} \nPlease answear me with these:\nh for too high guess,\nl for too low guess,\nc for correct guess.\nNow let us start!')
    low=1
    high=upperBound
    feedback=''
    while True:
        guess=random.randint(low, high)
        feedback=input(f'Is {guess} your number?')
        if feedback=='l':
            low=guess+1
            guess=random.randint(low,high)
        elif feedback=='h':
            high=guess-1
            guess=random.randint(low,high)
        elif feedback=='c':
            break
        else:
            print('Unknown answear! Try once again!')
    print(f'Your number was{guess}')
    return

computerGuess(100)
