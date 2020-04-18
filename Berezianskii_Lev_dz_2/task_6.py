# Задание 6.
# Создадим главный список данных "Товары".
products_list = list()

# # Переменная, являющаяся номером товара.
# number = 1
# # Входим в основной цикл.
# while True:
#     new_name = input(f'#{number} Введите название товара (чтобы закончить, оставьте поле пустым): ')
#     # Проверяем не является ли переменная пустой строкой.
#     if new_name:
#         new_price = int(input(f'#{number} Укажите цену: '))
#         new_count = int(input(f'#{number} Укажите количество: '))
#         new_unit = input(f'#{number} Укажите единицу измерения: ')
#         new_dict = {
#             "название": new_name,
#             "цена": new_price,
#             "количество": new_count,
#             "eд": new_unit
#         }
#         print()
#         new_tuple = (number, new_dict)
#         # Добавляем сформированный кортеж в список.
#         products_list.append(new_tuple)
#         # Увеличиваем номер товара.
#         number += 1
#     else:
#         print()
#         # Выходим из цикла.
#         break

# Готовая структура данных.
products_list = [
    (1, {'название': 'Смартфон', 'цена': 47000, 'количество': 25, 'eд': 'шт'}),
    (2, {'название': 'Зарядка', 'цена': 1200, 'количество': 47, 'eд': 'шт'}),
    (3, {'название': 'Стекло', 'цена': 1200, 'количество': 57, 'eд': 'шт'}),
    (4, {'название': 'Чехол', 'цена': 21, 'количество': 1550, 'eд': 'шт'}),
    (5, {'название': 'Карта памяти', 'цена': 3500, 'количество': 10, 'eд': 'шт'}),
    (6, {'название': 'Динозавр', 'цена': 990000, 'количество': 1, 'eд': 'шт'})
]

print('Сформированная структура данных "Товары":')
# Выводим сформированную структуру и сразу заполняем новые списки.
product_analytics = {
    "название": [],
    "цена": [],
    "количество": [],
    "eд": []
}
# Входим в цикл.
for product in products_list:
    # Перебираем ключи и значения.
    for key, value in product[1].items():
        # Добавляем значения в списки, если они там еще не присутствуют.
        if key == 'название' and not value in product_analytics[key]:
            product_analytics[key].append(value)
        elif key == 'цена' and not value in product_analytics[key]:
            product_analytics[key].append(value)
        elif key == 'количество' and not value in product_analytics[key]:
            product_analytics[key].append(value)
        elif key == 'eд' and not value in product_analytics[key]:
            product_analytics[key].append(value)
    # Выводим информацию.
    print(product)

print()
print('Аналитика товаров:')
# Выводим словарь аналитики о товарах.
for key, value in product_analytics.items():
    print(f' {key}: {value}')
