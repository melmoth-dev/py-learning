class Robot:
    '''Представляет робота с именем.'''
    # Переменная класса, содержащая количество роботов
    population = 0
    
    def __init__(self, name):
        '''Инициализация данных.'''
        self.name = name
        print('(Инициализация {0})'.format(self.name))
        
        # При создании этой личности, робот добавляется к переменной population
        Robot.population += 1
    
    def __del__(self):
        '''Уничтожение робота.'''
        print('{0} уничтожен'.format(self.name))
        
        Robot.population -= 1
        
        if Robot.population == 0:
            print('{0} был последним'.format(self.name))
        else:
            print('Популяция роботов уменьшилась до {0}'.format(Robot.population))
    
    def sayHi(self):
        '''Приветствие робота.'''
        print('Приветствую! Меня зовут {0}'.format(self.name))
    
    #@staticmethod
    def howMany():
        '''Выводит количество роботов.'''
        print('Популяция роботов: {0}'.format(Robot.population))
    
    howMany = staticmethod(howMany)
    
droid1 = Robot('R2-D2')
droid1.sayHi()
Robot.howMany()

droid2 = Robot('C-3PO')
droid2.sayHi()
Robot.howMany()

print("\nЗдесь роботы могут проделать какую-то работу.\n")

print("Роботы закончили свою работу. Давайте уничтожим их.")
del droid1
del droid2

Robot.howMany