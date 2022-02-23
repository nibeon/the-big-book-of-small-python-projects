"""Обратный отсчет, (c) Эл Свейгарт al@inventwithpython.com
Отображает динамическое изображение таймера обратного отсчета с помощью
семисегментного индикатора. Для останова нажмите Ctrl+C. Больше информации —
в статье https://ru.wikipedia.org/wiki/Семисегментный_индикатор
Требует наличия в том же каталоге файла sevseg.py.
Код размещен на https://nostarch.com/big-book-small-python-projects
Теги: крошечная, графика"""

import sys, time
import sevseg # импорт програамы sevseg.py

secondsLeft = 30

try:
    while True:
        print('\n' * 60)
        
        hours = str(secondsLeft // 3600)
        minutes = str((secondsLeft % 3600) // 60)
        seconds= str(secondsLeft % 60)
        
        # получаем из модуля sevseg стоковые значения для цифр
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()
        
        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()
        
        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()
        
        # отображаем цифры
        print(hTopRow + ' ' + mTopRow + ' ' + sTopRow)
        print(hMiddleRow + ' * ' + mMiddleRow + ' * ' + sMiddleRow)
        print(hBottomRow + ' * ' + mBottomRow + ' * ' + sBottomRow)
        
        if secondsLeft == 0:
            print()
            print(' * * * * BOOM * * * *')
            print()
            print('Press Ctrl-C to quit.')
            
            time.sleep(1)
            secondsLeft -= 1
except KeyboardInterrupt:
    print('Countdown, by Al Sweigart al@inventwithpython.com')
    sys.exit() # Если нажато сочетание клавиш Ctrl+C — завершаем программу.
            