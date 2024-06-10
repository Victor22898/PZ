# Из предложенного текстового файла (text18-8.txt) вывести на экран его содержимое,
#количество символов, принадлежащих к группе букв. Сформировать новый файл, в
# который поместить текст в стихотворной форме предварительно удалив букву «с» из текста.



with open('text18-8.txt', 'r', encoding='utf-8') as file:
    content = file.read()


print("Содержимое файла:")
print(content)


letters_count = sum(1 for char in content if char.isalpha())


print(f"Количество букв: {letters_count}")


new_content = content.replace('с', '').replace('С', '')


with open('new_text18-8.txt', 'w', encoding='utf-8') as file:
    file.write(new_content)

print("Обработка завершена. Содержимое нового файла записано в new_text18-8.txt.")
