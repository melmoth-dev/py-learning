#10.05.2020 11:46

import math

# Задаём значение, для которого будет вестись вычисление
number = 50000000

class PrimeNumbers:
    def __init__(self, maxValue):
        self.numbers = []

        while True:
            x = self.nextPrime()
            if x <= maxValue:
                self.numbers.append(x)
            else:
                break

    def isPrime(self, value):
        '''Проверка является ли число простым.'''
        for x in self.numbers:
            if x > math.sqrt(value):                                            # Если проверяемый простой делитель больше корня заданного числа
                return True                                                     # то заданное число - простое
            elif value % x == 0:                                                # Если заданное число делится без остатка на простое число
                return False                                                    # то оно уже не простое
        return True

    def nextPrime(self):
        '''Получение следующего простого числа.'''

        if len(self.numbers) == 0:                                              # Если не найдено ни одного простого числа
            n = 2                                                               # то первое простое число: 2
        elif self.numbers[-1] == 2:                                             # Если последнее найденное простое число "2"
            n = 3                                                               # то следующее простое число: 3
        else:                                                                   # Для всех остальных случаев
            n = self.numbers[-1] + 2                                            # Берём следующее за последним простым числом нечётное число
            while not self.isPrime(n):                                          # Проверяем является ли простым оно или какое-либо последующее нечётное число
                n += 2                                                          # Проверяем только нечётные числа

        return n

def isPermutation(value1, value2):
    '''Проверка является ли числа перестановками друг друга.'''
    if set(str(value1)) == set(str(value2)):                                    # Сравнение множества символов
        return value2 - value1
    else:
        return -1

primes = PrimeNumbers(math.sqrt(number)).numbers                                # Получаем список простых чисел до корня максимального числа

p2 = primes[:]
p3 = [p for p in primes if p < number ** (1/3)]
p4 = [p for p in primes if p < number ** (1/4)]

ic = 0
ia = 0
ib = 0

res = []
while True:
    a = primes[ia]
    b = primes[ib]
    c = primes[ic]

    if a ** 2 + b ** 3 + c ** 4 < number:
        res.append([a, b, c])

        ia = ia + 1 if ia < len(p2) - 1 else 0

        if ia == 0:
            ib = ib + 1 if ib < len(p3) - 1 else 0

            if ib == 0:
                ic = ic + 1 if ic < len(p4) - 1 else 0

                if ic == 0:
                    break

    else:
        if ia > 0:
            ia = 0
            ib = ib + 1 if ib < len(p3) - 1 else 0

            if ib == 0:
                ic = ic + 1 if ic < len(p4) - 1 else 0

                if ic == 0:
                    break
        else:
            if ib > 0:
                ib = 0
                ic = ic + 1 if ic < len(p4) - 1 else 0

                if ic == 0:
                    break

            else:
                break

print(len(res))

