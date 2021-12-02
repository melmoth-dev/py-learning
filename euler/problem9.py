#02.12.2021 23:33

a = b = 1
c = 1000 - (a + b)
while a + b + c:
    if a * a + b * b - c * c == 0:
        break
    c -= 1
    if c == 0:
        b +=1
        a = 1
        c = 1000 - (a + b)
    else:
        a += 1

print('abc={}'.format(a * b * c))
