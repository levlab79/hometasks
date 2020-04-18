# Задание 1.

# Создаем список с элементами различных типов данных.
strange_list = [
    'some string', 21, 31.2, True, complex(2, 4), list(), dict(),
    set(), frozenset(), tuple(), None, b'some text'
]
# Проверяем тип данных каждого элемента.
for element in strange_list:
    # Выводим тип данных.
    print(type(element))
