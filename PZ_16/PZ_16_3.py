#Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
#сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
#Использовать модуль pickle для сериализации и десериализации объектов Python в
#бинарном формате.


import pickle
def save_def(filename, instance):
    with open(filename, 'wb') as f:
        pickle.dump(instance, f)
def load_def(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)


class Counter:
    def __init__(self, counter_num):
        self.counter_num = counter_num
file1 = Counter('file1')
file2 = Counter('file2')
file3 = Counter('file3')

save_def('counters.data', [file1, file2, file3])

loaded_counters = load_def('counters.data')

for counter in loaded_counters:
    print(counter.counter_num)
















