class Person():
    '''Создание человека'''
    def __init__(self, name, age, height, weight):
        '''Инициализируем атрибуты человека'''
        self.name = name
        self.age = age
        self.hight = height
        self.weight = weight
    def description_person(self):
        '''Получение описания человека'''
        description = self.name + ' ему ' + str(self.age) + ' лет. Его рост ' + str(self.hight) + ' и вес ' + str(self.weight) + ' кг.'
        print('Нового человека зовут '+ description)
    def get_weight(self):
        """"Получение веса человека"""
        print('Вес нашего человека ' + str(self.weight))

    def update_weight(self, kg):
        """"Изменение веса человека"""
        self.weight = kg

man = Person('Alex', 30, 180, 80)
#man.description_person()
#man.get_weight()
man.update_weight(110)