# Даны два целых числа А и В (А<В). Найти сумму квадратов всех целых чисел от А до В включительно.

A = int(input("Введите число A:"))
B = int(input("Введите число B:"))
if A >= B:
    print("Значение A должно быть меньше B")
else:

    t = 0
    if A >= B:
        print("Значение A должно быть меньше B")
    else:
        for i in range(A - 1, B + 1):
            t = t + i ** 2
    print(t)











