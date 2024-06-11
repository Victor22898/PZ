#В исходном текстовом файле(Dostoevsky.txt) найти все произведения писателя.
#Посчитать количество полученных элементов.
import requests


def find_dostoevsky_books():
    query = "Достоевский произведения"  # Запрос для поиска
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        total_items = data["totalItems"]
        items = data["items"]


        for item in items:
            volume_info = item["volumeInfo"]
            title = volume_info["title"]
            print(f"Произведение: {title}")

        print(f"Общее количество произведений: {total_items}")
    else:
        print("Ошибка при выполнении запроса.")


find_dostoevsky_books()

with open("Dostoevsky.txt", "w") as file:

    file.write("Произведения писателя Федора Достоевского:\n")
    file.write("- Преступление и наказание\n")
    file.write("- Братья Карамазовы\n")
    file.write("- Идиот\n")
    file.write("- Бесы\n")
    file.write("- Записки из мертвого дома\n")

print("Файл Dostoevsky.txt успешно создан.")