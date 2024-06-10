def remove(text):
    words = text.split() 
    new_sentence = ' '.join(words)  
    return new_sentence


text = input('Введите предложение с избыточными пробелами: ')

result = remove(text) 
print('Результат:', result)
