#02.05.2020 22:22

def namesScores(name):
    '''Подсчёт алфавитного значения имени.'''
    res = 0
    for s in name[:]:
        res += ord(s.upper()) - 64
    return res

with open('./euler/names.txt', 'r') as f:
    names = [s.strip('"') for s in f.read().split(',')]                         # Получение списка имён из файла

names.sort()                                                                    # Сортировка имён

scores = [(i + 1) * namesScores(names[i]) for i in range(len(names))]           # Список алфавитных значений имён

print(sum(scores))
