#10.05.2020 12:50

import math
import itertools

# Задаём значение, для которого будет вестись вычисление
number = 999999999

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

def isNDigitNumber(value):
    '''Проверка является ли число - пан-цифровым.'''
    digits = '123456789'
    s = str(value)
    return set(s) == set(digits[:len(s)])                                       # Сравнение множества символов

primes = PrimeNumbers(math.sqrt(number))                                        # Получаем список простых чисел до корня максимального числа

# Получение списка всех n-значных пан-цифровых простых чисел
res = []
digits = range(1, 10)
for n in range(2, 10):
    for p in itertools.permutations(digits[:n]):                                # Перестановки цифр от 1 до n
        x = int(''.join(map(str, p)))                                           # Перевод картежа цифр в число
        if isNDigitNumber(x) and primes.isPrime(x):                             # Проверка является ли число - пан-цифровым и простым
            res.append(x)

print(max(res))