#04.05.2020 01:06
import math

# Задаём по условию значение, для которого будет вестись вычисление
number = 600851475143

primes = [2, 3]

def isPrime(value):
    '''Проверка простоты числа.'''
    for x in primes:
        if x > math.sqrt(value):                                                # Если проверяемый простой делитель больше корня заданного числа
            return True                                                         # то заданное число - простое
        elif value % x == 0:                                                    # Если заданное число делится без остатка на простое число
            return False                                                        # то оно уже не простое
    return True

def nextPrime(primes):
    '''Получение следующего простого числа.'''
    res = primes[-1]
    while True:
        res += 2                                                                # Проверяем только нечётные числа
        if isPrime(res):
            return res                                                          # то ищем дальше

def calcPrimeFactors(value):
    '''Получение всех простых делителей числа.'''

    # Составляем список всех простых чисел до корня заданного числа
    while True:
        x = nextPrime(primes)
        if x > math.sqrt(value):
            break
        primes.append(x)

    # Ищем все простые числа из полученного списка, являющиеся делителем заданного
    factors = [x for x in primes if value % x == 0]

    # Ищем последний простой делитель, который оказался больше корня заданного числа
    n = value
    for x in factors:
        while n % x == 0:
            n //= x

    if n > 1:                                                                   # Если такой делитель нашёлся
        factors.append(n)                                                       # Добавляем его к списку

    return(factors)

primeFactors = calcPrimeFactors(number)                                         # Список всех простых делителей числа

print(max(primeFactors))