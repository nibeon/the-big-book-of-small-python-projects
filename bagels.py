import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print('''Bagels, a deductive logic game.
    When I say:   That means:
    Pico          One digit is correct but in the wrong position.
    Fermi          One digit is correct and in the right position.
    Bagels        No digit is no correct.
    For example, if the secret number was 248 and your guess was 843, the
     clues would be Fermi Pico.'''.format(NUM_DIGITS))
    
    while True:
        secretNum = getSecretNum() # должен угадать игрок
        print('I have throuh up a number.')
        print('You have {} goesses to get it.'.format(MAX_GUESSES))
        
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}'.format(numGuesses))
                guess = input('> ')

            
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1
            
            if guess == secretNum:
                break # правильно, выходим из цикла
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNum))
                
        # спрашиваем игрока, хочет ли он сыграть еще раз
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswisth('y'):
            break
    print('Thanks for playing!')
    
def getSecretNum():
    """Возращает строку из NUM_DIGITS уникальных случайных цифр. """
    numbers = list('0123456789') # создает список цифр от 0 до 9.
    random.shuffle(numbers) # перетасовываем их случайным образом.
    
    # берем первые NUM_DIGITS цифр списка для нашего секретного числа
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    """Возвращает строку с подсказками pico, fermi и bagels
    для получаемой на входе пары из догадки и секретного числа."""
    if guess == secretNum:
        return 'You got it!'
    
    clues = []
    
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # правильная цифра на правильном месте
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # правильная цифра на неправильном месте
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels' # правильных цифр нет вообще
    else:
        # сортируем подсказки в алфавитном порядке, чтобы 
        # их исходный порядок ничего не выдавал.
        clues.sort()
        # склеиваем список подсказок в одно строковое значение.
        return ' '.join(clues)
    
# если программа не импортируется, а запускается, производим запуск:
if __name__ == '__main__':
    main()
    