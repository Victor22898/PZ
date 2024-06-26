# Единицы длины пронумерованы следующим образом: 1-дециметр, 2-километр, 3-метр, 4-миллиметр, 5-сантиметр.
# Дан номер единицы длины (целое число в диапазоне 1-5) и длина отрезка в этих единицах (вещественное число).
# Найти длину отрезка в метрах.

print('1 - дециметр')
print('2 - километр')
print('3 - метр')
print('4 - миллиметр')
print('5 - сантиметр')  # пишем значения

a = input('Выберите цифру: ')


while type(a) != int:
    try:
        a = int(a)
        if 6 <= a:
            print('Введите повторно')
            raise ValueError

    except ValueError:  # обработка ошибки
        print('1 - дециметр')
        print('2 - километр')
        print('3 - метр')
        print('4 - миллиметр')
        print('5 - сантиметр')
        a = input('Выберите цифру: ')

b = float(input('Введите длину: '))  # назначаем значения
if a == 1:
    c = b * 0.1
    print('Ответ в дециметрах: ', c)
elif a == 2:
    c = b * 1000
    print('Ответ в километрах: ', c)
elif a == 3:
    c = b
    print('Ответ в метрах: ', c)
elif a == 4:
    c = b * 0.001
    print('Ответ в миллиметрах: ', c)
elif a == 5:
    c = b * 0.01
    print('Ответ в сантиметрах: ', c)
else:
    print('Такой цифры нет!')
