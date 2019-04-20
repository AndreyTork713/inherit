class SchoolMember(object):
    '''Представляет любого человека в школе'''

    # Инициализация класса
    def __init__(self,name,age): # У экземпляра будет имя и возраст
        self.name = name
        self.age = age
        print('Создан SchoolMember: {0}'.format(self.name))
    #************************************************

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




