#01.05.2020 17:07

import math

value = 10001                                                                   # Заданное значение

def nextPrime(primes):
    '''Получение следующего простого числа.'''
    res = primes[-1]
    while True:
        res += 1                                                                # Проверяем следующее число
        for x in primes:
            if x > math.sqrt(res):                                              # Если простой делитель больше корня
                return res                                                      # то имеем следующее простое число
            if res % x == 0:                                                    # Если делится без остатка на простое число
                break                                                           # то ищем дальше

def createPrimes(count):
    '''Формирование списка всех простых чисел до заданного числа.'''
    primes = [2]
    while len(primes) < count:
        x = nextPrime(primes)
        primes.append(x)

    return primes

primes = createPrimes(value)

print(primes[-1])