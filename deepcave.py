"""Глубокая пещера, (c) Эл Свейгарт al@inventwithpython.com
Динамическое изображение глубокой пещеры, ведущей до самого центра Земли.
Код размещен на https://nostarch.com/big-book-small-python-projects
Теги: крошечная, для начинающих, прокрутка, графика"""

import random, sys, time

WIDTH = 70
PAUSE_AMOUNT = 0.05

print('Deep Cave, by Al Sweigart al@inventwithpython.com')
print('Press Ctrl-C to stop.')
time.sleep(2)

leftWidth = 20
gapWidth = 10

while True:
    # отображает фрагмент туннеля
    rightWidth = WIDTH - gapWidth - leftWidth
    print(('#' * leftWidth) + (' ' * gapWidth) + ('#' * rightWidth))
    
    # Проверяем, не нажато ли Ctrl+C, во время короткой паузы:
    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        sys.exit() # Если нажато сочетание клавиш Ctrl+C — завершаем программу.
        
    # подбираем ширину левой части
    diceRoll = random.randint(1, 6)
    if diceRoll == 1 and leftWidth > 1:
        leftWidth = leftWidth - 1
    elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
        leftWidth = leftWidth + 1
    else:
        pass
    
    # подбираем ширину зазора
    # diceRoll = random.randint(1, 6)
    #if diceRoll == 1 and gapWidth > 1:
    #    gapWidth = gapWidth - 1
    #elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
    #    gapWidth = gapWidth - 1
    #else:
    #    pass
    