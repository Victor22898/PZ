#Средствами языка Python сформировать текстовый файл (.txt), содержащий
 #последовательность из целых положительных и отрицательных чисел. Сформировать
 #новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
 #обработку элементов:
 #Исходные данные:
 #Количество элементов:
 #Индекс последнего минимального элемента:
 #Сумма элементов больших 10 во второй половине:



import random


sequence = [random.randint(-100, 100) for _ in range(20)]


with open('sequence.txt', 'w') as file:
    for number in sequence:
        file.write(f"{number}\n")


last_min_index = None
sum_greater_than_10_second_half = 0

for idx, number in enumerate(sequence):
    if number == min(sequence):
        last_min_index = id
    if idx >= len(sequence) // 2 and number > 10:
        sum_greater_than_10_second_half += number


with open('processed_sequence.txt', 'w') as file:
    file.write("Исходные данные:\n")
    file.write(" ".join(map(str, sequence)) + "\n")
    file.write(f"Количество элементов: {len(sequence)}\n")
    file.write(f"Индекс последнего минимального элемента: {last_min_index}\n")
    file.write(f"Сумма элементов больших 10 во второй половине: {sum_greater_than_10_second_half}\n")


print("\nСодержимое файла processed_sequence.txt:")
with open('processed_sequence.txt', 'r') as file:
    print(file.read())

print("Готово: processed_sequence.txt.")

