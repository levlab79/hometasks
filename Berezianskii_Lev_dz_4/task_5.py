from functools import reduce


# Формируем первоначальный список четных чисел с помощью генератора.
list_numbers = [number for number in range(100, 1001) if not number % 2]
print(f'Исходный список: {list_numbers}')

list_sum = reduce(lambda x, y: x * y, list_numbers)
print(f'Произведение всех элементов списка: {list_sum}')
