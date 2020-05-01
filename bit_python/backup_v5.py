import zipfile
import os
import time

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['C:\\develop\\source\\py', 'C:\\develop\\source\\test']
# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки.

# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'C:\\develop\\backup'

# 3. Файлы помещаются в zip-архив.
# 4. Именем для zip-архива служит текущая дата и время.
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

# 5. Создание нового архива
z = zipfile.ZipFile(target, 'w')

for s in source:                                                                # Список всех сохраняемыъ директорий
    for root, dirs, files in os.walk(s):                                        # Список всех файлов и папок в директории 
        for file in files:
            z.write(os.path.join(root, file))                                   # Создание относительных путей и запись файлов

# 6. Закрытие архива
z.close