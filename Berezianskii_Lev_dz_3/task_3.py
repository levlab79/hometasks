def my_func(*args):
    """Функция возвращает сумму наибольших двух аргументов."""
    result_sum = 0
    # Преобразуем кортеж в список.
    args = list(args)
    # Повторяем цикл 2 раза.
    for index in range(2):
        local_max = args[0]
        # Пробегаем весь список.
        for number in args:
            if number > local_max:
                local_max = number
        # Удаляем из списка максимальный элемент, который мы нашли.
        args.remove(local_max)
        # Увеличиваем общую сумму.
        result_sum += local_max
    # Возвращаем сумму наибольших двух аргументов.
    return result_sum


# Вызываем функцию с указанием 3 аргументов.
print(my_func(2, 9, 4))
print(my_func(0, 0, 0))
print(my_func(3, 3, 3))
print(my_func(-1, -3, 3))
print(my_func(1, -3, 0))

# Вызываем функцию с указанием более 3 аргументов.
print(my_func(0, 1, 4, -2, 3, 1))
print(my_func(-3, -4, -2, -2, -13))
print(my_func(1, 1, 11, 11))
