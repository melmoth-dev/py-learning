import time

class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.time = time.time()
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        print('{0} {1}'.format(self.time, time.time() ))

with ManagedFile('test.txt') as f:
    f.write('Проверка')
