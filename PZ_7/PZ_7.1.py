def validate_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")


N = validate_input("Введите число N: ")
C = input("Введите символ C: ")


try:
    if N <= 0:
        print("Число N должно быть больше нуля.")
    else:
        result = C * N
        print("Результат:", result)
except TypeError:
    print("Некорректный ввод символа C.")
