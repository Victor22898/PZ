import random

def validate_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")


N = validate_input("Введите размер списка: ")

lst = []
for _ in range(N):
    lst.append(random.randint(1, 100))


count = 0
try:
    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            count += 1
except IndexError:
    print("Возникла ошибка индекса списка")

print("Сгенерированный список:", lst)
print("Количество участков с монотонно возрастающими элементами:", count)
