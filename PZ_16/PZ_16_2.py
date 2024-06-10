#Создание базового класса "Животное" и его наследование для создания классов
#"Собака" и "Кошка". В классе "Животное" будут общие методы, такие как "дышать"
#(и "питаться", а классы-наследники будут иметь свои уникальные методы и свойства, такие как "гавкать" и "мурлыкать"




class Animal:
    def __init__(self, name):
        self.name = name

    def breathe(self):
        return f'{self.name} дышит'

    def eat(self):
        return f'{self.name} питается'


class Dog(Animal):
    def bark(self):
        return f'{self.name} гавкает'


class Cat(Animal):
    def purr(self):
        return f'{self.name} мурлыкает'

dog = Dog('Шарик')
print(dog.breathe())
print(dog.bark())

cat = Cat('Мурзик')
print(cat.eat())
print(cat.purr())
