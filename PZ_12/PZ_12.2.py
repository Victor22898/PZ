# Составить генератор (yield), который преобразует все буквенные символы в заглавные

def uppercase_generator(string):
    for char in string:
        if char.isalpha():
            yield char.upper()
        else:
            yield char


text = "Пример строки для преобразования"
result = ''.join(uppercase_generator(text))
print(result)
