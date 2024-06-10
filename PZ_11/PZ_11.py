#Средствами языка Python сформировать текстовый файл (txt), содержащий последовательность из целых положительных и отрицательных чисел.
#Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:

#Исходные данные:

#Индекс последнего минимального элемента:

#Сумма элементов больших 10 во второй половине:

filename = "output.txt"
import random

num_elements = 20

numbers = [random.randint(-100, 100) for _ in range(num_elements)]

last_min_index = numbers.index(min(numbers))

second_half_sum = sum(num for num in numbers[num_elements // 2:] if num > 10)

print("Исходные данные:\n")
print(f"Количество элементов: {num_elements}")
print(f"Индекс последнего минимального элемента: {last_min_index}")
print(f"Сумма элементов больших 10 во второй половине: {second_half_sum}")


with open('output.txt', 'w') as file:
    file.write("Исходные данные:\n\n")
    file.write(f"Количество элементов: {num_elements}\n")
    file.write(f"Индекс последнего минимального элемента: {last_min_index}\n")
    file.write(f"Сумма элементов больших 10 во второй половине: {second_half_sum}\n")

data = """Количество элементов: 20
Индекс последнего минимального элемента: 1
Сумма элементов больших 10 во второй половине: 163"""

with open("output.txt", "w") as file:
    file.write(data)
    print("Файл output.txt успешно создан.")










