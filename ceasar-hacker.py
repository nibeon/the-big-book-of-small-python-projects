"""Взлом шифра Цезаря прямым перебором всевозможных ключей."""

print('Ceasar Cipher Hacker, by Al Sweigart')

# просим пользователя ввести сообщение для взлома
print('Enter the encrypted Ceasar ciper message to hack.')
message = input('> ')

# все возможные символы для дешифровки
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)):
    translated = ''
    
    # расшифровываем каждый символ
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol) # получаем числовое значение символа
            num = num - key # расшифровываем числовое значение
            
            # выполняем переход по кругу, если число меньше 0
            if num < 0:
                num = num + len(SYMBOLS)
            # добавляем соответствующий числу расшифрованный символ в translated
            translated = translated + SYMBOLS[num]
        else:
            # просто добавляем символ без расшифровки
            translated = translated + symbol
            
    # выводим проверяемый ключ вместе с расшифрованным на его основе текстом
    print('Key #{}: {}'.format(key, translated))
            