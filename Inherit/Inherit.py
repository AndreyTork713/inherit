from abc import *

class SchoolMember(metaclass = ABCMeta):
    '''Представляет любого человека в школе'''

    # Инициализация класса
    def __init__(self,name,age): # У экземпляра будет имя и возраст
        self.name = name
        self.age = age
        print('Создан SchoolMember: {0}'.format(self.name))
    #************************************************
    @abstractmethod
    def tell(self):
        '''Вывести информацию'''
        print('Имя: "{0}", Возраст: "{1}"'.format(self.name,self.age,end = " "))
    #************************************************

#   КЛАССЫ НАСЛЕДНИКИ

class Teacher(SchoolMember):      # класс Teacher наследник класса SchoolMember  
    '''Представляет преподавателя'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('Создан Teacher: {0}'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата: "{0:d}"'.format(self.salary))

class Student(SchoolMember):      # класс Student наследник класса SchoolMember  
    '''Представляет студента'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('Создан Student: {0}'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Оценки: "{0:d}"'.format(self.marks))


      #СОЗДАНИЕ ОБЪЕКТОВ И ВЫПОЛНЕНИЕ ТЕЛА ПРОГРАММЫ

t = Teacher('Mrs. Shrividya',40,30000)
s = Student('Swaroop',25,75)

print()

members = [t, s]
for member in members:
    member.tell() # Работает как для преподавателя так и для студента





