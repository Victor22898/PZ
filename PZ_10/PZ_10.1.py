Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> magnit = {'молоко', 'соль', 'сахар'}
... pyaterochka = {'мясо', 'молоко', 'сыр'}
... perekrestok = {'молоко', 'творог', 'сыр', 'сахар'}
... 
... # не сыр
... stores_without_cheese = []
... 
... if 'сыр' not in magnit:
...     stores_without_cheese.append('Магнит')
... if 'сыр' not in pyaterochka:
...     stores_without_cheese.append('Пятерочка')
... if 'сыр' not in perekrestok:
...     stores_without_cheese.append('Перекресток')
... 
... print("В магазинах нельзя приобрести сыр:", stores_without_cheese)
... 
... # молоко и сахар
... milk_and_sugar_stores = []
... 
... if 'молоко' in magnit and 'сахар' in magnit:
...     milk_and_sugar_stores.append('Магнит')
... if 'молоко' in pyaterochka and 'сахар' in pyaterochka:
...     milk_and_sugar_stores.append('Пятерочка')
... if 'молоко' in perekrestok and 'сахар' in perekrestok:
...     milk_and_sugar_stores.append('Перекресток')
... 
... print("В магазинах можно приобрести молоко и сахар:", milk_and_sugar_stores)
... 
... # Соль
... stores_with_salt = []
... 
... if 'соль' in magnit:
...     stores_with_salt.append('Магнит')
... if 'соль' in pyaterochka:
...     stores_with_salt.append('Пятерочка')
... if 'соль' in perekrestok:
...     stores_with_salt.append('Перекресток')

print("В магазинах можно приобрести соль:", stores_with_salt)
