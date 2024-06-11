# В последовательности на n целых элементов найти количество пар, для которых произведение элементов делится на 3
# (элементы пары в последовательности являются соседними)

n = int(input("Введите число: "))

from functools import reduce

def count_pairs(sequence):
    count = reduce(lambda acc, pair: acc + 1 if pair[0] % 3 == 0 or pair[1] % 3 == 0 else acc, zip(sequence[:-1], sequence[1:]), 0)
    return count

sequence = [i for i in range(n)]
print(sequence)

count = count_pairs(sequence)
print("Количество пар, для которых произведение элементов делится на 3:", count)
