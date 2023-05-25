import random
from words import words

def validWord(words):
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice(words)
    return word.upper()

def hangman():
    lives=6
    word=validWord(words)
    wordSet=set(word)
    alphabet=set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    usedLetters=set()
    while len(wordSet)>0 and lives>0:
        print('You have used these characters: ', ' '.join(usedLetters))

        userLetter=input('Guess a letter: ').upper()
        wordList=[letter if letter in usedLetters else '-' for letter in word]
        print('Curent word: ', ' '.join(wordList))

        if userLetter in alphabet - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordSet:
                wordSet.remove(userLetter)
            else:
                lives-=1
                print(f'This letter is not in the word! You have {lives} more lives!')
        elif userLetter in usedLetters:
            print('You have already guessed this letters')

        else:
            print('Invalid character!')
    if lives == 0:
        print(f'You died! THe word was: {word}')
    else:
        print(f'You guessed the word {word}, correctly! Congratulation!')
    


hangman()