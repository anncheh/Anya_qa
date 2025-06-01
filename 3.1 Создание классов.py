class Person():
    """Модель человека"""
    def __init__(self, name, age):
        """Инициализация атрибутов человека - имя, возраст"""
        self.name = name
        self.age = age
        print('Человек создан')

    def sing(self):
        """"Просим человека спеть"""
        print(self.name + ' поет')

    def dance(self):
        """Просим человека станцевать"""
        print(self.name + ' танцует')

man = Person("Алекс", 30)
#print(man.name)
woman = Person('Настя',28)

man.sing()
woman.dance()

class Animal():
    def __init__(self, type, name, age, bridd):
        self.type = type
        self.name = name
        self.age = age
        self.bridd = bridd
    def eat(self):
        print(self.type + " " + self.name + ' ест')
    def drink(self):
        print(self.type + ' ' + self.name + " пьет")
    def walk(self):
        print(self.type + ' ' + self.name + " гуляет")

cow = Animal("Корова", 'Мася', 10, 'татарская')
dog = Animal("Собака", 'Чика', 4, 'чихуа')
cow.eat()
dog.eat()
dog.drink()
dog.walk()