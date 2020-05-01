#01.05.2020 15:38

value = 999                                                                     # Заданное значение

def isPalindrome(value):
    '''Проверка строки на палиндромность.'''
    return value == value[::-1]

def maxPalindromeProduct(value):
    '''Наибольшее произведение-палиндром.'''

    # Обоим мрожителям присваиваем заданное значение
    x = value
    y = value

    while True:
        if isPalindrome(str(x * y)):                                            # Если произведение даёт полиндром
            break                                                               # то поиск закончен

        if x > y:
            x -= 1
            y = value
        else:
            y -= 1

    return x * y

print(str(maxPalindromeProduct(value)))