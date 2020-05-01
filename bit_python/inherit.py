from abc import *

class SchoolMember(metaclass=ABCMeta):
    '''Представляет любого человека в школе.'''
    
    members = []
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Создан {0}: {1})'.format(self.__class__.__name__, self.name))
        SchoolMember.members.append(self)
        
    def __del__(self):
        print('(Удалён {0}: {1})'.format(self.__class__.__name__, self.name))
        SchoolMember.members.remove(self)
    
    @abstractmethod
    def tell(self):
        '''Вывести информацию о человеке'''
        print('Имя: "{0}" Возраст: "{1}"'.format(self.name, self.age), end = ' ')

class Teacher(SchoolMember):
    '''Представляет преподавателя.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        
    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата: "{0}"'.format(self.salary))

class Student(SchoolMember):
    '''Представляет студента.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
    
    def tell(self):
        SchoolMember.tell(self)
        print('Оценки: "{0:d}"'.format(self.marks))

m = SchoolMember('Иван Петров', 39)
t = Teacher('Мандик Виктор Петрович', 59, 50000)
s = Student('Илья Петров', 19, 75)

print('') # Печать пустой строки

#members = [t, s]

for member in SchoolMember.members:
    member.tell()
