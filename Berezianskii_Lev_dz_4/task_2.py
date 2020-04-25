import random


def gen_list(n):
    """Формирует первоначальный список чисел длинной n с помощью генератора."""
    return [random.randint(0, 30) for _ in range(n)]


if __name__ == '__main__':
    # Длина списка.
    count_number = 15
    list_numbers = gen_list(count_number)
    print(f'Исходный список: {list_numbers}')

    # Формируем новый список согласно условиям.
    new_list = [list_numbers[index] for index in range(1, len(list_numbers))
                if list_numbers[index] > list_numbers[index - 1]]
    print(f'Новый список: {new_list}')
