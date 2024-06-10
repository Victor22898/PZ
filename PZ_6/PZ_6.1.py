
import random

lst = [random.randint(-100, 100) for _ in range(10)]

print("Исходный список:")
print(lst)

new_list = [num for i, num in reversed(list(enumerate(list))) if num % 2 == 0]

print("Новый список с четными числами (в порядке убывания их индексов):")
print(new_lst)

K = len(new_lst)
print("Количество четных чисел: ", K)

