#01.05.2020 23:38

import math

value = 2000000                                                                 # Заданное значение

def nextPrime(primes):
    '''Получение следующего простого числа.'''
    res = primes[-1]
    while True:
        res += 2                                                                # Проверяем следующее нечётное число
        for x in primes:
            if x > math.sqrt(res):                                              # Если простой делитель больше корня
                return res                                                      # то имеем следующее простое число
            if res % x == 0:                                                    # Если делится без остатка на простое число
                break                                                           # то ищем дальше

def createPrimes(value):
    '''Формирование списка всех простых чисел до заданного числа.'''
    primes = [2, 3]
    x = nextPrime(primes)
    while x < value:
        primes.append(x)
        x = nextPrime(primes)

    return primes

res = 0
for x in createPrimes(value):
    res += x

print(res)