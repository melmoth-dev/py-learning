#01.05.2020 16:59

value = 20                                                                      # Заданное значение

def quadSum(values):
    '''Сумма квадратов чисел последовательности.'''
    res = 0
    for x in values:
        res += x ** 2
    return res

def sumQuad(values):
    '''Квадрат суммы чисел последовательности.'''
    res = 0
    for x in values:
        res += x
    return res ** 2

values = range(1, value + 1)
res = sumQuad(values) - quadSum(values)
print(str(res))