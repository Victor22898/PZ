sales_string = 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16'

sales_list = sales_string.split()

averages_dict = {}

i = 0
while i < len(sales_list):
    product = sales_list[i]
    sales = list(map(int, sales_list[i+1:i+6]))
    average_sales = sum(sales) / len(sales)
    averages_dict[product] = average_sales
    i += 6

product_keys = averages_dict.keys()
average_sales_values = averages_dict.values()

result = "\n".join([f"Средняя продажа {product}: {average_sales} кг" for product, average_sales in zip(product_keys, average_sales_values)])
print(result)
