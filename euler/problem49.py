#10.05.2020 14:11

import math

# Задаём значение, для которого будет вестись вычисление
number = 9999

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

numbers = [x for x in PrimeNumbers(9999).numbers if x >= 1000]                  # Получаем список простых чисел от 1000 до максимального числа

# Получаем список арифметических прогрессий, удовлетворяющих условиям
res = []
for x in numbers:
    l = [x,]
    for y in numbers[numbers.index(x) + 1:]:
        d = isPermutation(x, y)
        if d > 0:
            for z in numbers[numbers.index(y) + 1:]:
                if d == isPermutation(y, z):
                    l.extend([y, z])
    if len(l) == 3:
        res.append(l)

res = [str(x) for x in res[1]]

print(''.join(res))