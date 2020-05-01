#01.05.2020 13:25
# Задаём максимальное значение, до которого будем искать числа
max_lvl = 4000000

def nextFib(prev, curr):
    '''Расчёт следующего числа ряда Фибоначчи.'''
    return prev + curr

# Создаём список чисел ряда Фибоначчи
l = [1, 2]
i = 1
while True:
    x = nextFib(l[i - 1], l[i])
    if x > max_lvl:
        break
    l.append(x)
    i += 1

# Инициализируем начальное значение суммы
res = 0

# Считаем значение суммы
for x in l:
    if x % 2 == 0:
        res += x
    
# Вывод значения суммы на экран
print(res)