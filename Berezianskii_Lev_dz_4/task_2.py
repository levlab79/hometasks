import random

# Формируем первоначальный список чисел длинной 15 с помощью генератора.
list_numbers = [random.randint(0, 30) for _ in range(15)]
print(f'Исходный список: {list_numbers}')

# Формируем новый список согласно условиям.
new_list = [list_numbers[index] for index in range(1, len(list_numbers))
            if list_numbers[index] > list_numbers[index - 1]]
print(f'Новый список: {new_list}')
