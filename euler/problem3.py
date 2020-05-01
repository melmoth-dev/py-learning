#01.05.2020 15:00
import math

primes = [2, 3]

def nextPrime(curr):
    '''Получение следующего простого числа.'''
    res = curr
    while True:
        res += 2                                                                # Проверяем только нечётные числа
        for x in primes:
            if x > math.sqrt(res):                                              # Если простой делитель больше корня
                return res                                                      # то имеем следующее простое число
            if res % x == 0:                                                    # Если делится без остатка на простое число
                break                                                           # то ищем дальше

def maxPrimeFactor(value):
    '''Поиск самого большого делителя числа, являющегося простым числом'''

    # Составляем список всех простых чисел до корня из заданного числа
    i = len(primes) - 1
    while True:
        x = nextPrime(primes[i])
        if x > math.sqrt(value):
            break
        primes.append(x)
        i += 1

    # Ищем наибольшее простое число, являющееся делителем заданного
    i = len(primes) - 1
    while True:
        if i < 0 or value % primes[i] == 0:
            break
        i -= 1

    if i < 0:                                                                   # Если среди простых чисел делителя не нашли
        return value                                                            # то само число является простым
    else:
        return primes[i]

print(maxPrimeFactor(600851475143))