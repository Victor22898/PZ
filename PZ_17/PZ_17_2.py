# Единицы длины пронумерованы следующим образом: 1-дециметр, 2-километр, 3-метр, 4-миллиметр, 5-сантиметр.
# Дан номер единицы длины (целое число в диапазоне 1-5) и длина отрезка в этих единицах (вещественное число).
# Найти длину отрезка в метрах.

import tkinter as tk


def convert_length():
    unit = int(entry_unit.get())
    length = float(entry_length.get())

    if unit == 1:
        result = length / 10
    elif unit == 2:
        result = length * 1000
    elif unit == 3:
        result = length
    elif unit == 4:
        result = length / 1000
    elif unit == 5:
        result = length / 100
    else:
        result = -1

    if result != -1:
        label_result.config(text=f"Длина отрезка в метрах: {result}")
    else:
        label_result.config(text="Неверный номер единицы длины")


root = tk.Tk()
root.title("Конвертер длины")

label_unit = tk.Label(root, text="Номер единицы длины (1-5):")
label_unit.pack()
entry_unit = tk.Entry(root)
entry_unit.pack()

label_length = tk.Label(root, text="Длина отрезка:")
label_length.pack()
entry_length = tk.Entry(root)
entry_length.pack()

convert_button = tk.Button(root, text="Преобразовать", command=convert_length)
convert_button.pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
