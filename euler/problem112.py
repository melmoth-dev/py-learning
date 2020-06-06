#07.06.2020 01:18

# Заданный процент пропорции прыгучих чисел
percent = 99

def isBouncy(value):
    '''Проверка является ли число положительным целым, ни убывающим, ни возрастающим,
    т.е. "прыгучим"'''
    s = str(value)
    increased = False
    decreased = False
    for (i, c) in enumerate(s):
        if i > 0:
            if not increased:
                increased = s[i - 1] < s[i]
            if not decreased:
                decreased = s[i - 1] > s[i]

        if increased and decreased: break

    return increased and decreased

n = 0

for x in range(1, 10 ** 10):
    if isBouncy(x):
        n += 1
        if n * 100 // x == percent:
            print(x)
            break