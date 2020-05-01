#02.05.2020 00:30

# Задаём по условию значение, для которого будет вестись вычисление
number = 100

def factorial(value):
    '''Вычисление факториала от числа.'''
    if value == 1:
        res = 1
    elif value == 0:
        res = 0
    else:
        res = value * factorial(value - 1)
    return res

res = 0
for s in str(factorial(number)):
    res += int(s)

print(res)