#10.05.2020 14:28

def digitSum(value):
    '''Получение суммы чифр числа.'''
    return sum([int(x) for x in str(value)])

res = 0
for x in range(1, 100):
    for y in range(1, 100):
        res = max(res, digitSum(x ** y))

print(res)