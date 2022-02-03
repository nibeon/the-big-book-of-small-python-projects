"""Шифр Цезаря - шифр сдвига, в котором шифрование 
и дешифровка букв производистя путем сложения и 
вычитания соответствующих чисел."""

try:
    import pyperclip # pyperclip копирует текст в буфер обмена
except ImportError:
    pass # если библиотека не подключена ничего не делаем

# все возможные символы для шифровки/дешифровки
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Caesar Cipher, by Al Sweigart al@inventwithpython.com')
print('The Caesar cipher encrypts letters by shifting them over by a')
print('key number. For example, a key of 2 means the letter A is')
print('encrypted into C, the letter B encrypted into D, and so on.')
print()

# спрашиваем пользователя, хочет он шифровать или дешифровать
while True: # повторяем вопрос пока юзер не ввведет e или d
    print('Do you want (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letter e or d.')
    
# просим пользователя ввести ключ шифрования
while True:
    maxKey = len(SYMBOLS) - 1
    print('Plese enter the key (0 to {}) to use.'.format(maxKey))
    response = input('> ').upper()
    if not response.isdecimal():
        continue
    
    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break
    
# просим пользователя ввести сообщение для шифрования/расшифровки
print('Enter the message to {}.'.format(mode))
message = input('> ')

# шифр цезаря работает только с символами в верхнем регистре
message = message.upper()

# для хранения зашифрованного/расшифрованного варианта сообщения
translated = ''

# зашифровываем/расшифровываем каждый символ сообщения
for symbol in message:
    if symbol in SYMBOLS:
        # получаем зашифрованное/расшифрованное значение для символа
        num = SYMBOLS.find(symbol) # получаем числовое значение символа
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
            
        # производим переход по кругу, если число больше длины SYMBOLS
        # или меньше 0
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)
        # добавляем соответствующий числу зашифрованный/расшифрованный символ
        # в переменную translated
        translated = translated + SYMBOLS[num]
    else:
        # просто добавляем символ без шифрования/расшифровки
        translated = translated + symbol
        
# выводим зашифрованную/расшифрованную строку на экран 
print(translated)

try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to clipboard.'.format(mode))
except:
    pass
