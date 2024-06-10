


# Из предложенного текстового файла (text18-8.txt) вывести на экран его содержимое. количество символов, принадлежащих к группе букв.
# Сформировать новый файл, в который поместить текст в стихотворной форме предварительно удалив букву «с» из текста.
filename = "text18-8.txt"


content = "Пример текста для записи в файл."


with open('filename.txt', "w") as file:
    file.write(content)

print(f"Файл '{filename}' успешно создан и содержит текст.")


filename = "text18-8.txt"

with open(filename, "r") as file:
    content = file.read()


print("Содержимое файла:")
print(content)


letters_count = sum(1 for c in content if c.isalpha())
print("Количество символов, принадлежащих к группе букв:", letters_count)


modified_content = content.replace("с", "")
modified_content = modified_content.replace(".", ".\n")
modified_content = modified_content.replace(",", ",\n")


new_filename = "modified_text.txt"
with open(new_filename, "w") as new_file:
    new_file.write(modified_content)

print(f"\nТекст в стихотворной форме, без буквы 'с', записан в файл: {new_filename}")
