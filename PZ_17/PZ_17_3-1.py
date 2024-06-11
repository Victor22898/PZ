#Задание 3.
#Задание предполагает, что у студента есть проект с практическими работами (№№ 2-13),
#оформленный согласно требованиям. Все задания выполняются c использованием модуля
#OS:
#перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге. Имена
#вложенных подкаталогов выводить не нужно.
# перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку
#test1. В папку test переместить два файла из ПЗ6, а в папку test1 - один файл из ПЗ7.
#Файл из ПЗ7 переименовать в test.txt. Вывести в консоль информацию о размере
#файлов в папке test.
# перейти в папку с PZ11, найти там файл с самым коротким именем, имя вывести в
#консоль. Использовать функцию basename () (os.path.basename()).
# перейти в любую папку где есть отчет в формате .pdf и «запустите» файл в
 #привязанной к нему программе. Использовать функцию os.startfile().
# удалить файл test.txt.


import os
import shutil


os.chdir('C:\\Users\\victor\\Desktop\\Pzz\\pythonProject')
files_in_pz11 = [f for f in os.listdir() if os.path.isfile(f)]
print("PZ11:", files_in_pz11)


os.makedirs('test/test1', exist_ok=True)


try:
    shutil.move('PZ_6/PZ_6.py', 'test/PZ_6.py')
except FileNotFoundError:
    print('Файл "PZ_6/PZ_6.py" не найден.')

try:
    shutil.move('PZ_6/PZ_6_2.py', 'test/PZ_6_2.py')
except FileNotFoundError:
    print('Файл "PZ_6/PZ_6_2.py" не найден.')

try:
    shutil.move('PZ_7/PZ_7.py', 'test/test1/test.txt')
except FileNotFoundError:
    print('Файл "PZ_7/PZ_7.py" не найден.')


os.chdir('test')
for file in os.listdir():
    if os.path.isfile(file):
        print(f"размер {file}: {os.path.getsize(file)}")


os.chdir('C:\\Users\\victor\\Desktop\\Pzz\\pythonProject\\PZ_11')
shortest_name = min(files_in_pz11, key=len)
print("короткий в PZ11:", shortest_name)


report_path = 'C:\\Users\\victor\\Desktop\\Pzz\\pythonProject\\Report'
os.chdir(report_path)
found = False
for file in os.listdir():
    if file.endswith('PZ_7.pdf'):
        os.startfile(file)
        found = True
        break

if not found:
    print(f'Файл "PZ_7.pdf" не найден в папке "{report_path}".')


try:
    os.remove('C:\\Users\\victor\\Desktop\\Pzz\\pythonProject\\test\\test1\\test.txt')
except FileNotFoundError:
    print('Файл "test.txt" не найден в папке "test/test1".')
