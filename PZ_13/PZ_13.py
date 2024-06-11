#В матрице элементы столбца N (N задать с клавиатуры) увеличить в два раза.
rows = int(input("Введите количество строк матрицы: "))
columns = int(input("Введите количество столбцов матрицы: "))

matrix = []
for i in range(rows):
    row = []
    for j in range(columns):

        element = int(input(f"Введите элемент [{i}][{j}]: "))
        row.append(element)
    matrix.append(row)

print("Исходная матрица:")
for row in matrix:
    print(row)

n = int(input("Введите номер столбца (N): "))

for i in range(rows):
    matrix[i][n-1] += 2

print("Измененная матрица:")
for row in matrix:
 print(row)





 rows = int(input("Введите количество строк матрицы: "))
columns = int(input("Введите количество столбцов матрицы: "))


matrix = []
for i in range(rows):
    row = []
    for j in range(columns):

        element = int(input(f"Введите элемент [{i}][{j}]: "))
        row.append(element)
    matrix.append(row)


print("Исходная матрица:")
for row in matrix:
    print(row)


n = int(input("Введите номер столбца (N): "))


for i in range(rows):
    matrix[i][n-1] += 2


print("Измененная матрица:")
for row in matrix:
    print(row)

    matrix[i][n] += 2

    matrix[i][n - 1] += 2

