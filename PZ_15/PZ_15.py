# Приложение ОПТОВАЯ БАЗА для автоматизированного контроля движения
# товаров на оптовой базе. Таблица Товары должна содержать следующие данные: Код
# товара, Наименование товара, Наименование магазина, Заявки магазина, Количество
# товара на складе, Единицы измерения, Оптовая цена.

import sqlite3

def update_product(product_code, product_name, customer, order_date, execution_period, order_cost):
    cursor.execute("""UPDATE orders SET product_name = ?, customer = ?, order_date = ?, execution_period = ?, order_cost = ? WHERE product_code = ?""",
                   (product_name, customer, order_date, execution_period, order_cost, product_code))
    print(f"Товар с кодом {product_code} обновлен.")
    conn.commit()

def add_product_quantity(product_code, quantity):
    cursor.execute("UPDATE orders SET quantity = quantity + ? WHERE product_code = ?", (quantity, product_code))
    print(f"Количество товара с кодом {product_code} увеличено.")
    conn.commit()

def update_product_prices(product_code, new_price):
    cursor.execute("UPDATE orders SET order_cost = ? WHERE product_code = ?", (new_price, product_code))
    print(f"Стоимость товара с кодом {product_code} обновлена.")
    conn.commit()

conn = sqlite3.connect('orders_database.db')

cursor = conn.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS orders (
    product_code INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    customer TEXT,
    order_date TEXT,
    execution_period INTEGER CHECK(execution_period BETWEEN 1 AND 10),
    order_cost REAL,
    quantity INTEGER DEFAULT 0
)
"""

cursor.execute(create_table_query)

for product_code in range(1, 11):
    cursor.execute(
        """
        INSERT OR IGNORE INTO orders (product_code, product_name, customer, order_date, execution_period, order_cost)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (product_code, f"Product {product_code}", f"Customer {product_code}", "2022-12-01", product_code, 100.0 * product_code)
    )

conn.commit()

if __name__ == "__main__":
    while True:
        print("1: Обновить цены\n2: Изменить количество\n3: Выход")
        choice = int(input("Выберите действие: "))
        if choice == 1:
            product_code = int(input("Введите код товара: "))
            new_price = float(input("Введите новую цену: "))
            update_product_prices(product_code, new_price)
        elif choice == 2:
            product_code = int(input("Введите код товара: "))
            quantity = int(input("Введите количество: "))
            add_product_quantity(product_code, quantity)
        elif choice == 3:
            break
        else:
            print("Недопустимый выбор")

cursor.execute("SELECT * FROM orders")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()


