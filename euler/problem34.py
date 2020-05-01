#02.05.2020 00:14
def factorial(value):
    '''Вычисление факториала от числа.'''
    if value == 0:
        res = 0
    else:
        res = 1
        for i in range(1, value + 1):
            res *= i
    return res

def digFactorials():
    '''Сосотавление словаря цифр со значениями факториалов от них.'''
    return {str(x):factorial(x) for x in range(10)}

digFactorials = digFactorials()

def digFactorialSum(value):
    res = 0
    for s in str(value):
        res += digFactorials[s]
    return res

res = 0
for x in range(10, 10000000):
    if x == digFactorialSum(x):
        res += x

print(res)