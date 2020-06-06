#06.06.2020 23:50

power = 5                                                                       # Заданная степень

digitsPowers = [int(x) ** power for x in range(10)]                             # Список значений степеней всех цифр

def digitPowersSum(value):
    '''Получение суммы степеней цифр числа.'''
    powers = [digitsPowers[int(c)] for c in str(value)]
    return sum(powers)

l = [x for x in range(11, digitsPowers[9] * 10) if digitPowersSum(x) == x]      # Список всех чисел, которые могут быть записаны в виде суммы пятых степеней их цифр

print(sum(l))                                                                   # Вывести сумму всех полученных чисел
