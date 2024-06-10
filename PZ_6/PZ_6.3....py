try:
    N = int(input("Введите длину списка: "))
    if N <= 0:
        raise ValueError("Длина списка должна быть положительным числом")
except ValueError as e:
    print("Ошибка:", e)
else:
    numbers = []
    for i in range(N):
        try:
            num = float(input("Введите число для элемента {}: ".format(i+1)))
            numbers.append(num)
        except ValueError:
            print("Ошибка ввода! Пожалуйста, введите число.")

    print("Исходный список:", numbers)
  
   
    def calculate_average(lst, i):
        total = lst[i]
        count = 1
        if i > 0:
            total += lst[i-1]
            count += 1
        if i < len(lst)-1:
            total += lst[i+1]
            count += 1
        return total / count
  
S
    for i in range(len(numbers)):
        numbers[i] = calculate_average(numbers, i)
  
    print("Измененный список:", numbers)
