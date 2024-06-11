#В матрице элементы последней строки заменить на 0


import random

def replace_last_row_with_zeros(matrix):
    last_row_index = len(matrix) - 1
    for i in range(len(matrix[last_row_index])):
        matrix[last_row_index][i] = 0

matrix = [[random.randint(1, 10) for _ in range(0, 3)] for _ in range(0, 3)]


print("Исходная матрица:")
for row in matrix:
    print(row)


replace_last_row_with_zeros(matrix)


print("\nМатрица с заменой последней строки на 0:")
for row in matrix:
    print(row)