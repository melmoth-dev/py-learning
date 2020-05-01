#01.05.2020 16:48
import math

value = 20                                                                      # Заданное значение

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

def createPrimes(maxValue):
    '''Формирование списка всех простых чисел до заданного числа.'''
    primes = [2]
    while True:
        x = nextPrime(primes)
        if x > maxValue:
            break
        primes.append(x)

    return primes

primes = createPrimes(101)

def calcFactors(value):
    '''Разбиение на простые множители и их степени'''
    factors = {}
    x = value
    if x in primes:
        factors[x] = 1
    else:
        n = len(primes)
        i = 0
        while i < n:
            if x < primes[i]:
                break
            elif x % primes[i] == 0:
                x //= primes[i]
                factors.setdefault(primes[i], 0)
                factors[primes[i]] += 1
            else:
                i += 1

    return factors

factors = {x:0 for x in primes if x <= value}

for i in range(2, value + 1):
    for k, v in calcFactors(i).items():
        factors[k] = max(factors[k], v)

res = 1
for k, v in factors.items():
    res *= k ** v

print(res)