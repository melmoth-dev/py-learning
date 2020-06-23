#24.06.2020 02:01

# Задаём значение, для которого будет вестись вычисление
number = 100

def calc(k):
    if k > 1:
        l = calc(k - 1)
        res = [[(sum(l[0][:i + 1]) + sum(l[1][:i])) if i > 1 else 0 for i in range(10)],
               [1 if i > 0 else 0 for i in range(10)],
               [(sum(l[2][i:]) + sum(l[1][i + 1:])) for i in range(10)]]
    else:
        res = [[0 for i in range(10)],
               [1 if i > 0 else 0 for i in range(10)],
               [0 for i in range(10)]]

    return res

l = [calc(x) for x in range(1, number + 1)]
total = sum(sum(x[0]) + sum(x[1]) + sum(x[2]) for x in l)

print(total)