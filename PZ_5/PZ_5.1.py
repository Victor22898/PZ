 #Составить программу в которой функцию построит изображение в котором в первой строке 1 звёзжочка во второй 2 в третьей 3... в строке с номером m - m звёздочек
def print_triangle():
 while True:
    try:
        num = int(input("Введите число: "))
        break
    except ValueError:
        print("Ошибка: Введите целое число!")

 for i in range(1, num+1):
    print('*' * i)

print_triangle()


