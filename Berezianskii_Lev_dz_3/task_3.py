def my_func(*args):
    """Функция возвращает сумму наибольших двух аргументов."""
    # Преобразуем в список.
    args = list(args)
    # Определяем переменную максимального аргумента.
    first_max_arg = args[0]
    for arg in args:
        # Если текущий элемент больше данного максимального.
        if arg > first_max_arg:
            first_max_arg = arg
    # Удаляем из списка максимальный элемент.
    args.remove(first_max_arg)
    # Определяем переменную второго максимального элемента.
    second_max_arg = args[0]
    for arg in args:
        # Если текущий элемент больше данного максимального.
        if arg > second_max_arg:
            second_max_arg = arg
    # Возвращаем сумму наибольших двух аргументов.
    return first_max_arg + second_max_arg


print(my_func(2, 9, 4))
print(my_func(0, 1, 4, -2, 3, 1))
print(my_func(-3, -4, -2, -2, -13))
print(my_func(0, 0, 0))
print(my_func(1, 1, 11, 11))
