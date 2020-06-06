#06.06.2020 23:50

power = 5                                                                       # Заданная степень

def digitPowersSum(value, power):
    '''Получение суммы степений цифр числа.'''
    digitsPowers = [int(c) ** power for c in str(value)]
    return sum(digitsPowers)

l = [x for x in range(11, 1000000) if digitPowersSum(x, power) == x]            # Список всех чисел, которые могут быть записаны в виде суммы пятых степеней их цифр

print(sum(l))                                                                   # Вывести сумму всех полученных чисел
