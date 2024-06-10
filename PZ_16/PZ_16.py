#Создай класс "Человек" с атрибутами "имя", "возраст" и "пол".
# Напиши метод который выводит информацию о человеке в формате Имя: имя, Возраст: возраст, Пол: пол".


class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        return f'Имя: {self.name}, Возраст: {self.age}, Пол: {self.gender}'


person = Human("Alex", 30, "Мужской")

print(person.display_info())
