import os
import shutil

# Переход в каталог PZ11 и вывод списка всех файлов в этом каталоге (1)
os.chdir('C:\\Users\\victor\\Desktop\\pycharm\\pythonProject\\PZ_11')
files_in_pz11 = [f for f in os.listdir() if os.path.isfile(f)]
print("PZ11:", files_in_pz11)

# Переход в корень проекта и создание папок (2)
os.chdir('C:\\Users\\victor\\Desktop\\pycharm\\pythonProject')
os.makedirs('test/test1', exist_ok=True)

# Перемещение файлов
shutil.move('PZ_6/PZ_6.py', 'test/PZ_6.py')
shutil.move('PZ_6/PZ_6_1.py', 'test/PZ_6_1.py')
shutil.move('PZ_7/PZ_7.py', 'test/test1/test.txt')

# Вывод информации о размере файлов в папке test
os.chdir('test')
for file in os.listdir():
    if os.path.isfile(file):
        print(f"размер {file}: {os.path.getsize(file)}")

# Переход в папку с PZ11 и нахождение файла с самым коротким именем (3)
os.chdir('C:\\Users\\victor\\Desktop\\pycharm\\pythonProject\\PZ_11')
shortest_name = min(files_in_pz11, key=len)
print("короткий в PZ11:", os.path.basename(shortest_name))

# Переход в папку с отчетом и запуск файла (4)
os.chdir('C:\\Users\\victor\\Desktop\\pycharm\\pythonProject\\Reports')
for file in os.listdir():
    if file.endswith('PZ_11.pdf'):
        os.startfile(file)
        break

# Удаление файла test.txt (5)
os.remove('../test/test1/test.txt')
