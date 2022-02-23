"""Ромбы, (c) Эл Свейгарт al@inventwithpython.com
Рисует ромбы различного размера.
Код размещен на https://nostarch.com/big-book-small-python-projects
Теги: крошечная, для начинающих, графика"""

def main():
    print('Diamonds, by Al Sweigart al@inventwithpython.com')
    
    # Отображает ромбы размера с 0 по 6:    
    for diamondSize in range(0, 6):
        displayOutlineDiamond(diamondSize)
        print()
        displayFilledDiamond(diamondSize)
        print()
        
def displayOutlineDiamond(size):
    # отображает верхнюю часть ромба
    for i in range(size):
        print(' ' * (size - i - 1), end ='') # прбелы слева
        print('/', end='') # левая сторона ромба
        print(' ' * (i * 2), end='') # внутреность ромба
        print('\\') # правая сторона ромба
        
    # отображает нижнюю половину ромба
    for i in range(size):
        print(' ' * i, end='')
        print('\\', end='') # левая сторона ромба
        print(' ' * ((size - i - 1) * 2), end='') # внутренность ромба
        print('/') # правая сторона ромба
        
def displayFilledDiamond(size):
    # отображает верхнюю часть ромба
    for i in range(size):
        print(' ' * (size - i - 1), end='') # пробелы слева
        print('/' * (i + 1), end='') # левая сторона ромба
        print('\\' * (i + 1)) # правая сторона ромба
        
    # отображает нижнюю половину ромб    а
    for i in range(size):
        print(' ' * i, end='') # пробелы слева
        print('\\' * (size - i), end='') # левая сторона ромба
        print('/' * (size - i)) # правая сторона ромба
        
# если программа не импортируется а запускается - производим запуск
if __name__ == '__main__':
    main()
    