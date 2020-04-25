import task_2


def unique_find(el, list_el):
    count_el = 0
    # Проверяем, есть ли вообще элемент в списке.
    if el in list_el:
        for el_value in list_el:
            if el_value == el:
                count_el += 1
                if count_el > 1:
                    return False
        # Если цикл не прервался, значит в списке только 1 такой элемент.
        return True
    else:
        return False


# Формируем первоначальный список чисел с помощью генератора.
list_numbers = task_2.gen_list(15)
print(f'Сгенерированный список:\t\t{list_numbers}')

# Хочу обратить внимание на то, что я не знал можно ли использовать .count() для списков,
# или лучше обойтись без него. Поэтому я реализовал оба варианта с .count() и через свою фукнцию.

# Создаем список с элементами, не имеющими повторений, с помощью моей функции.
my_func_list = [number for number in list_numbers if unique_find(number, list_numbers)]
print(f'Новый список (моя функция):\t{my_func_list}')
# или лучше обойтись без него. Поэтому я реализовал оба варианта с .count() и через свою фукнцию.

# Создаем список с элементами, не имеющими повторений, с помощью функции .count().
count_list = [number for number in list_numbers if list_numbers.count(number) == 1]
print(f'Новый список (.count()):\t{count_list}')
