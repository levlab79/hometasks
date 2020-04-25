from itertools import count, cycle


def gen_int_numbers(start_n, end_n):
    """Функция, генерирующая целые числа, начиная с указанного"""
    for number in count(start_n):
        if number > end_n:
            break
        else:
            yield number


def repeat_list_chars(end_n, list_n):
    """Функиця, повторяющая элементы списка"""
    count_n = 0
    for el in cycle(list_n):
        if count_n > end_n:
            break
        else:
            count_n += 1
            yield el


# Переменная начального числа для генерации.
start_with = 10
# Ограничение числа при генерации (чтобы не было бесконечного цикла).
end_count = 30
# Список для повторения.
some_list = [1, 2, 3, False, 'Da']

# Вызываем функции.
print(list(gen_int_numbers(start_with, end_count)))
print(list(repeat_list_chars(end_count, some_list)))
