def my_func(x, y):
    """Функция возвращает число, возведенное в отрицательную степень."""
    result_number = 1
    # Производим возведение в положительную степень.
    for el in range(y * (-1)):
        result_number *= x
    # Переворачиваем дробь, т.к. степень отрицательная.
    result_number = 1 / result_number
    # Возвращаем результат.
    return result_number


def my_func_easy(x, y):
    """Функцию возвращает число, возведенное в степень."""
    return x ** y


user_x = float(input('Введите число: '))
user_y = int(input('Введите степень: '))
# Вызываем функцию.
print(f'Результат (без использования **): {my_func(user_x, user_y)}')
print(f'Результат (с использованием **): {my_func_easy(user_x, user_y)}')
